# StackOverflow-lite
Is a platform where people can ask questions and provide answers.

## Overview
StackOverflow-lite is a platform where people can ask questions and provide answers.

## StackOverflow-lite Required Features
    - Users can create an account and log in.
    - Users can post questions.
    - Users can delete the questions they post
    - Users can post answers
    - Users can view the answers
    - Users can accept an answer out of all the answers to his/her queston as they preferred answer

## Optional Features
    - Users can upvote or downvote an answer.
    - Users can comment on an answer.
    - Users can fetch all questions he/she has ever asked on the platform
    - Users can search for questions on the platform
    - Users can view questions with the most answers.


#  Sample Tasks
 
 >  **[Pivot Tracker Board](https://www.pivotaltracker.com/n/projects/2234206)**

## StackOverflow-lite Installation Steps
```
    $ git clone https://github.com/blairt001/StackOverflow-lite.git
    $ cd StackOverflow-lite
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt  
```
 

## Run the Application
```
    $ export DATABASE_URL="Copy Your DATABASE_URL here"
``` 
    Another option is to create and open the .env, then paste your postgres url
```
    #.env file
    DATABASE_URL=postgres://username:password@localhost/database_name i.e
    DATABASE_URL=postgres://blairt001:1234@localhost/stacklite_db
    
    $ python run.py runserver
```
## Testing the Application
``` 
    $ pytest --cov=app

```
## Run Individual Tests
``` 
    pytest/tests/test_name.py 
```
### List of API Endpoints

#### Users API Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/auth/signup` | Registers a new user
GET | `/api/v1/auth/users` | Returns a list of all registered users
GET | `/api/v1/auth/users/{user_id}` | Returns a user with the specific user_id
POST | `/api/v1/auth/login` | Login a user

#### Questions API Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions` | Add a question to the database
GET | `/api/v1/questions` | Lists all questions in the database
GET | `/api/v1/questions/{question_id}` | Retrieve a question with the given id
PUT | `/api/v1/questions/{question_id}` | Edit a question by logged in user
DELETE | `/api/v1/questions/{question_id}` | Delete a specific question

#### Answers API Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions/{question_id}/answers` | Add an answer to a question
GET | `/api/v1/questions/answers` | Lists all answersin the database
GET | `/api/v1/questions/answers/{answerID}` | Retrieve an answer with the id
PUT | `/api/v1/questions/{question_id}/answer/{answerID}` | Edit answer
DELETE | `/api/v1/questions/{question_id}/answer/{answerID}` | Delete answer
POST | `/api/v1/questions/answers/vote/{answer_id}` | Upvote/DownVote an answer
POST | `/api/v1/questions/answers/comment/{answer_id}` | Comment on an answer


### License
[MIT LICENSE](https://github.com/blairt001/StackOverflow-lite/blob/master/LICENSE)

## Extras
Andela Cycle-36 Pre-bootcamp Challenge Preparation.

## Developer
Tony Blair