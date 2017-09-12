from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello", methods=['POST', 'GET'])
def index():

    greeting = "Hello World" 
    
    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    
    return render_template("hello_form.html")
    
    
if __name__ == "__main__":
    app.run()
    
# C:/Python/python.exe app.py
# FLASK_APP=app.py flask run
# opens http://localhost:5000/

