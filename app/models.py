

from flask import Flask
from hashlib import sha256
from typing import Iterable
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)  # sha256

    def __repr__(self):
        return f"<{self.__class__.__name__} #{self.id}> login={self.login}"

    @classmethod
    def authenticate(cls, auth):
        password = sha256(auth.password.encode()).hexdigest()
        return cls.query.filter(cls.login == auth.username).filter(cls.password_hash == password).first()


class File(db.Model):
    __tablename__ = "files"
    name = db.Column(db.String(64), primary_key=True)  # sha256-filename
    # size = db.Column(db.Integer)
    owner = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @classmethod
    def add_files(cls, filenames: Iterable[str], owner: int):
        user_id = owner.id if isinstance(owner, User) else owner
        for filename in filenames:
            db.session.add(cls(name=filename, owner=user_id))
        db.session.commit()

    @classmethod
    def get(cls, file_hash: str):
        return cls.query.get(file_hash)

    @classmethod
    def delete(cls, file_hash: str):
        cls.query.filter(cls.name == file_hash).delete()
        db.session.commit()


def configure_database(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return db
