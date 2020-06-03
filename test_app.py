import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Concert, Player, add_test_data, db_drop_and_create_all
from config import jwt_tokens
# from auth.auth import AuthError, requires_auth

class AgencyTest(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "players_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        # self.database_path = "postgres://gfkivkkacbfdtw:1f6615a42dee7a00e77ea56b97a09b35e85526f7b4bfaece1e8bc4fe14111ad8@ec2-3-231-16-122.compute-1.amazonaws.com:5432/daloe12oi67tmb"
        setup_db(self.app, self.database_path)

        # start with sample data
        db_drop_and_create_all()
        add_test_data()

        # sample new concert
        self.new_concert = {
            'title': "LSO returns!",
            'style': "Romantic",
            'concert_date': '20200901'
        }

        # sample incomplete new concert
        self.incomplete_new_concert = {
            'title': "LSO returns!",
            'style': "Romantic"
        }

        # sample patch concert
        self.patch_concert = {
            'title': "LSO returns (updated)!"
        }

        # sample new player
        self.new_player = {
            'name': "Foo Bar",
            'instrument': "Oboe",
            'experience': 5
        }

        # sample incomplete new concert
        self.incomplete_new_player = {
            'name': "Foo Bar",
            'instrument': "Oboe"
        }

        # sample patch player
        self.patch_player = {
            'name': "Foo Update Bar",
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    #----------------------------------------------------------------------------#
    # Tests - GET concerts
    #----------------------------------------------------------------------------#

    def test_get_concerts_by_manager(self):
        res = self.client().get('/concerts', headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['no_concerts'])


    def test_get_concerts_by_fixer(self):
        res = self.client().get('/concerts', headers={
            "Authorization": jwt_tokens['Concert_Fixer']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['no_concerts'])

    
    def test_get_concerts_by_assistant(self):
        res = self.client().get('/concerts', headers={
            "Authorization": jwt_tokens['Concert_Assistant']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['no_concerts'])

    #----------------------------------------------------------------------------#
    # Tests - POST concerts
    #----------------------------------------------------------------------------#

    def test_post_concerts_by_manager(self):
        res = self.client().post('/concerts', json=self.new_concert, headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_concert'])
        self.assertTrue(data['concerts'])


    def test_error_422_post_incomplete_concerts_by_manager(self):
        res = self.client().post('/concerts', json=self.incomplete_new_concert, headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    
    def test_error_401_post_concerts_by_fixer(self):
        res = self.client().post('/concerts', json=self.new_concert, headers={
            "Authorization": jwt_tokens['Concert_Fixer']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_error_401_post_concerts_by_assistant(self):
        res = self.client().post('/concerts', json=self.new_concert, headers={
            "Authorization": jwt_tokens['Concert_Assistant']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    #----------------------------------------------------------------------------#
    # Tests - PATCH concerts
    #----------------------------------------------------------------------------#

    def test_patch_concerts_by_manager(self):
        res = self.client().patch('/concerts/1', json=self.patch_concert, headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_concert'])


    def test_error_401_patch_concerts_by_fixer(self):
        res = self.client().patch('/concerts/1', json=self.patch_concert, headers={
            "Authorization": jwt_tokens['Concert_Fixer']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    
    def test_error_401_patch_concerts_by_assistant(self):
        res = self.client().patch('/concerts/1', json=self.patch_concert, headers={
            "Authorization": jwt_tokens['Concert_Assistant']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    #----------------------------------------------------------------------------#
    # Tests - DELETE concerts
    #----------------------------------------------------------------------------#

    def test_delete_concerts_by_manager(self):
        res = self.client().delete('/concerts/1', headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    
    def test_error_401_delete_concerts_by_fixer(self):
        res = self.client().delete('/concerts/2', headers={
            "Authorization": jwt_tokens['Concert_Fixer']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_error_401_delete_concerts_by_assistant(self):
        res = self.client().delete('/concerts/2', headers={
            "Authorization": jwt_tokens['Concert_Assistant']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    #----------------------------------------------------------------------------#
    # Tests - GET players
    #----------------------------------------------------------------------------#

    def test_get_players_by_manager(self):
        res = self.client().get('/players', headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['no_players'])
        self.assertTrue(data['players'])


    def test_get_players_by_fixer(self):
        res = self.client().get('/players', headers={
            "Authorization": jwt_tokens['Concert_Fixer']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['no_players'])
        self.assertTrue(data['players'])

    
    def test_get_players_by_assistant(self):
        res = self.client().get('/players', headers={
            "Authorization": jwt_tokens['Concert_Assistant']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['no_players'])
        self.assertTrue(data['players'])

    #----------------------------------------------------------------------------#
    # Tests - POST players
    #----------------------------------------------------------------------------#

    def test_post_players_by_manager(self):
        res = self.client().post('/players', json=self.new_player, headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_player'])
        self.assertTrue(data['players'])


    def test_error_422_post_incomplete_players_by_manager(self):
        res = self.client().post('/players', json=self.incomplete_new_player, headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    
    def test_post_players_by_fixer(self):
        res = self.client().post('/players', json=self.new_player, headers={
            "Authorization": jwt_tokens['Concert_Fixer']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_player'])
        self.assertTrue(data['players'])


    def test_error_401_post_players_by_assistant(self):
        res = self.client().post('/players', json=self.new_concert, headers={
            "Authorization": jwt_tokens['Concert_Assistant']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    #----------------------------------------------------------------------------#
    # Tests - PATCH players
    #----------------------------------------------------------------------------#

    def test_patch_players_by_manager(self):
        res = self.client().patch('/players/1', json=self.patch_player, headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_player'])


    def test_patch_players_by_fixer(self):
        res = self.client().patch('/players/2', json=self.patch_player, headers={
            "Authorization": jwt_tokens['Concert_Fixer']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_player'])


    def test_error_401_patch_players_by_assistant(self):
        res = self.client().patch('/players/1', json=self.patch_player, headers={
            "Authorization": jwt_tokens['Concert_Assistant']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    #----------------------------------------------------------------------------#
    # Tests - DELETE players
    #----------------------------------------------------------------------------#

    def test_delete_players_by_manager(self):
        res = self.client().delete('/players/1', headers={
            "Authorization": jwt_tokens['Concert_Manager']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    
    def test_delete_players_by_fixer(self):
        res = self.client().delete('/players/2', headers={
            "Authorization": jwt_tokens['Concert_Fixer']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    
    def test_error_401_delete_players_by_assistant(self):
        res = self.client().delete('/players/2', headers={
            "Authorization": jwt_tokens['Concert_Assistant']
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()