
import argparse
import sys

from your_app import cli_binding


"""
Usage:

    yourapp directory list
    yourapp directory get <account-id>
    
    yourapp service credit <account-id> <amount>
    yourapp service debit <account-id> <amount>

"""


def main():

    # Base
    parser = argparse.ArgumentParser(prog='your-app', description='Your app')
    subparsers = parser.add_subparsers(help='SUB-COMMANDS')

    # Directory
    directory_parser = subparsers.add_parser('directory', help='Account directory operations')
    directory_subparsers = directory_parser.add_subparsers(help='SUB-COMMANDS')

    # Directory list
    directory_list_cmd = directory_subparsers.add_parser('list', help='List accounts')
    directory_list_cmd.set_defaults(func=cli_binding.directory_list)

    # Directory get
    directory_list_cmd = directory_subparsers.add_parser('get', help='Get account')
    directory_list_cmd.set_defaults(func=cli_binding.directory_get)
    directory_list_cmd.add_argument('account_id')

    # Service
    service_parser = subparsers.add_parser('service', help='Account services')
    service_subparsers = service_parser.add_subparsers(help='SUB-COMMANDS')

    # Service credit
    service_credit_cmd = service_subparsers.add_parser('credit', help='Credit account')
    service_credit_cmd.set_defaults(func=cli_binding.account_credit)
    service_credit_cmd.add_argument('account_id')
    service_credit_cmd.add_argument('amount', type=float)

    # Service debit
    service_debit_cmd = service_subparsers.add_parser('credit', help='Credit account')
    service_debit_cmd.set_defaults(func=cli_binding.account_debit)
    service_debit_cmd.add_argument('account_id')
    service_debit_cmd.add_argument('amount', type=float)

    has_args = len(sys.argv) > 1
    if has_args:

        args = parser.parse_args()

        if 'func' in args:
            args.func(args)
        else:
            print('Invalid option; use -h for help')

    else:
        parser.print_help()


if __name__ == "__main__":
    # For direct access using: python -m reta.cli
    main()
