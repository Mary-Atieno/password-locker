import random
import string

import pyperclip


class User:
    '''
    user class generate new users
    '''
    user_list = []

    def __init__(self, username ,password ):
        '''
        create method for defining user properties
        '''
        self.username = username
        self.password = password
       
    def add_user(self):
        '''
        adds users to a new list
        '''
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        deletes users from the list
        '''
        User.user_list.remove(self)


class Credentials():
    '''
    class to create new objects of credentials
    '''
    credentials_list = []
    @classmethod
    def verify_user(cls, username, password):
        '''
        method to verify if a user is already in the list
        '''
        check_user = ""
        for user in User.user_list:
            if (user.username == username and user.password == password):
                check_user = user.username
            return check_user

    def __init__(self, account, user_name, password):
        '''
        method defining the user credentials to be stored 
        '''
        self.account = account
        self.user_name = user_name
        self.password = password

    
    def save_details(self):
        '''
        method for saving new credentials to the credentials store
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        Method that deletes the credentials from the credentials store
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account):
        '''
        method that checks the credentials for validity
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def existing_credentials(cls, account):
        '''
        method that checks if the credentials exists for the account
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
            return False

    @classmethod
    def show_credentials(cls):
        '''
        method to show all the credentials
        '''
        return cls.credentials_list
    def generateRandomPassword(stringLength=10):
        '''
        generate random password string of letters and special characters
        '''
        password = string.ascii_uppercase + \
            string.ascii_lowercase + string.digits + "~#!@%&*"
        return ''.join(random.choice(password) for i in range(stringLength))


    