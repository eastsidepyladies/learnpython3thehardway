from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")
def index():
    name = request.args.get('name', 'Nobody')
    greet = request.args.get('greet', 'Hi')
    
    if name:
        if greet:
            greeting = f"{greet} {name}"
        else: 
            greeting = f"Hello, {name}"
    else:
        greeting = "Hi, there!"
        
    return render_template("index.html", greeting=greeting)
    
    
if __name__ == "__main__":
    app.run()
    
#C:/Python/python.exe form_test.py
# opens http://localhost:5000/hello?name=Jose&greet=Hola

