from flask import request, Blueprint
from BLog import db, bcrypt, celery
from flask import jsonify
from flask_jwt_extended import (create_access_token)
from BLog.models import User
from BLog.users.utils import send_email

users = Blueprint('users', __name__)

#Register User

@users.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        user = User(username=data['username'], email=data['email'], password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        result = {'email': user.email + " registered"}
        return jsonify({"result": result}), 201

# Login User
@users.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        password = data['password']
        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity={
                'username': user.username,
                'email': user.email
            })
            result = jsonify({'token': access_token})

        else:
            result = jsonify({'error': 'invalid username password'}), 404

    return result



# reset Password route
@users.route("/reset_password", methods=['POST', 'GET'])
def reset_request():
    data = request.get_json()
    reset.delay(data['email'])
    return jsonify({'message': 'email sent'})

@users.route("/change_password",methods=['POST'])
def change_pass():
    data = request.get_json()
    print(data)
    user = User.query.filter_by(email=data['email']).first()
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user.password=hashed_pw
    db.session.commit()
    return jsonify({'message':'success'})



@celery.task
def reset(email):
    user = User.query.filter_by(email=email).first()
    send_email(user, email)
