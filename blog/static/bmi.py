from browser import document
def func(event):
    w = float(document["weight"].value)
    h = float(document["height"].value)
    document["result"].text = str(w/h/h)
document["execute"].bind("click", func)