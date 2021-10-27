import re
import unicodedata
import datetime
 
def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    text = re.sub('[^0-9a-zA-Z_ -@.]', '', str(text))
    return text

def retrieve_date_time():
    dt = datetime.datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def save_file(content, file):
    file = open(file, "a+")
    file.write(content + "\r\n")
    file.close()



