from app.main import db


class Contact(db.Model):
    """ Contact Model for storing contact related details """
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email_addresses = db.relationship("EmailAddress", backref="contact", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"<Contact: '{self.username}'>"
