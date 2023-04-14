from flask import Flask, request, jsonify
from pymongo import MongoClient, ReturnDocument
from jsonschema import validate
from flask_restful import Api,Resource
app = Flask(__name__)
api=Api(app)

# Connect to the database
# client = MongoClient('mongodb://localhost:27017')
client = MongoClient('mongodb+srv://<user-name>:<password>@cluster0.x18sgkj.mongodb.net/test')
db = client['corider']
collection = db['users']

# User schema
user_schema={
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "email": {
      "type": "string",
      "format": "email"
    },
    "password": {
      "type": "string"
    }
  },
  "required": ["id","name", "email", "password"]
}

class User(Resource):
    # /users - Returns a list of users
    def get(self,id=None):
        # Single user
        if id:
            try:
                user = collection.find_one({'id': id})
                if user is None:
                    return jsonify({'message': 'User not found'})
                return jsonify({'id': user['id'], 'name': user['name'], 'email': user['email']})
            except: 
                return jsonify({"message": "No user found"})
        # All users
        else:
            users=[]
            try: 
                for user in collection.find():
                    users.append({'id': user['id'], 'name': user['name'], 'email': user['email']})
                    
                if len(users)==0:
                    return jsonify({"message": "No user found"})
                
                return jsonify(users)
            except :
                return jsonify({"message": "No user found"})

    # /users - Creates a new user
    def post(self):
        try:
            # Validate user data
            user = request.get_json()
            errors=validate(instance=user,schema=user_schema)
            if errors:
                return jsonify({'message': 'Validation error'})

            # check for the existing user
            user_exist = collection.find_one({'id': user['id']})
            if user_exist:
                return jsonify({'message': 'User already exist'})
            # Insert user data into the database
            result = collection.insert_one(user)
            user['_id'] = str(result.inserted_id)
            return jsonify(user)
        except: 
            return jsonify({"message": "Some error occured"})

    # /users/<id> - Updates the user data
    def put(self, id):
        try:
            # Validate user data    
            user = request.get_json()
            errors = validate(instance=user,schema=user_schema)
            if errors:
                return jsonify({'message': 'Validation error'})

            # Update user data in the database
            result = collection.find_one_and_update({'id': id}, {'$set': user}, return_document=ReturnDocument.AFTER)
            if result is None:
                return jsonify({'message': 'User not found'})
            result['_id'] = str(result['_id'])
            return jsonify(result)
        except:
            return jsonify({"message": "Some error occured"})
        


    # /users/<id> - Deletes the user
    def delete(self, id):
        try:
            result = collection.delete_one({'id': id})
            if result.deleted_count == 0:
                return jsonify({'message': 'User not found'})
            return jsonify({'message': 'User deleted'})
        except:
            return jsonify({"message": "User not found"})

api.add_resource(User, '/users', '/users/<int:id>')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)