# -*- coding: utf-8 -*-
import datetime as dt

from flask.ext.login import UserMixin

from {{cookiecutter.app_name}}.extensions import bcrypt, db


class User(UserMixin, db.Document):

    username = db.StringField(max_length=80, unique=True, required=True)
    email = db.StringField(max_length=80, unique=True, required=True)
    #: The hashed password
    password = db.StringField(max_length=128, required=True)
    created_at = db.DateTimeField(required=True)
    first_name = db.StringField(max_length=30)
    last_name = db.StringField(max_length=30)
    active = db.BooleanField(default=False)
    is_admin = db.BooleanField(default=False)

    @classmethod
    def create(cls, username, email, password, **kwargs):
        now = dt.datetime.now()
        user = cls(username=username, email=email, created_at=now, **kwargs)
        user.set_password(password)
        user.save()
        return user

    @classmethod
    def get_by_id(cls, id):
        user = cls.objects.with_id(id)
        if user:
            return user
        else:
            return None

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __repr__(self):
        return '<User({username!r})>'.format(username=self.username)
