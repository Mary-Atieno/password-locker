#!/usr/bin/env python3.8
from user import User
from ast import While
from enum import auto
from json.tool import main

from user import User
from user import Credentials

def create_new_user(username, password):
    '''
     generates new user name
    '''
    new_user = User(username, password)
    return new_user

def add_user(user):
    '''
    saves new user
    '''
    user.add_user()

def display_user():
    '''
    returns all the saved users
    '''
    return User.display_user()


def authenticate_user(username, password):
    '''
    Function to check if user exists and log them in
    '''

    validate_user = Credentials.verify_user(username, password)
    return validate_user


def create_new_credential(account, user_name, password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account, user_name, password)
    return new_credential


def save_credentials(credentials):
    '''
    Function to add credentials to credential list
    '''
    credentials.save_details()


def display_accounts_details():
    '''
    Function returns all saved credentials
    '''
    return Credentials.show_credentials()


def delete_credentials(credentials):
    '''
    Function deletes credentials from credential list
    '''
    credentials.delete_credentials()


def find_credential(account):
    '''
    Function finds credential
    '''
    return Credentials.find_credential(account)


def credential_exists(account):
    '''
    Function that checks if credential exists
    '''
    return Credentials.existing_credentials(account)


def generate_Password():
    '''
    generate random password
    '''
    auto_password = Credentials.generateRandomPassword()
    return auto_password


def copy_password(account):
    '''
    Function that copies password using pyperclip
    '''
    return Credentials.copyPassword(account)


def main():
    print("Welcome to Password Locker...\n Choose one of the following to continue./n CN --- Create New Account \n AC --- Already Created Account /n")
    short_code = input('').lower().strip()
    if short_code == 'cn':
        print('Sign Up new User')
        print('*' * 20)
        username = input("User_name: ")
        while True:
            print('TYP - To type your own password:\n GEN - To generate random Password')
            password_option = input().lower().strip()
            if password_option == 'typ':
                password = input('Enter Password\n')
                break
            elif password_option == 'gen':
                password = generate_Password()
                break
            else:
                print("Incorrect password please try again")
        add_user(create_new_user(username, password))
        print('*' * 100)
        print(
            f'Hello {username}, Account created successfully! Your password is: {password}')
        print('*' * 100)

    elif short_code == 'ac':
        print('*' * 50)
        username = input('user_name:')
        password = input('Password:')
        login = authenticate_user(username, password)
        if authenticate_user == login:
            print(f'Hello {username}. Welcome to Password Locker')
            print('\n')

    while True:
        print("Use the following short codes:\n CNC - Create new credentials \n D - Display Credentials \n FND - Find a credential \n GEN - Generate a random password \n Del - Delete a credential \n EXT - Exit application \n")
        short_code = input().lower().strip()
        if short_code == "cnc":
            print('Create new credentials')
            print('.' * 20)
            print("Account name .....")
            account = input().lower()
            print('Account username')
            user_name = input()
            while True:
                print(
                    'TYP - To type your own password if account exists:\n GEN - To generate random Password')
                password_option = input().lower().strip()
                if password_option == 'typ':
                    password = input('Enter preferred password\n')
                    break
                elif password_option == 'gen':
                    password = generate_Password()
                    break
                else:
                    print("Incorrect password please try again")
            save_credentials(create_new_credential(
                account, user_name, password))
            print('\n')
            print(
                f'Account Credential for: {account} - userName: {user_name} - password: {password} created successfully')
            print('\n')
        elif short_code == 'd':
            if display_accounts_details():
                print("Saved Accounts")
                print('*' * 30)
                print('*' * 30)
                for account in display_accounts_details():
                    print(
                        f'Account:{account.account} \n User Name:{username} \n Password:{password}')
                    print('*' * 30)
                print('*' * 30)
            else:
             print('You have not yet saved any credentials.......')
        elif short_code == 'fnd':
            print('Input Account Name you want to find')
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f'Account Name: {search_credential.account}')
                print('-' * 50)
                print(
                    f'Username: {search_credential.user_name} password: {search_credential.password}')
                print('-' * 50)
            else:
                print('Credential does not exist')
                print('\n')

        elif short_code == 'del':
            print('Input account name of the credential you wish to delete')
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print('_' * 50)
                search_credential.delete_credentials()
                print('\n')
                print(
                    f'Saved credentials for: {search_credential.account} successfully deleted')
                print('\n')
            else:
                print('Credential does not exist')

        elif short_code == 'gen':

            password = generate_Password()
            print(
                f'{password} has been generated successfully. Proceed to use it in your account')

        elif short_code == 'ext':
            print('Have a nice Day')
            break
        else:
            print('Invalid code... Please try again')


if __name__ == '_main_':
    
    main()