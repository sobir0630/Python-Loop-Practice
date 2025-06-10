kamp = 5
count = 0

while count < 3:
    tax = int(input("taxmin kritng: "))
    if tax == kamp:
        print("topdingiz")
        break
    else:
        print("qayta urining!!!")
        count +=1
else:
    print("urinishlar tugadi")