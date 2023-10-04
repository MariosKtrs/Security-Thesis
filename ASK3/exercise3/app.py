from flask import Flask, request, render_template_string, render_template
import os;

app = Flask(__name__)


@app.route('/')
def home():
    name = ""
    tags = request.args.get('name');
    if request.args.get('name'):
        return render_template_string('Wait! This is top secret! '+request.args.get('name')) 
    else:
        return render_template('index.html') 
    
if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'PPYQ{Q4qdip' 
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=True, host='0.0.0.0', port=port)
