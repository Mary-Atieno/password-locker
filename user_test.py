from cgi import test
import unittest
from user import Credentials
from user import User
import pyperclip

class TestClass(unittest.TestCase):
    '''
    Test class
    '''
    def setUp(self):
        '''
        sets up application
        '''
        self.new_user = User('BillHaris','08642')
        
    def test_init(self):
        '''
        checks for initialization 
        '''
        self.assertEqual(self.new_user.username, 'BillHaris')
        self.assertEqual(self.new_user.password, '08642')
    
    def test_add_user(self):
        '''
        adds users
        '''
        self.new_user.add_user()
        self.assertEqual(len(User.user_list),1)
 

class TestCredentials(unittest.TestCase):
    '''
    defines test cases for credentials
    '''

    def setUp(self):
        '''
        runs each test cases
        '''
        self.new_credential = Credentials('Space', 'BillHaris', '08642')
    def test_init(self):
        '''
        test if the object is initialized 
        '''
        self.assertEqual(self.new_credential.account, 'Space')
        self.assertEqual(self.new_credential.user_name, 'BillHaris')
        self.assertEqual(self.new_credential.password, '08642')

    def save_credential_test(self):
        '''
        test if the contact object is saved into
         the contact list
        '''
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
        does not clean up after each test case has been run.
        '''
        Credentials.credentials_list = []

    
    def test_save_multiple_credentials(self):
        '''
        saves multiple contact to  contact_list
        '''
        self.new_credential.save_details()
        test_credential = Credentials('Test', 'TestUser', '08642')
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 2)

    
    def test_delete_credentials(self):
        '''
        test if we can delete a contact
        from our credential list
        '''

        self.new_credential.save_details()
        test_credential = Credentials('Test', 'TestUser', '08642')
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    
    def show_credential(self):
        '''
        checks if we can find a credential by account name
        and information
        '''

        self.new_credential.save_details()
        test_credential = Credentials('Test', 'TestUser', '08642')
        test_credential.save_details()

        found_credential = Credentials.show_credential('Test')

        self.assertEqual(found_credential.account, test_credential.account)

    def test_credential_exists(self):
        '''
        checks if we can return a Boolean if we cannot find the credential.
        '''
        self.new_credential.save_details()
        test_credential = Credentials('Test', 'TestUser', '08642')
        test_credential.save_details()

        credential_exists = Credentials.existing_credentials('Test')

        self.assertFalse(credential_exists)

    def test_display_all_credentials(self):
        '''
        returns a list of saved credentials 
        '''

        self.assertEqual(Credentials.show_credentials(), Credentials.credentials_list)


if __name__=='_main_':
     unittest.main()