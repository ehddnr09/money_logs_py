from storage import TransactionRepository
from models import Transaction
from stats import MonthlyStats

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
        return "save success"
      else:
        return "save failed"
    
    def list_transaction(self, month = None, category = None):
      data_list = self.transaction_repo.load()
      filtered_data_list = []
      if month:

        for item in data_list:
          
          if self.transaction_model(date=item.date).is_same_month(month=month):
                filtered_data_list.append(item)
        return filtered_data_list
      
      if category:
        for item in data_list:
            if self.transaction_model(category=item.category).is_category(category=category):
                filtered_data_list.append(item)
        return filtered_data_list
      
      return data_list
    
    def delete_transaction(self, id:int):
      delete_status = self.transaction_repo.delete(id=id)

      if delete_status:
        return "delete success"
      else:
        return "delete failed retry"
      
    def get_monthly_stats(self, month: str):
      data_list = self.transaction_repo.load()
      transaction_model = self.transaction_model
      monthly_stats = MonthlyStats()
      sorted_data_list = []
      
      for item in data_list:
        item_amount = item.amount

        if transaction_model(date= item.date).is_same_month(month=month):
          monthly_stats.total_amount += item_amount
          sorted_data_list.append(item)

          if transaction_model(category= item.category).is_category(category="food"):
            monthly_stats.amount_by_category["food"] += item_amount
          elif transaction_model(category= item.category).is_category(category="coffee"):
            monthly_stats.amount_by_category["coffee"] += item_amount
          elif transaction_model(category= item.category).is_category(category="transport"):
            monthly_stats.amount_by_category["transport"] += item_amount
          elif transaction_model(category= item.category).is_category(category="etc"):
            monthly_stats.amount_by_category["etc"] += item_amount
      
      for key, value in monthly_stats.amount_by_category.items():
        if monthly_stats.top_category_amount < value:
          monthly_stats.top_category = key
          monthly_stats.top_category_amount = value
      
      sorted_data_list.sort(key=lambda dict_data: int(dict_data.date.split("-")[2]))
      
      # print(sorted_data_list)
      # split_month = month.split("-")
      # inqury_month = monthrange(int(splitMonth[0]),int(splitMonth[1]))
      inqury_month = int(sorted_data_list[len(sorted_data_list) - 1].date.split("-")[2])

      monthly_stats.daily_average = monthly_stats.total_amount / inqury_month

      return monthly_stats
