from app import app
from models import Message, User
import unittest
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class MessageModelAttributes(unittest.TestCase):
    def create_app(self):
        app.config[
            "SQLALCHEMY_DATABASE_URI"] = 'postgres://localhost/warbler_db_test'
        return app

    def setUp(self):
        db.create_all()
        # user1 = User(
        #     email="itsfriday@hotmail.com", username="tgif", password="123fish")
        # user2 = User(
        #     email="kristenrules@hotmail.com",
        #     username="bayarearules",
        #     password="456easypeezy")
        # user3 = User(
        #     email="kelley@hotmail.com",
        #     username="tetonchick",
        #     password="474646574584ok")
        # db.session.add_all([user1, user2, user3])
        # db.session.commit()
        # user1 = User.query.filter_by(username="tgif")
        # user2 = User.query.filter_by(username="bayarearules")
        message1 = Message(text="Hello Friday")
        # message1.liked_by = user1
        message2 = Message(text="Harry Potter is awesome")
        # message2.user_id = user2
        message3 = Message(text="So is Star Wars")
        db.session.add_all([message1, message2, message3])
        db.session.commit()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    def test_create_message(self):
        """check thar a message was made"""
        found_message = Message.query.filter_by(text="Hello Friday")
        self.assertIsNotNone(found_message)

    def like_message(self):
        found_message = Message.query.filter_by(text="Hello Friday")
        found_message.liked_by = 1
        self.assertIsNone(found_message.liked_by)

    def test_liked_by(self):
        """test if a message can be liked"""
        found_message = Message.query.filter_by(text="Hello Friday")
        user1 = User.query.filter_by(username="tgif")
        self.assertIn(user1, found_message.liked_by)

    def test_message_author(self):
        """check that message has associated user id for its author"""
        found_message = Message.query.filter_by(text="Hello Friday")
        user2 = User.query.filter_by(username="bayarearules")
        self.assertIn(user2, found_message.user_id)


if __name__ == '__main__':
    unittest.main()
