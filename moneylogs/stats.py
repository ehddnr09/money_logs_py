from calendar import monthrange
import storage
import os.path

file_path = "/app/data/transactions.json"

def stats_transaction(month: str):
    if os.path.isfile(file_path) is False:
            return print("데이터가 없습니다. 먼저 데이터를 추가해주세요.")
    splitMonth = month.split("-")
    correctYear = splitMonth[0]
    correctMonth = splitMonth[1]


    datas_list = storage.load_transactions()

    filteredData = {
            "full_acount": 0,
            "many_expense_category": "",
            "many_expense_amount": 0,
            "one_day_average": 0,
            "each_category": {
                "food": 0,
                "coffee": 0,
                "transport": 0,
                "etc": 0
            }
        }
    # FilteredEachItemCategoryFood = filteredData["each_category"]["food"]
    # FilteredEachItemCategoryCoffee = filteredData["each_category"]["coffee"]
    # FilteredEachItemCategoryTransport = filteredData["each_category"]["transport"]
    # FilteredEachItemCategoryEtc = filteredData["each_category"]["etc"]
    
    for item in datas_list:
        itemSplitArr = item["date"].split("-")
        itemYear = itemSplitArr[0]
        itemMonth = itemSplitArr[1]
        
        itemAmount = item["amount"]
        
        if itemYear == correctYear and itemMonth == correctMonth:
            filteredData["full_acount"] += itemAmount
            
            if item["category"] == "food":
                filteredData["each_category"]["food"] += itemAmount
            elif item["category"] == "coffee":
                filteredData["each_category"]["coffee"] += itemAmount
            elif item["category"] == "transport":
                filteredData["each_category"]["transport"] += itemAmount
            else:
                filteredData["each_category"]["etc"] += itemAmount
    
    for key, value in filteredData["each_category"].items():
        
        if filteredData["many_expense_amount"] < value:
            
            filteredData["many_expense_category"] = key
            filteredData["many_expense_amount"] = value
    inquryMonth = monthrange(int(splitMonth[0]),int(splitMonth[1]))
    
    filteredData["one_day_average"] = filteredData["full_acount"] / inquryMonth[1]

        
    print(f'{month} 지출 요약\n\n총 지출:{filteredData["full_acount"]}\n가장 많이 쓴 카테고리: {filteredData["many_expense_category"]} {filteredData["many_expense_amount"]}\n일평균 지출: {filteredData["one_day_average"]}\n카테고리 별:\nfood: {filteredData["each_category"]["food"]}\ncoffee: {filteredData["each_category"]["coffee"]}\ntransport: {filteredData["each_category"]["transport"]}\netc: {filteredData["each_category"]["etc"]}')