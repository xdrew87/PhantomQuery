import argparse
from modules.phone_lookup import lookup_number
from modules.inmate_lookup import lookup_inmate

parser = argparse.ArgumentParser(description="JailbirdX OSINT Tool")
parser.add_argument('--phone', help='Phone number to look up')
parser.add_argument('--name', help='Inmate name to search')
parser.add_argument('--state', help='State for inmate lookup')

args = parser.parse_args()

if args.phone:
    result = lookup_number(args.phone)
    print("Phone Lookup Result:")
    print(result)

if args.name and args.state:
    result = lookup_inmate(args.name, args.state)
    print("Inmate Lookup Result:")
    print(result)
