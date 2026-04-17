from flask import Flask
from flask_restful import Api
from server.config import Config
from server.extensions import db, migrate, bcrypt, jwt
from server.resources import Signup, Login, Me, JournalList, JournalDetail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    api = Api(app)

    # AUTH ROUTES
    api.add_resource(Signup, "/signup")
    api.add_resource(Login, "/login")
    api.add_resource(Me, "/me")

    # CRUD ROUTES
    api.add_resource(JournalList, "/journal")
    api.add_resource(JournalDetail, "/journal/<int:id>")
    
    #BASIC ROUTES 
    @app.route("/")
    def home():
        return {"message": "Backend Productivity API is running"}, 200

    
     # ERROR HANDLERS 
    @app.errorhandler(404)
    def not_found(error):
        return {"message": "Route not found"}, 404

    @app.errorhandler(500)
    def server_error(error):
        return {"message": "Internal server error"}, 500

    return app
    
    
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)