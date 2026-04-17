from app import app
from extensions import db
from models import User, JournalEntry

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username="john")
    user1.set_password("password")

    user2 = User(username="mary")
    user2.set_password("password")

    db.session.add_all([user1, user2])
    db.session.commit()

    entry1 = JournalEntry(title="Day 1", content="Hello world", user_id=user1.id)
    entry2 = JournalEntry(title="Day 2", content="Learning Flask", user_id=user1.id)

    db.session.add_all([entry1, entry2])
    db.session.commit()

    print("Database seeded!")