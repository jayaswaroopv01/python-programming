try :
    print (x)
except NameError:
    print("x is not defined")
except :
    print("Something is wrong")