import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from database.models import setup_db, db_drop_and_create_all, add_test_data, Concert, Player
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # To reset database
    # db_drop_and_create_all()
    # add_test_data()

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    #----------------------------------------------------------------------------#
    # Concerts
    #----------------------------------------------------------------------------#

    '''
    Endpoint to handle GET requests for concerts
    '''
    @app.route('/concerts')
    @requires_auth('get:concerts')
    def get_concerts(payload):
        if 'get:concerts' not in payload['permissions']:
            abort(405)

        concerts = Concert.query.all()

        if len(concerts) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'no_concerts': len(concerts),
            'concerts': [con.format() for con in concerts]
        })

    '''
    Endpoint to handle POST requests for concerts
    '''
    @app.route('/concerts', methods=['POST'])
    @requires_auth('post:concerts')
    def post_concert(payload):
        if 'post:concerts' not in payload['permissions']:
            abort(405)

        body = request.get_json()
        title = body.get('title')
        style = body.get('style')
        concert_date = body.get('concert_date')

        try:
            concert = Concert(
                title=title,
                style=style,
                concert_date=concert_date
            )

            concert.insert()
            concerts = Concert.query.all()

            return jsonify({
                'success': True,
                'new_concert': concert.id,
                'concerts': len(concerts)
            })
        except:
            abort(422)

    '''
    Endpoint to handle DELETE requests for concerts
    '''
    @app.route('/concerts/<int:concert_id>', methods=['DELETE'])
    @requires_auth('delete:concerts')
    def delete_concert(payload, concert_id):
        if 'delete:concerts' not in payload['permissions']:
            abort(405)
        try:
            concert = Concert.query.filter(
                Concert.id == concert_id).one_or_none()

            if concert is None:
                abort(404)

            concert.delete()

            return jsonify({
                'success': True,
                'deleted': concert.id
            })
        except:
            abort(422)

    '''
    Endpoint to handle PATCH requests for concerts
    '''
    @app.route('/concerts/<int:concert_id>', methods=['PATCH'])
    @requires_auth('patch:concerts')
    def patch_concert(payload, concert_id):
        if 'patch:concerts' not in payload['permissions']:
            abort(405)

        body = request.get_json()
        title = body.get('title', None)
        style = body.get('style', None)
        concert_date = body.get('concert_date', None)

        try:
            concert = Concert.query.filter(
                Concert.id == concert_id).one_or_none()

            if title:
                concert.title = title
            if style:
                concert.style = style
            if concert_date:
                concert.concert_date = concert_date

            concert.update()

            return jsonify({
                'success': True,
                'updated_concert': concert.id
            })
        except:
            abort(422)

    #----------------------------------------------------------------------------#
    # Players
    #----------------------------------------------------------------------------#

    '''
    Endpoint to handle GET requests for players
    '''
    @app.route('/players')
    @requires_auth('get:players')
    def get_players(payload):
        if 'get:players' not in payload['permissions']:
            abort(405)

        players = Player.query.all()

        if len(players) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'no_players': len(players),
            'players': [pl.format() for pl in players]
        })

    '''
    Endpoint to handle POST requests for players
    '''
    @app.route('/players', methods=['POST'])
    @requires_auth('post:players')
    def post_player(payload):
        if 'post:players' not in payload['permissions']:
            abort(405)

        body = request.get_json()
        name = body.get('name')
        instrument = body.get('instrument')
        experience = body.get('experience')

        try:
            player = Player(
                name=name,
                instrument=instrument,
                experience=experience
            )

            player.insert()
            players = Player.query.all()

            return jsonify({
                'success': True,
                'new_player': player.id,
                'players': len(players)
            })
        except:
            abort(422)

    '''
    Endpoint to handle DELETE requests for players
    '''
    @app.route('/players/<int:player_id>', methods=['DELETE'])
    @requires_auth('delete:players')
    def delete_player(payload, player_id):
        if 'delete:players' not in payload['permissions']:
            abort(405)

        try:
            player = Player.query.filter(
                Player.id == player_id).one_or_none()

            if player is None:
                abort(404)

            player.delete()

            return jsonify({
                'success': True,
                'deleted': player.id
            })
        except:
            abort(422)

    '''
    Endpoint to handle PATCH requests for players
    '''
    @app.route('/players/<int:player_id>', methods=['PATCH'])
    @requires_auth('patch:players')
    def patch_player(payload, player_id):
        if 'patch:players' not in payload['permissions']:
            abort(405)

        body = request.get_json()
        name = body.get('name', None)
        instrument = body.get('instrument', None)
        experience = body.get('experience', None)

        try:
            player = Player.query.filter(
                Player.id == player_id).one_or_none()

            if name:
                player.name = name
            if instrument:
                player.instrument = instrument
            if experience:
                player.experience = experience

            player.update()

            return jsonify({
                'success': True,
                'updated_player': player.id
            })
        except:
            abort(422)


    #----------------------------------------------------------------------------#
    # Error Handlers
    #----------------------------------------------------------------------------#

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404


    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify(error.error), error.status_code


    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unauthorized'
        }), 401


    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'forbidden'
        }), 403


    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    return app

app = create_app()

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(host='127.0.0.1', port=8080, debug=True)
