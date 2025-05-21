#Error handling
try:
  result = 10/0
except ZeroDivisionError:
    print("It cannot be divided by zero")
except Exception as error:
  print("error")