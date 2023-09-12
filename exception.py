x= input("Enter no1 ")
y= input("Enter no2 ")

try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print("Division by ZDE")
    z = None
except Exception as e:
    print("Exception type",type(e).__name__)
    z=None