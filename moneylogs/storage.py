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
        if os.path.isfile(file_path) is False:
          with open(file_path, "w") as f:
            f.write("[]")
          return [] 
        with open(file_path, "r", encoding='utf-8') as f:
          json_data_list = json.load(f)
        
        dict_data_list= list(map(self.transaction.from_dict, json_data_list))
            
        
        return dict_data_list
      except ValueError:
        commands.error()


    
    def save(self, transactions: list[models.Transaction]):
      try:
        if os.path.isfile(file_path):
  
          save_data_list = []
          
          ## todo save function fix 
          for item in transactions:
            save_data_list.append(models.Transaction(
              id=item.id,
              date=item.date,
              category=item.category,
              amount=item.amount,
              memo=item.memo
            ).to_dict())
          
          
          with open(file_path, "w") as f:
              json.dump(save_data_list, f)
          return True
        else:
          json_data = json.dumps(transactions)
          with open(file_path, "w") as f:
                  f.write(json_data)
        
      except ValueError:
        commands.error()
    
    def next_id(self, id: int):
      
      return id + 1
    
    def add(self, transaction):
      # id = transaction.id
      
      category = transaction["category"]
      date = transaction["date"]
      amount = transaction["amount"]
      memo = transaction["memo"]
      if category != "coffee" and category != "food" and category != "transport" and category != "etc":
          return print("카테고리는 coffee or food or transport or etc 중에 골라주세요.")
          
      datas_list = []

      insert_data_model = models.Transaction(
          date=date,
          category=category,
          amount=amount,
          memo=memo
      )
      
      # insert_data = insert_data_model.to_dict()


      if os.path.isfile(file_path):
        
        datas_list = self.load()
      else:
        insert_data_model.id = 0 
        
        return self.save(transactions=insert_data_model)
        
      
      if len(datas_list) > 0:
          
          print(self.next_id(id=datas_list[len(datas_list)-1].id))
          insert_data_model.id = self.next_id(id=datas_list[len(datas_list)-1].id)

          transactions = [*datas_list, insert_data_model]
          self.save(transactions=transactions)

          return True
      else:
          insert_data_model.id = 0
          print(insert_data_model.id)
          transactions =[insert_data_model]
          print(transactions)
          self.save(transactions=transactions)

          return True
    def delete(self, id: int):
        if id == 0 or id:
        
          if os.path.isfile(file_path) is False:
              return print("데이터가 없습니다. 먼저 데이터를 추가해주세요.")
          datas_list= self.load()

          transactions = []
          
          
          for item in datas_list:
              if item.id != id:
                  transactions = [*transactions, item]
                  
          
          if len(transactions) == len(datas_list):
              return print("해당 아이디가 없습니다. 다시 확인 후 입력해주세요.")

          delete_status = self.save(transactions=transactions)

          return delete_status

        else:
            print("id가 없습니다. id를 입력해주세요.")



def export_transaction(format):
    if(format != "csv"):
        return print("현재는 csv 확장자 외에는 지원하지 않습니다.")
    datas_list= TransactionRepository.load()
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