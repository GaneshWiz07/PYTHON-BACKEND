from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html', title="Home", message="Welcome to the Home Page!")
@app.route('/about')
def about():
    return render_template('about.html', title="About", content="This is the About page.")
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', title="Greet", name=name)
if __name__ == '__main__':
    app.run(debug=True)