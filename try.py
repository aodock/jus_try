try:
    while True:
        n = int(raw_input("enter a number : "))
        print 'Entered value : ', n
        break
except ValueError:
    print 'u\'v entered invalid number,\nmake sure its an int type'
