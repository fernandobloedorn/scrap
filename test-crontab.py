from utils import save_file
from time import gmtime, strftime

save_file(strftime("%Y-%m-%d %H:%M:%S", gmtime()), "fer.txt")

