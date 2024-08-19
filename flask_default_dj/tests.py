from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import unittest


class BasicTests(unittest.TestCase):

    def create_app(self):
        self.app: Flask = None
        self.db: SQLAlchemy = None

    def setUp(self) -> None:
        self.app = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db.create_all()

    def tearDown(self) -> None:
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()