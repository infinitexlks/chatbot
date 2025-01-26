
This is a simple REST API built with Flask in Python that allows you to perform CRUD operations (Create, Read, Update, Delete) on a list of users.

### Features:
1. **GET** `/users` - Retrieve all users.
2. **GET** `/users/<id>` - Retrieve a user by their ID.
3. **POST** `/users` - Create a new user.
4. **PUT** `/users/<id>` - Update an existing user.
5. **DELETE** `/users/<id>` - Delete a user by their ID.

### Requirements:
- Python 3.x
- Flask library (install with `pip install Flask`)

### Setup Instructions:
1. Save this file as `app.py`.
2. Install Flask by running: `pip install Flask`.
3. Run the API with the command: `python app.py`.
4. Use the following endpoints to interact with the API:
   - GET all users: `curl http://127.0.0.1:5000/users`
   - GET a user by ID: `curl http://127.0.0.1:5000/users/1`
   - POST create a new user: 
     ```py
     curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice", "email": "alice@example.com"}' http://127.0.0.1:5000/users
     ```
   - PUT update a user: 
     ```py
     curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name", "email": "updated@example.com"}' http://127.0.0.1:5000/users/1
     ```
   - DELETE a user: `curl -X DELETE http://127.0.0.1:5000/users/1`

### Notes:
- This API uses an in-memory list for users. Data will reset when the server restarts.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data
```py
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}
]
```
# GET /users: Get all users
```py
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200
```

# GET /users/<id>: Get a user by ID
```py
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((user for user in users if user["id"] == id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# POST /users: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if "name" in data and "email" in data:
        new_user = {
            "id": len(users) + 1,
            "name": data["name"],
            "email": data["email"]
        }
        users.append(new_user)
        return jsonify(new_user), 201
    return jsonify({"message": "Invalid data"}), 400

# PUT /users/<id>: Update an existing user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = next((user for user in users if user["id"] == id), None)
    if user:
        data = request.get_json()
        user["name"] = data.get("name", user["name"])
        user["email"] = data.get("email", user["email"])
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# DELETE /users/<id>: Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [user for user in users if user["id"] != id]
    return jsonify({"message": "User deleted"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
