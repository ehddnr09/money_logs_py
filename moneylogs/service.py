from storage import TransactionRepository
from models import Transaction

class MoneyLogService:
    def __init__(self):
        self.transaction_repo = TransactionRepository()
        self.transaction_model = Transaction

    def add_transaction(self, date, category, amount, memo):
      add_status = self.transaction_repo.add({
        "date": date,
        "category": category,
        "amount": amount,
        "memo": memo
      })

      if add_status:
        print("save success")
      else:
        print("save failed")
    
    def list_transaction(self, month = None, category = None):
      data_list = self.transaction_repo.load()
      filtered_data_list = []
      if month:
        for item in data_list:
          if self.transaction_model(date=item.date).is_same_month(month=month):
                filtered_data_list.append(item)
        return filtered_data_list
      
      elif category:
        for item in data_list:
            if self.transaction_model(category=item.category).is_category:
                filtered_data_list.append(item)
        return filtered_data_list
      
      return data_list
    
    def delete_transaction(self, id:int):
      delete_status = self.transaction_repo.delete(id=id)

      if delete_status:
        return print("delete success")
      else:
        return print("delete failed retry")
    

                