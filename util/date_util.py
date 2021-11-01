from datetime import datetime

def parse(str):
    if str is None:
        return None
    if not str:
        return None 
    return datetime.strptime(str, '%d/%m/%Y')

def now():
    dt = datetime.datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")
