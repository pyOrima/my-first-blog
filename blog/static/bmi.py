from browser import document
import random, math
def func(event):
    w = float(document["weight"].value)
    h = float(document["height"].value)
    document["result"].text = str(w/h/h)
document["execute"].bind("click", func)