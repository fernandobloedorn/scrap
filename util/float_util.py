
def parse(str):
    if str is None:
        return 0.0
    str = str.replace(".", "")
    str = str.replace(",", ".")
    return float(str)