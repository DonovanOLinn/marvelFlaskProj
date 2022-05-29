from app.models import db, User
from app import app

@app.shell_context_processor
def shell_context():
    return {'db' : db, 'User' : User}