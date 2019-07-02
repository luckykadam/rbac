from data_access_object import DataAccessObject
from authorization import Authorization
from user_interface import UserInterface


def main():
    print('initializing role based resource access system')

    dao = DataAccessObject()
    dao.load_data()

    authorization = Authorization(dao)

    ui = UserInterface(authorization)
    ui.start()


if __name__ == '__main__':
    main()
