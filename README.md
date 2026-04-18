# Backend-Productivity-App

## Project Title

```bash
Backend-Productivity-App
```

## Project Description
This project is a secure RESTful API built using Flask that allows users to manage a personal productivity resource (such as notes, journal entries, or tasks).

Each user can:
- Register and securely log in
- Create, read, update, and delete their own resources
- Access only their own data (fully protected routes)
- Work with paginated data responses

Authentication is handled using **JWT (JSON Web Tokens)** and passwords are securely hashed using **Flask-Bcrypt**.



##  Tech Stack / Tools

### Python Version
- Python 3.8+

### Core Technologies
- Flask 2.2.2
- Flask-SQLAlchemy 3.0.3
- Flask-Migrate 4.0.0
- Flask-RESTful 0.3.9
- Flask-Bcrypt 1.0.1
- Flask-JWT-Extended
- Marshmallow 3.20.1

### Development Tools
- Faker (test data generation)
- Pytest (testing)
- Pipenv (dependency management)

---

## Installation Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Novar-Knight/Backend-Productivity-App.git
cd Backend-Productivity-App
````

### 2. Install dependencies

```bash
pipenv install
```

### 3. Activate virtual environment

```bash
pipenv shell
```

### 4. Set environment variables (optional)

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

---

## Database Setup

### Initialize migrations

```bash
flask db init
```

### Create migration

```bash
flask db migrate -m "initial migration"
```

### Apply migration

```bash
flask db upgrade
```

---

##  Seeding the Database

To populate the database with sample data:

```bash
python seed.py
```

---

## Running the Application

```bash
flask run
```

The API will be available at:

```
http://127.0.0.1:5000/
```

---

##  Authentication Flow

### Signup

* Creates a new user
* Password is hashed using Bcrypt

### Login

* Returns a JWT token

### Protected Routes

* All resource routes require a valid token:

```http
Authorization: Bearer <token>
```

---

###  API Endpoints


###  Auth Routes


#### Register User

```http
POST /signup
```

#### Login User

```http
POST /login
```

#### Get Current User

```http
GET /me
```

---

###  Resource Routes (Notes / Tasks / Journal)

#### Get All Items (Paginated)

```http
GET /resources?page=1
```

#### Create Item

```http
POST /resources
```

#### Get Single Item

```http
GET /resources/<id>
```

#### Update Item

```http
PATCH /resources/<id>
```

#### Delete Item

```http
DELETE /resources/<id>
```

---

##  Security Features

* Password hashing using Flask-Bcrypt
* JWT authentication for secure sessions
* Route protection (users can only access their own data)
* Unauthorized requests return proper HTTP error codes (401/403)

---

##  Testing

Run tests using:

```bash
pytest
```

---

##  Project Structure (Recommended)

```
├── app.py
├── models.py
├── seed.py
├── config.py
├── routes/
├── migrations/
├── resources/
├── auth/
└── tests/
```

---

##  Future Improvements

* Role-based access control (Admin/User)
* Refresh tokens
* Rate limiting
* Frontend integration (React/Vue)

---

##  Author

Developed as part of a Backend-Productivity-App assignment focusing on authentication, authorization, and secure REST API design.

```





