from app.main import db


class EmailAddress(db.Model):
    """ EmailAddress Model for storing email_address related details """
    __tablename__ = "email_address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))

    def __repr__(self):
        return f"<Email Address: '{self.email}'>"
