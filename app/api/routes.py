from flask import Blueprint
from app.models import MarvelCharacter, User
from flask import jsonify
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/test', methods=['GET'])
def test():


    x = User.query.all()
    y = MarvelCharacter.query.all()[0]
    return jsonify(y.to_dict()), 200