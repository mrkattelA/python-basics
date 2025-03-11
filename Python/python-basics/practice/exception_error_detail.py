#ZeroDivisionError
try:
    1/0
except Exception as e:
    print(type(e))
    print(e,"\n")

#ValueError
try:
    int("a")
except Exception as e:
    print(type(e))
    print(e,"\n")

#NameError
#try:
#    print(foo)
#except Exception as e:
 #   print(type(e))
  #  print(e,"\n")

#FileNotFoundError
try:
    open("nonexisiting/file/abc/txt", "r")
except Exception as e:
    print(type(e))
    print(e,"\n")

#ModuleNotFoundError
#try:
#    import non_exisiting_module
#except Exception as e:
#    print(type(e))
 #   print(e,"\n")

#TypeError
try:
    nums= [1,2] #list are iterables not iterators
    next(nums)
except Exception as e:
    print(type(e))
    print(e,"\n")

#AttributeError
try:
    greeting = "Namaste"
    greeting.print() # strings don't have print() method
except Exception as e:
    print(type(e))
    print(e,"\n")

#StopIteration
try:
    nums = [1,2]
    iter_nums = iter(nums)
    print(next(iter_nums))
    print(next(iter_nums))
    print(next(iter_nums))
except Exception as e:
    print(type(e))
    print(e,"\n")

#KeyError
try:
    grades = {"Math" :45, "Science":55,"Art":53}
    print(grades["Music"])
except Exception as e:
    print(type(e))
    print(e,"\n")


