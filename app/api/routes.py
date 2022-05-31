from flask import json, Blueprint, jsonify, request, flash, redirect, url_for, render_template
from flask_login import current_user
from app.models import MarvelCharacter, User, db
from .services import token_required
from.apiforms import ApiCharForm
api = Blueprint('api', __name__, template_folder='api_templates', url_prefix='/api')


@api.route('/test', methods=['GET'])
def test():


    x = User.query.all()
    y = MarvelCharacter.query.all()[0]
    return jsonify(y.to_dict()), 200

@api.route('/MarvelCharacters', methods=['GET'])
def getMarvelCharacters():
    marvelcharacter = MarvelCharacter.query.all()
    marvelcharacter = [mc.to_dict() for mc in marvelcharacter]
    return jsonify(marvelcharacter), 200

@api.route('/create', methods=['GET', 'POST'])
#@token_required
def createMarvelCharacters():
    marform = ApiCharForm()
    if request.method =='POST':
        if marform.validate_on_submit():
            print(marform.data)
            newdict = {'name':marform.name.data, 'description':marform.description.data, 'super_power':marform.super_power.data, 'comics_appeared_in':marform.comics_appeared_in.data}
            newestdict = json.dumps(newdict, indent=2, separators=(',', ': '))
            loaded_newestdict = json.loads(newestdict)
            
            #marvelcharacter = MarvelCharacter(marform.name.data, marform.description.data, marform.comics_appeared_in.data, marform.super_power.data)
            marvelcharacter = MarvelCharacter(loaded_newestdict, owner_id=current_user.id)
            print(marvelcharacter)
            
            #try:
            db.session.add(marvelcharacter)
            db.session.commit()
            print(marvelcharacter.owner_id)
            flash(f'Your new character {marvelcharacter.name} has been made!', category='success')
            return render_template('newcharacter.html', form=marform)
    return render_template('newcharacter.html', form=marform)
            #except:
            #    flash('Sorry, that did not work. Try again', 'danger')
            #    return redirect(url_for('api.create'))

    #try:
        #newdict = request.get_json()
        #print(newdict)
        #a = MarvelCharacter(newdict)
    #except:
    #    return jsonify({'error': 'improper request of body data'}), 400
    #try:
        #Make sure that the character name is unique or else this code here is essentially useless.
    #    db.session.add(a)
    #    db.session.commit()
    #except:
    #    return jsonify({'error': 'This hero is already in the database'}), 400
    #return jsonify({'created': a.to_dict()}), 200
    

@api.route('/MarvelCharacter/<string:name>', methods=['GET'])
def getMarvelCharacterName(name):
    print(name)
    marvelcharacter = MarvelCharacter.query.filter_by(name=name).first()
    print(marvelcharacter)
    if marvelcharacter:
        return jsonify(marvelcharacter.to_dict()), 200
    return jsonify({'error': f'no such marvel character with the name: {marvelcharacter}'}), 404


@api.route('/update/<string:id>', methods=['POST'])
@token_required
def updateMarvelCharacter(id):
    try: 
        newvals = request.get_json()
        marvelcharacter = MarvelCharacter.query.get(id)
        marvelcharacter.from_dict(newvals)
        db.session.commit()
        return jsonify({'Updated Marvel Character': marvelcharacter.to_dict()}), 200
    except:
        return jsonify({'Request failed': 'Invalid request or Marvel Character ID does not exist.'}), 400


@api.route('delete/<string:id>', methods=['DELETE'])
@token_required
def removeMarvelCharacter(id):
    #NEED TO TEST THIS
    marvelcharacter = MarvelCharacter.query.get(id)
    if not marvelcharacter:
        return jsonify({'Remove failed': 'No character with ID in the database'}), 404
    db.session.delete(marvelcharacter)
    db.session.commit()
    return jsonify({'Removed character': marvelcharacter.to_dict()}), 200