from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-us')
def about():
    return render_template('about-us.html')

@app.route('/trainers')
def trainers():
    return "render new template"

@app.route('/all-courses')
def courses():
    return render_template('all-courses.html')

@app.route('/success-stories')
def success_stories():
    return render_template('success-stories.html')

@app.route('/contact-us')
def contact():
    return render_template('contact-us.html')


app.run(debug=True, port=8000, host='0.0.0.0')
