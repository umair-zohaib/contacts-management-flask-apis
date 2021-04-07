from flask_restx import Namespace, fields


class ContactDto:
    api = Namespace('contact', description='contact related apis')
    contact = api.model('contact', {
        'username': fields.String(required=True, description='contact username'),
        'firstname': fields.String(required=True, description='contact firstname'),
        'lastname': fields.String(required=True, description='contact lastname'),

        'email_address': fields.List(
            fields.String(attribute='email', required=True),
            required=True,
            description='array of email addresses for a contact',
            attribute='email_addresses'
        )
    })

    update_contact = api.model('uddated contact', {
        'firstname': fields.String(description='contact firstname'),
        'lastname': fields.String(description='contact lastname'),

        'email_address': fields.List(
            fields.String(attribute='email'),
            description='array of email addresses for a contact',
            attribute='email_addresses'
        )
    })
