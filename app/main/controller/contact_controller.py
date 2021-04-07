from flask import request
from flask_restx import Resource

from app.main.util.dto import ContactDto
from app.main.service.contact_service import get_contact, get_all_contact, delete_contact, update_contact, \
    create_contact

api = ContactDto.api
_contact = ContactDto.contact
_update_contact = ContactDto.update_contact


@api.route('/<username>')
@api.param('username', 'Username of the contact')
class Contact(Resource):
    @api.doc('get a user')
    @api.response(404, 'Contact not found')
    @api.marshal_with(_contact)
    def get(self, username):
        """ Get a contact for the given username """
        contact = get_contact(username)

        if contact:
            return contact
        else:
            api.abort(404)

    @api.doc('delete a contact')
    @api.response(404, 'Contact not found')
    def delete(self, username):
        """ Delete a contact for the given username """
        return delete_contact(username)

    @api.doc('update a contact')
    @api.expect(_update_contact)
    @api.marshal_with(_contact)
    def put(self, username):
        """ Update a contact for the given username """
        data = request.json
        if data:
            return update_contact(username, data)
        else:
            return api.abort(409)


@api.route('/')
class ContactList(Resource):
    @api.doc('create a new contact')
    @api.response(201, 'Contact successfully created')
    @api.expect(_contact, validate=True)
    def post(self):
        """ Creates a new Contact """
        data = request.json
        return create_contact(data=data)

    @api.doc('list_of_all_contacts')
    @api.marshal_list_with(_contact, envelope='data')
    def get(self):
        """ List all contacts """
        return get_all_contact()
