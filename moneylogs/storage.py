import os.path
import json
import commands
from datetime import datetime
from jsonschema import validate, exceptions
from models import amount_schema
import csv
import models


file_path = "/app/data/transactions.json"
export_file_path = "/app/data/transaction_export.csv"

class TransactionRepository:
    

    def __init__(self):
        self.transaction = models.Transaction()

    def load(self):
      try:
        with open(file_path, "r", encoding='utf-8') as f:
          datas_list = json.load(f)
        
        dict_data_list= list(map(self.transaction.from_dict, datas_list))
        
        return dict_data_list
      except ValueError:
        commands.error()
        with open(file_path, "w") as f:
                f.write("[]")
        return []

    
    def save(self, transactions: list[models.Transaction]):
      try:
        if os.path.isfile(file_path):
          save_data_list = map(self.transaction.to_dict, transactions)
          with open(file_path, "w") as f:
              json.dump(save_data_list, f)
          return print("save succeed.")
        else:
          json_data = json.dumps(transactions)
          with open(file_path, "w") as f:
                  f.write(json_data)
        
      except ValueError:
        commands.error()
    
    def next_id(id: int):
      return id + 1
    
    def add(self, transaction: models.Transaction):
      # id = transaction.id
      category = transaction.category
      date = transaction.date
      amount = transaction.amount
      memo = transaction.memo
      if category != "coffee" and category != "food" and category != "transport" and category != "etc":
          return print("카테고리는 coffee or food or transport or etc 중에 골라주세요.")
          
      datas_list = []
      
      insert_data = models.Transaction(
          date=date,
          category=category,
          amount=amount,
          memo=memo
      ).to_dict()


      if os.path.isfile(file_path):
        datas_list = self.load()
      else:
        insert_data =[{'id': 0, **insert_data}]
        return self.save(transactions=insert_data)
      
      if len(datas_list) > 0:
          data_id = self.next_id(id=datas_list[len(datas_list)-1])

          transactions = [*datas_list,{
              "id": data_id,
              **insert_data
          }]
          save_transactions(transactions=transactions)
      else:
          transactions =[{'id': 0, **insert_data}]
          save_transactions(transactions=transactions)


def check_data(data):
    try:
        if validate(schema= amount_schema, instance= data) is None:
            return data
        else:
            commands.error()
    except exceptions.ValidationError as e:
        print("Valid is not data")
        print(e)


def load_transactions():
    # if os.path.isfile(file_path) is False:
    try:
        with open(file_path, "r", encoding='utf-8') as f:
                datas_list = json.load(f)

        
        if isinstance(datas_list, list):
            check_datas = map(check_data, datas_list)
            check_datas_list = list(check_datas)
            filetered_list = []

            for i in check_datas_list:
                if i != None:
                    filetered_list = [*filetered_list, i]

            return filetered_list
        elif isinstance(datas_list, dict):
            check_one_data = check_data(datas_list)
            check_one_data_list= [check_one_data]

            filetered_list = []

            for i in check_one_data_list:
                if i != None:
                    filetered_list = [*filetered_list, i]
            
            return filetered_list

        else:
            commands.error()
    except ValueError:
            with open(file_path, "w") as f:
                f.write("[]")
            return []

def save_transactions(transactions: list):
    with open(file_path, "w") as f:
            json.dump(transactions, f)
    return print("save succeed.")


def add_transaction(date:datetime, category:str, amount:int, memo:str):
    if commands.validate_date(date) == False:
        return
    if type(amount) is not int:
        return
    if category != "coffee" and category != "food" and category != "transport" and category != "etc":
        return print("카테고리는 coffee or food or transport or etc 중에 골라주세요.")
        
    datas_list = []

    insert_data = {
        'date': date,
        'category': category,
        'amount': amount,
        'memo': memo
    }

    

    if os.path.isfile(file_path):
            datas_list = load_transactions()
    else:
        insert_data ={'id': 0, **insert_data}
        json_data = json.dumps(insert_data)
        with open(file_path, "w") as f:
                f.write(json_data)
    
    
    

    if len(datas_list) > 0:
        data_id = datas_list[len(datas_list)-1]['id'] + 1

        transactions = [*datas_list,{
            "id": data_id,
            **insert_data
        }]
        save_transactions(transactions=transactions)
    else:
        transactions =[{'id': 0, **insert_data}]
        save_transactions(transactions=transactions)

def list_transaction(month: str, category: str):
    if os.path.isfile(file_path) is False:
        return print("데이터가 없습니다. 먼저 데이터를 추가해주세요.")
    datas_list = load_transactions()
        
    
    if month: 
        splitMonth = month.split("-")
        correctYear = splitMonth[0]
        correctMonth = splitMonth[1]
        # filteredList = []
        if type(datas_list) is object:
            data = datas_list["date"].split("-")
            data_year = data[0]
            data_month = data[1]
            if correctYear == data_year and correctMonth == data_month:
                return print(f'아이디: {datas_list["id"]}\n날짜: {datas_list["date"]}\n카테고리: {datas_list["category"]}\n금액: {datas_list["amount"]}\n메모: {datas_list["memo"]}')
        for item in datas_list:
            # print(item["date"])
            itemSplitArr = item["date"].split("-")
            itemYear = itemSplitArr[0]
            itemMonth = itemSplitArr[1]
            if itemYear == correctYear and itemMonth == correctMonth:
                # filteredList = [*filteredList, item]
                print(f'아이디: {item["id"]}\n날짜: {item["date"]}\n카테고리: {item["category"]}\n금액: {item["amount"]}\n메모: {item["memo"]}')
    elif category:
        if type(datas_list) is object:
            if datas_list["category"]:
                return print(f'아이디: {datas_list["id"]}\n날짜: {datas_list["date"]}\n카테고리: {datas_list["category"]}\n금액: {datas_list["amount"]}\n메모: {datas_list["memo"]}')
            
        for item in datas_list:
            if item["category"] == category:
                print(f'아이디: {item["id"]}\n날짜: {item["date"]}\n카테고리: {item["category"]}\n금액: {item["amount"]}\n메모: {item["memo"]}')
                
    else:
        if type(datas_list) is object:
            return print(f'아이디: {datas_list["id"]}\n날짜: {datas_list["date"]}\n카테고리: {datas_list["category"]}\n금액: {datas_list["amount"]}\n메모: {datas_list["memo"]}')
        for item in datas_list:
            print(f'아이디: {item["id"]}\n날짜: {item["date"]}\n카테고리: {item["category"]}\n금액: {item["amount"]}\n메모: {item["memo"]}')


def delete_transaction(id: int):
    if id == 0 or id:
        
        if os.path.isfile(file_path) is False:
            return print("데이터가 없습니다. 먼저 데이터를 추가해주세요.")
        datas_list= load_transactions()

        transactions = []
        
        
        for item in datas_list:
            if item['id'] != id:
                transactions = [*transactions, item]
                
        
        if len(transactions) == len(datas_list):
            return print("해당 아이디가 없습니다. 다시 확인 후 입력해주세요.")

        save_transactions(transactions=transactions)
    else:
        print("id가 없습니다. id를 입력해주세요.")

def export_transaction(format):
    if(format != "csv"):
        return print("현재는 csv 확장자 외에는 지원하지 않습니다.")
    datas_list= load_transactions()
    field_names = ['id', 'date', 'category', 'amount', 'memo']
    f = open(export_file_path, "w")

    writer = csv.DictWriter(f, fieldnames=field_names)

    writer.writeheader()
    writer.writerows(datas_list)

    f.close()

    print("success for export csv")
    # two_dimen_data_list = [
    #     ['id', 'date', 'category', 'amount', 'memo']
    # ]

    # for i in datas_list:
    #     two_dimen_data_list =[
    #         *two_dimen_data_list,
    #         [i["id"], i['date'], i['category'], i['amount'], i['memo']]
    #     ]

    # f = open(export_file_path, "w")
    # writer = csv.writer(f)

    # writer.writerows(two_dimen_data_list)
    # f.close()