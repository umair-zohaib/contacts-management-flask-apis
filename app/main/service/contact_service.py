from app.main import db
from app.main.model.contact import Contact
from app.main.model.email_address import EmailAddress
from sqlalchemy.exc import IntegrityError


def get_all_contact():
    """ Return all the contacts """
    return Contact.query.all()


def get_contact(username):
    """ Return a contact with the username """
    return Contact.query.filter_by(username=username).first()


def delete_contact(username):
    """ Return a contact with the username """
    contact = get_contact(username)
    if contact:
        db.session.delete(contact)
        db.session.commit()

        response = {
            'status': 'success',
            'message': 'Successfully deleted contact'
        }
        status_code = 202
    else:
        response = {
            'status': 'fail',
            'message': 'Contact not found'
        }
        status_code = 404
    return response, status_code


def update_contact(username, data):
    """ Update existing contact """
    contact = get_contact(username)
    if contact:
        if data.get('firstname'):
            contact.firstname = data['firstname']

        if data.get('lastname'):
            contact.lastname = data['lastname']

        if data.get('email_address'):
            contact.email_addresses = []
            add_email_address(contact, data)

            try:
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                response = {
                    'status': 'fail',
                    'message': f'Email address: {e.params[0]} already associated with some contact'
                }
                status_code = 409
                return response, status_code

        elif 'email_address' in data:
            contact.email_addresses = []

        return contact
    else:
        response = {
            'status': 'fail',
            'message': 'Contact not found'
        }
        status_code = 404
        return response, status_code


def create_contact(data):
    """ Create a new contact """
    contact = get_contact(data['username'])
    if not contact:
        new_contact = Contact(
            username=data['username'],
            firstname=data['firstname'],
            lastname=data['lastname']
        )
        db.session.add(new_contact)
        add_email_address(new_contact, data)
        try:
            db.session.commit()
            response = {
                'status': 'success',
                'message': 'Successfully created contact'
            }
            status_code = 201
        except IntegrityError as e:
            db.session.rollback()
            response = {
                'status': 'fail',
                'message': f'Email address: {e.params[0]} already associated with some contact'
            }
            status_code = 409
    else:
        response = {
            'status': 'fail',
            'message': 'Contact already exists'
        }
        status_code = 409

    return response, status_code


def add_email_address(contact, data):
    for email_address in data['email_address']:
        new_email_address = EmailAddress(email=email_address)
        contact.email_addresses.append(new_email_address)
