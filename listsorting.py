def ASCII(x):
    if type(x)==str:
         return ord(x)
    return x
l=["A",-20,"a",94,96]
l.sort(key=ASCII)
print("SORTED LIST: ",l)

