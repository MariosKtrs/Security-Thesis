from flask import Flask, request, render_template
from jinja2 import Environment, Markup
import os

app = Flask(__name__)
Jinja2 = Environment()

@app.route('/')
def home():
    name = "admin"
    tags = Jinja2.from_string('Welcome Back ' + str(request.values.get('name'))).render()
    return render_template('index.html',tags=tags) 
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=True, host='0.0.0.0', port=port)
