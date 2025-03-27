
import os
import openstack

def get_connection():
    return openstack.connect(
        auth_url=os.getenv('OS_AUTH_URL'),
        project_name=os.getenv('OPENSTACK_PROJECT'),
        username=os.getenv('OPENSTACK_USER'),
        password=os.getenv('OPENSTACK_PASS'),
        user_domain_name='default',
        project_domain_name='default',
    )

def get_workers():
    conn = get_connection()
    servers = conn.compute.servers(details=True, all_projects=False)
    workers = []
    for server in servers:
        if 'render-worker' in server.name:
            workers.append({
                'id': server.id,
                'name': server.name,
                'status': server.status,
                'age': server.launched_at
            })
    return workers

def scale_up():
    conn = get_connection()
    image = conn.compute.find_image('windows-10-render')
    flavor = conn.compute.find_flavor('standard.medium')
    network = conn.network.find_network('private-network')
    keypair = conn.compute.find_keypair('render-key')

    server_name = f"render-worker-{os.urandom(2).hex()}"

    user_data_script = '''#cloud-config
write_files:
  - path: "C:\\DeadlineInit\\setup.ps1"
    content: |
      Start-Process "C:\\Program Files\\Thinkbox\\Deadline10\\bin\\deadlineworker.exe"
      Rename-Computer -NewName "{server_name}" -Force -Restart
'''

    server = conn.compute.create_server(
        name=server_name,
        image_id=image.id,
        flavor_id=flavor.id,
        networks=[{"uuid": network.id}],
        key_name=keypair.name,
        user_data=user_data_script.encode('utf-8'),
    )
    conn.compute.wait_for_server(server)
    print(f"✅ VM {server_name} lancée")

def scale_down():
    conn = get_connection()
    servers = get_workers()
    if servers:
        oldest = sorted(servers, key=lambda x: x['age'])[0]
        conn.compute.delete_server(oldest['id'])
        print(f"🗑 VM {oldest['name']} supprimée")
