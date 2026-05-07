# todo: oop 시작하기.
import sys
sys.path.append('/app/moneylogs')
import argparse
import storage
import datetime
import stats
import models


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", help="choose the command")

add_parser = subparsers.add_parser("add", help="add list")
add_parser.add_argument("--date", type= str, default= datetime.datetime.now, help="YYYY-MM-DD")
add_parser.add_argument("--category", type= str, default= "etc", choices=["food","coffee","transport","etc"])
add_parser.add_argument("--amount", type= int, default= 0)
add_parser.add_argument("--memo", type= str, default="")

list_parser = subparsers.add_parser("list", help="ask list")
list_parser.add_argument("--month", type= str)
list_parser.add_argument("--category", type= str, choices=["food","coffee","transport","etc"])

stats_parser = subparsers.add_parser("stats", help="show stats")
stats_parser.add_argument("--month", type= str)

delete_parser = subparsers.add_parser("delete", help="delete data")
delete_parser.add_argument("--id", type= int)

export_parser = subparsers.add_parser("export", help="export data")
export_parser.add_argument("--format", type= str)


args = parser.parse_args()

if args.command == "add":
    date = args.date
    category = args.category
    amount = args.amount
    memo = args.memo
    storage.add_transaction(date, category, amount, memo)

elif args.command == "list":
    month = args.month
    category = args.category
    storage.list_transaction(month, category)

elif args.command == "stats":
    month = args.month
    stats.stats_transaction(month)

elif args.command == "delete":
    id = args.id
    storage.delete_transaction(id)

elif args.command == "export":
    export_format = args.format
    storage.export_transaction(export_format)




