import datetime
import os
import json
import commands
from enum import Enum, auto

file_path = "/app/data/transactions.json"

amount_schema = {
  "type": "object",
  "properties": {
      "id": {"type": "integer"},
      "date": {"type": "string"},
      "category": {"type": "string", "enum": ["food", "coffee", "transport", "etc"]},
      "amount": {"type": "integer"},
      "memo": {"type": "string"}
  },
  "required": ["id", "date", "category", "amount", "memo"]
}
class CategoryValue(Enum):
  # @staticmethod
  # def _generate_next_value_(name, start, count, last_values):
  #   return name
  
  food = "food"
  coffee = "coffee"
  transport = "transport"
  etc = "etc"
  

def type_check(data):
    if data["id"] is not int:
      commands.error()

    if os.path.isfile(file_path) is False and data["id"] is None:
      data["id"] = 0
    
    if data["date"] is None or commands.validate_date(date_text=data["date"]) is False:
      commands.error()

    if isinstance(data["category"], str) or data["category"] is None:
      commands.error()

    if isinstance(data["amount"], int) or data["amount"] is None:
      commands.error()

    if isinstance(data["memo"], str) or data["memo"] is None:
      commands.error()

    return data
    
class Transaction:
  def __init__(self, id: int = None, date: str = None, category: str = None, amount: int = None, memo: str = None):
    self.id = id
    self.date = date
    self.category = category
    self.amount = amount
    self.memo = memo

  def __str__(self):
    return f'id: {self.id}, date: {self.date}, category: {self.category}, amount: {self.amount}, memo: {self.memo}'

  def to_dict(self):
    return {
      "id": self.id,
      "date": self.date,
      "category": self.category,
      "amount": self.amount,
      "memo": self.memo
    }
  
  
  @classmethod
  def from_dict(cls, data):

    type_check_data = type_check(data=data)

    return cls(
        id = type_check_data["id"],
        date = type_check_data["date"],
        category = type_check_data["category"],
        amount = type_check_data["amount"],
        memo = type_check_data["memo"]
      )
    

  def is_category(self, category: str):
    return self.category == category
  
  def is_same_month(self, month: str):
    year_text, month_text = month.split("-")
    compare_year_text, compare_month_text, compare_day_text = self.date.split("-")

    return compare_year_text == year_text and compare_month_text == month_text
