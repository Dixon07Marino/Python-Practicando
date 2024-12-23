variableGlobal = "Como has estado?"

def myfunc():
    global variableGlobal
    variableGlobal = "Todo bien?"
    print("Hola bro, " + variableGlobal)

myfunc()
print("Hola bro, " + variableGlobal)