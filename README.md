# Orchestra-Players-Agency

The Orchestra Agency models a company that is responsible for preparing new concerts and assigning players to each concert. 

Final Project for [Udacity Full-Stack Web Developer Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).

## Getting Started

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

## Running the server

From within the project directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
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

* [GET /concerts](#get-categories)
* [POST /concerts](#get-questions)
* [DELETE /concerts/int:concert_id](#delete-questionsintquestion_id)
* [PATCH /concerts/int:concert_id](#post-questions)
* [GET /players](#get-categories)
* [POST /players](#get-questions)
* [DELETE /players/int:player_id](#delete-questionsintquestion_id)
* [PATCH /players/int:player_id](#post-questions)

#### GET /categories

- General:
  - Returns: a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category 
- Sample: `curl http://127.0.0.1:5000/categories`
```
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}
"success": true
```
