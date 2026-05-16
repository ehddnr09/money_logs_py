from calendar import monthrange
import storage
import os.path

file_path = "/app/data/transactions.json"

class MonthlyStats:
  def __init__(
    self, 
    total_amount:int = 0, 
    top_category:str = "", 
    top_category_amount:int = 0, 
    daily_average:int = 0, 
    amount_by_category:dict[str, int] = {
      "food": 0,
      "coffee": 0,
      "transport": 0,
      "etc": 0
    }
  ):
    self.total_amount = total_amount
    self.top_category = top_category
    self.top_category_amount = top_category_amount
    self.daily_average = daily_average
    self.amount_by_category = amount_by_category



