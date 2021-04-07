import json
import unittest

from app.test import BaseTestCase


data_dict = dict(username="test123",
                 firstname="mary",
                 lastname="john",
                 email_address=[
                     'testemail_1@gmail.com', 'testemail_2@gmail.com'
                 ])


def create_contact(self, data=None):
    dumped_data = data or json.dumps(data_dict)
    return self.client.post(
        '/contact/',
        data=dumped_data,
        content_type='application/json'
    )


def get_contact(self, username):
    return self.client.get(
        f'/contact/{username}'
    )


def delete_contact(self, username=None):
    return self.client.delete(
        f'/contact/{username}'
    )


def update_contact(self, data, username=None):
    dumped_data = json.dumps(data)
    return self.client.put(
        f'/contact/{username}',
        data=dumped_data,
        content_type='application/json'
    )


class TestContactBlueprint(BaseTestCase):

    def test_create_new_contact(self):
        """ Test for creation of new contact """
        with self.client:
            # create a new contact
            contact_response = create_contact(self)
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 201)
            self.assertEqual(response_data['status'], 'success')
            self.assertEqual(response_data['message'], 'Successfully created contact')

            # create contact with same username
            contact_response = create_contact(self)
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 409)
            self.assertEqual(response_data['status'], 'fail')
            self.assertEqual(response_data['message'], 'Contact already exists')

    def test_get_contact(self):
        """ Test for get a contact """
        with self.client:
            # create a new contact
            contact_response = create_contact(self)
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 201)
            self.assertEqual(response_data['status'], 'success')
            self.assertEqual(response_data['message'], 'Successfully created contact')

            # get a contact with username we have created
            contact_response = get_contact(self, username=data_dict["username"])
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 200)
            self.assertEqual(response_data['username'], data_dict['username'])
            self.assertEqual(response_data['firstname'], data_dict['firstname'])
            self.assertEqual(response_data['lastname'], data_dict['lastname'])
            self.assertEqual(response_data['email_address'], data_dict['email_address'])

            # get a contact doesn't exist
            contact_response = get_contact(self, username='contact_doesnt_exist')
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 404)
            self.assertIn('URL was not found on the server', response_data['message'])

    def test_delete_contact(self):
        """ Test for delete a contact """
        with self.client:
            # create a new contact
            contact_response = create_contact(self)
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 201)
            self.assertEqual(response_data['status'], 'success')
            self.assertEqual(response_data['message'], 'Successfully created contact')

            # delete a contact
            contact_response = delete_contact(self, username=data_dict["username"])
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 202)
            self.assertEqual(response_data['status'], 'success')
            self.assertEqual(response_data['message'], 'Successfully deleted contact')

            # delete a contact which doesn't exist
            contact_response = delete_contact(self, username='contact_doesnt_exist')
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 404)
            self.assertEqual(response_data['status'], 'fail')
            self.assertEqual(response_data['message'], 'Contact not found')

    def test_update_contact(self):
        """ Test for delete a contact """
        with self.client:
            # create a new contact
            contact_response = create_contact(self)
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 201)
            self.assertEqual(response_data['status'], 'success')
            self.assertEqual(response_data['message'], 'Successfully created contact')

            # update a contact
            data = dict(
                firstname='mary_updated',
                lastname='john_updated',
                email_address=[
                    'testemail_updated@gmail.com'
                ]
            )
            contact_response = update_contact(self, data=data, username=data_dict["username"])
            response_data = json.loads(contact_response.data)

            self.assertEqual(contact_response.status_code, 200)
            self.assertEqual(response_data['username'], data_dict['username'])

            self.assertEqual(response_data['firstname'], data['firstname'])
            self.assertEqual(response_data['lastname'], data['lastname'])
            self.assertEqual(response_data['email_address'], data['email_address'])


if __name__ == '__main__':
    unittest.main()
