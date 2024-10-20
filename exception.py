try:
    age=int(input("Enter a number :"))
    income=20000
    risk=income/age
    print(risk)


except ZeroDivisionError:
    print("Age can't be zero.")
except ValueError:
    print("Invalid value.")
