from app import app
from flask import render_template
#remember, the from app refers to the folder, and the import app is from app instantiation from the __init__ file

@app.route('/')
def home():


    return render_template('index.html')