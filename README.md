# Orchestra-Players-Agency

The Orchestra Agency models a company that is responsible for preparing new concerts and assigning players to each concert. 

Final Project for [Udacity Full-Stack Web Developer Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).

## Getting Started

* Each roles' JWT token can be found at [config.py](https://github.com/IvanCheng1/Orchestra-Players-Agency/blob/master/config.py)
* Heroku link is hosted at: [Orchestra-Agency](https://orchestra-agency.herokuapp.com/)

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server locally

From within the project directory first ensure you are working using your created virtual environment. Ensure postgres.app is running and create a database called "players".

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
python3 app.py
```

## Specifications

### Models
* Concerts with attributes title, style and concert date
* Players with attributes name, years of experience and instrument

### Roles
* Assistant
    * Can view concerts and players
* Fixer
    * All the above
    * Add / delete players from the database
    * Modify players 
* Concert manager
    * All the above
    * Modify conerts
    * Add or delete a concert from the database

## Tests

1. Ensure postgres.app is running and create a database called "players_test".
2. Execute the tests, run

```
python test_app.py
```

## Error Handling

Errors are returned as JSON objects in the following format:

```python
{
    "success": False,
    "error": 400,
    "message": "bad request"
}

```

The API will return five error types when requests fail:

* 401: unauthorized
* 403: forbidden
* 404: resource not found
* 405: method not allowed
* 422: unprocessable

## Endpoints

* [GET /concerts](#get-concerts)
* [POST /concerts](#post-concerts)
* [DELETE /concerts/int:concert_id](#delete-concertsintconcert_id)
* [PATCH /concerts/int:concert_id](#patch-concertsintconcert_id)
* [GET /players](#get-players)
* [POST /players](#post-players)
* [DELETE /players/int:player_id](#delete-playersintplayer_id)
* [PATCH /players/int:player_id](#patch-playersintplayer_id)
* [POST /players/int:player_id](#post-playersintplayer_id)

#### GET /concerts

- General:
  - Returns: a dictionary of concerts with details for each concert
- Sample: `curl https://orchestra-agency.herokuapp.com/concerts -X GET -H "authorization: Bearer {{TOKEN}}"`
```
{
   "concerts" : [
      {
         "concert_date" : "Wed, 01 Jan 2020 00:00:00 GMT",
         "id" : 1,
         "players_booked" : 1,
         "title" : "Bach returns",
         "style" : "Baroque"
      },
      {
         "style" : "Classical",
         "title" : "Mozart returns",
         "players_booked" : 0,
         "concert_date" : "Sat, 01 Jan 2022 00:00:00 GMT",
         "id" : 2
      }
   ],
   "success" : true,
   "no_concerts" : 2
}
```

#### POST /concerts

- General:
  - Returns: JSON object with the success value, id of the new concert and the updated total number of concerts
- Sample: `curl https://orchestra-agency.herokuapp.com/concerts -X POST -H "Content-Type: application/json" -d '{"title": "Bach returns", "style": "Baroque", "concert_date": "20200101"}' -H "authorization: Bearer {{TOKEN}}"`
```
{
   "concerts" : 3,
   "new_concert" : 3,
   "success" : true
}
```

#### DELETE /concerts/<int:concert_id>

- General:
  - Deletes the concert of the given concert id if exists
  - Returns: JSON object with the success value and the deleted concert id
- Sample: `curl https://orchestra-agency.herokuapp.com/concerts/3 -X DELETE -H "authorization: Bearer {{TOKEN}}"`
```
{
   "deleted" : 3,
   "success" : true
}
```

#### PATCH /concerts/<int:concert_id>

- General:
  - Edits the concert of the given id if exists
  - Returns: JSON object with the success value and the id of updated concert
- Sample: `curl https://orchestra-agency.herokuapp.com/concerts/3 -X PATCH -H "Content-Type: application/json" -d '{"title": "Bach returns (updated)"}' -H "authorization: Bearer {{TOKEN}}"`
```
{
   "updated_concert" : 3,
   "success" : true
}
```

#### GET /players

- General:
  - Returns: a dictionary of players with detail of each player
- Sample: `curl https://orchestra-agency.herokuapp.com/players -X GET -H "authorization: Bearer {{TOKEN}}"`
```
{
   "no_players" : 2,
   "success" : true,
   "players" : [
      {
         "concerts_booked" : 1,
         "experience" : "3 year(s)",
         "instrument" : "Violin",
         "name" : "Austin Pierce",
         "id" : 1
      },
      {
         "id" : 2,
         "instrument" : "Broom",
         "name" : "Harry Potter",
         "experience" : "2 year(s)",
         "concerts_booked" : 0
      }
   ]
}
```

#### POST /players

- General:
  - Returns: JSON object with the success value, id of the new player and the updated total number of players
- Sample: `curl https://orchestra-agency.herokuapp.com/players -X POST -H "Content-Type: application/json" -d '{"name": "Hermione Granger", "instrument": "Wand", "experience": 19}' -H "authorization: Bearer {{TOKEN}}"`
```
{
   "players" : 3,
   "success" : true,
   "new_player" : 3
}
```

#### DELETE /players/<int:player_id>

- General:
  - Deletes the concert of the given player id if exists
  - Returns: JSON object with the success value and the deleted player id
- Sample: `curl https://orchestra-agency.herokuapp.com/players/3 -X DELETE -H "authorization: Bearer {{TOKEN}}"`
```
{
   "deleted" : 3,
   "success" : true
}
```

#### PATCH /players/<int:player_id>

- General:
  - Edits the player of the given id if exists
  - Returns: JSON object with the success value and the id of updated player
- Sample: `curl https://orchestra-agency.herokuapp.com/player/3 -X PATCH -H "Content-Type: application/json" -d '{"name": "Hermione Granger (updated)"}' -H "authorization: Bearer {{TOKEN}}"`
```
{
   "updated_player" : 3,
   "success" : true
}
```

#### POST /players/<int:player_id>

- General:
  - Binds the player to a particular concert if concert exists
  - Returns: JSON object with the success value, the player id and the concert id
- Sample: `curl https://orchestra-agency.herokuapp.com/player/3 -X POST -H "Content-Type: application/json" -d '{"concert_id": 1}' -H "authorization: Bearer {{TOKEN}}"`
```
{
   "success" : true,
   "player" : 3,
   "concert" : 1
}
```
