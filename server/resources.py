from flask_restful import Resource ,request
from models import db, User, JournalEntry
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


 # AUTH
class Signup(Resource):
    def post(self):
        data = request.get_json()
        
        if not data:
            return {"message": "Missing JSON data"}, 400

        if User.query.filter_by(username=data["username"]).first():
            return {"message": "User already exists"}, 400

        user = User(username=data["username"])
        user.set_password(data["password"])

        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully"}, 201


class Login(Resource):
    def post(self):
        data = request.get_json()
        
        if not data:
            return {"message": "Missing JSON data"}, 400

        user = User.query.filter_by(username=data["username"]).first()

        if not user or not user.check_password(data["password"]):
            return {"message": "Invalid credentials"}, 401

        token = create_access_token(identity=user.id)
        return {"access_token": token}, 200


class Me(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        return {
            "id": user.id,
            "username": user.username
        }, 200


#  JOURNAL CRUD 
class JournalList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)


        entries = JournalEntry.query.filter_by(user_id=user_id)\
            .paginate( page=page, per_page=per_page)

        return {
            "items": [
                {"id": e.id, "title": e.title, "content": e.content}
                for e in entries.items
            ],
            "total": entries.total,
            "pages": entries.pages
        },200

    @jwt_required()
    def post(self):
        data = request.get_json()
        
        if not data:
            return {"message": "Missing JSON data"}, 400

        user_id = get_jwt_identity()

        entry = JournalEntry(
            title=data["title"],
            content=data["content"],
            user_id=user_id
        )

        db.session.add(entry)
        db.session.commit()

        return {"message": "Entry created"}, 201


class JournalDetail(Resource):
    @jwt_required()
    def patch(self, id):
        user_id = get_jwt_identity()

        entry = JournalEntry.query.filter_by(id=id, user_id=user_id).first()
        if not entry:
            return {"message": "Not found"}, 404

        data = request.get_json()
        
        if not data:
            return {"message": "Missing JSON data"}, 400
        
        entry.title = data["title"]
        entry.content = data["content"]

        db.session.commit()
        return {"message": "Updated"}, 200

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()

        entry = JournalEntry.query.filter_by(id=id, user_id=user_id).first()
        if not entry:
            return {"message": "Not found"}, 404

        db.session.delete(entry)
        db.session.commit()

        return {"message": "Deleted"}, 200