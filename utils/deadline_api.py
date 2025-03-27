
import os
import requests

DEADLINE_API = os.getenv("DEADLINE_REPO", "http://localhost:8082")

def get_jobs(status_filter=None, limit=50):
    try:
        response = requests.get(f"{DEADLINE_API}/api/jobs?Limit={limit}")
        response.raise_for_status()
        jobs = response.json()

        if status_filter:
            jobs = [job for job in jobs if job.get("JobStatus") == status_filter]

        return sorted(jobs, key=lambda j: j.get("JobName", "zzz"))
    except requests.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Deadline : {e}")
        return []

def get_job_summary():
    jobs = get_jobs(limit=500)
    summary = {"Queued": 0, "Rendering": 0, "Suspended": 0, "Completed": 0, "Failed": 0}
    for job in jobs:
        status = job.get("JobStatus", "Unknown")
        if status in summary:
            summary[status] += 1
        else:
            summary[status] = 1
    return summary

def get_job_by_id(job_id):
    try:
        response = requests.get(f"{DEADLINE_API}/api/jobs/{job_id}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération du job {job_id} : {e}")
        return None

def suspend_job(job_id):
    try:
        response = requests.post(f"{DEADLINE_API}/api/jobs/{job_id}/suspend")
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Erreur lors de la suspension du job {job_id} : {e}")
        return False

def resume_job(job_id):
    try:
        response = requests.post(f"{DEADLINE_API}/api/jobs/{job_id}/resume")
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Erreur lors de la reprise du job {job_id} : {e}")
        return False
