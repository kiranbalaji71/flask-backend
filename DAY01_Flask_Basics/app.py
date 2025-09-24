from flask import request, jsonify
from config import app ,db
from models import User

@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    json_users = list(map(lambda user: user.to_json(), users))
    return jsonify({'users': json_users}),200

@app.route('/create_users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    email = request.json.get('email')
    if not username or not email:
        return jsonify({'message': 'Missing username or email'}), 400
 
    new_user = User(username=username, email=email)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.json
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()

    return jsonify({'message': 'User updated successfully'}), 200


@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200
 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)