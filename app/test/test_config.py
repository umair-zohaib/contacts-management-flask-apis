import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir


class TestProductionConfig(TestCase):
    def create_app(self):
        config_obj = 'app.main.config.ProductionConfig'
        app.config.from_object(config_obj)
        return app

    def test_app_is_production(self):
        self.assertIsNotNone(current_app)
        self.assertFalse(app.config['DEBUG'])
        self.assertIsNot(app.config['SECRET_KEY'], 'i_am_secret_key')
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'prod.db')
        )


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        config_obj = 'app.main.config.DevelopmentConfig'
        app.config.from_object(config_obj)
        return app

    def test_app_is_development(self):
        self.assertIsNotNone(current_app)
        self.assertTrue(app.config['DEBUG'])
        self.assertIsNot(app.config['SECRET_KEY'], 'i_am_secret_key')
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'dev.db')
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        config_obj = 'app.main.config.TestingConfig'
        app.config.from_object(config_obj)
        return app

    def test_app_is_testing(self):
        self.assertIsNotNone(current_app)
        self.assertTrue(app.config['DEBUG'])
        self.assertIsNot(app.config['SECRET_KEY'], 'i_am_secret_key')
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'test.db')
        )


if __name__ == '__main__':
    unittest.main()
