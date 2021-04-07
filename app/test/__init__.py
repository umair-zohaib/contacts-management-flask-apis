from flask_testing import TestCase

from app.main import db
from manage import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        config_obj = 'app.main.config.TestingConfig'
        app.config.from_object(config_obj)
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
