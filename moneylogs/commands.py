from datetime import datetime, date

def error():
    raise ValueError()

def validate_date(date_text: str):
    try:
        d_day= datetime.strptime(date_text, "%Y-%m-%d")
        today = datetime.today()        

        if d_day > today:
            error()
        
        return True
    except ValueError:
        print("Incorrect data format({0}), should be YYYY-MM-DD".format(date_text), "or You don't choose future Date.")
        return False