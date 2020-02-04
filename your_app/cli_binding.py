
from your_app_webapi_client.BankDirectory import BankDirectory


def directory_list(command):

    directory = BankDirectory('http://localhost:5000')

    account_list = directory.read_list()

    for account in account_list:
        print(account.__dict__)


def directory_get(command):

    directory = BankDirectory('http://localhost:5000')

    account = directory.read(command.account_id)

    print(account.__dict__)


def account_credit(command):
    raise NotImplementedError


def account_debit(command):
    raise NotImplementedError
