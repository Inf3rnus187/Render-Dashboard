
import os

class Config:
    USERNAME = os.getenv('DASH_USER')
    PASSWORD = os.getenv('DASH_PASS')
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    DEADLINE_REPO = os.getenv('DEADLINE_REPO')

class User:
    def __init__(self, username):
        self.id = username
        self.role = 'admin' if username == Config.USERNAME else 'viewer'

    def is_authenticated(self): return True
    def is_active(self): return True
    def is_anonymous(self): return False
    def get_id(self): return self.id
