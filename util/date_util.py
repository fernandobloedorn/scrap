from datetime import datetime

def parse(str):
    if str is None:
        return None
    if not str:
        return None 
    return datetime.strptime(str, '%d/%m/%Y')

def now():
    dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def today():
    dt = datetime.now()
    return dt.strftime("%Y-%m-%d")

def dateToString(dt):
    if dt is None:
        return None
    return dt.strftime("%Y-%m-%d")