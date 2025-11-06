def main():
    phoneNumber = '+1 (800) 555-1212'
    prefix= phoneNumber[:2]
    print("prefix:", prefix)
    lastDigits = phoneNumber[-4:]
    print("lastDigits:", lastDigits)
    areaCode = phoneNumber[4:7]
    print("areaCode:", areaCode)

main()    