from tkinter import *
from PIL import Image,ImageTk
import json
foo = ['1',2,1.23]

print(foo[1])
bar = {}#dictionaries, structures
bar = {"candy": 5, "clippy": "idiot" } #hashtable, or name-value pair
print(bar['candy'])


with open ("MAP.json") as f:
    data=json.load(f)

try:
    string = (data['(0,0)']['north']['next-pos'])
except KeyError:
    print("XD")


print (string)




