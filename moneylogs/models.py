amount_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "date": {"type": "string"},
        "category": {"type": "string", "enum": ["food", "coffee", "transport", "etc"]},
        "amount":{"type": "integer"},
        "memo": {"type": "string"}
    },
    "required": ["id", "date", "category", "amount", "memo"]
}
# class AmountModel:
#     def __init__(self, id=None, date=None, category=None, amount=None, memo=None):
#         self.id = id
#         self.date = date
#         self.category = category
#         self.amount = amount
#         self.memo = memo

    



