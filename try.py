import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    errno, strerror = e.args
    print "I/O error({0}): {1}".format(errno, strerror)
    print " e0 = ", e[0]
    print " e1 = ", e[1]
    for i in e:
        print i
except ValueError:
    print 'u\'v entered invalid number,\nmake sure its an int type'
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
