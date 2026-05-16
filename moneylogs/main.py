# todo: oop 시작하기.
import sys
sys.path.append('/app/moneylogs')
import argparse
import storage
import datetime
import stats
import models
import service


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

money_log_service = service.MoneyLogService()

if args.command == "add":
    date = args.date
    category = args.category
    amount = args.amount
    memo = args.memo
    add_status = money_log_service.add_transaction(date, category, amount, memo)
    print(add_status)

elif args.command == "list":
    month = args.month
    category = args.category
    money_log_list = money_log_service.list_transaction(month, category)
    print(money_log_list)
    for item in money_log_list:
        print(item)

elif args.command == "stats":
    month = args.month
    monthly_stats = money_log_service.get_monthly_stats(month=month)

    print(f'{month} 지출 요약\n\n총 지출:{monthly_stats.total_amount}\n가장 많이 쓴 카테고리: {monthly_stats.top_category} {monthly_stats.top_category_amount}\n일평균 지출: {monthly_stats.daily_average}\n카테고리 별:\nfood: {monthly_stats.amount_by_category["food"]}\ncoffee: {monthly_stats.amount_by_category["coffee"]}\ntransport: {monthly_stats.amount_by_category["transport"]}\netc: {monthly_stats.amount_by_category["etc"]}')

elif args.command == "delete":
    id = args.id
    delete_status = money_log_service.delete_transaction(id)
    print(delete_status)

elif args.command == "export":
    export_format = args.format
    storage.export_transaction(export_format)




