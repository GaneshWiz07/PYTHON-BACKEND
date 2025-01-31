from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app1 = Flask(__name__)
api1 = Api(app1)

class HOTEL(Resource):
    menu = ["Burger", "Pizza", "Fries"]

    def get(self):
        return {"menu": self.menu}

    def post(self):
        data = request.get_json()
        if data and 'item' in data:
            self.menu.append(data['item'])
            return {"message": "Item added successfully"}, 201
        return jsonify({"message": "No data received"}), 400

    def post(self, index):
        if 0 <= index < len(self.menu):
            removed_item = self.menu.pop(index)
            return {"message": f"Item '{removed_item}' removed successfully"}, 200
        else:
            return {"message": "Invalid index"}, 400

api1.add_resource(HOTEL, '/hotel', '/addmenu', '/removemenu/<int:index>')

if __name__ == '__main__':
    app1.run(debug=True)