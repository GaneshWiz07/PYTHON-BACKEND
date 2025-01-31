from flask import Flask, render_template, request,jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
Api = Api(app)
class CSKTeam(Resource):
    team = []
    def get(self):
        return {"team": self.team}
    def post(self):
        data = request.get_json()
        if data:
            self.team.append(data.get('name'))
            return {"team": self.team}
        return jsonify({"message": "No data received"})    
Api.add_resource(CSKTeam, '/csk')
@app.route('/')
def home():
    return render_template('home.html', title="Home", message="Welcome to the Home Page!")
@app.route('/about')
def about():
    return render_template('about.html', title="About", content="This is the About page.")
@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        return {"message": "Data received", "data": data}
    return {"message": "Send a POST request with JSON data"}

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', title="Greet", name=name)
if __name__ == '__main__':
    app.run(debug=True)