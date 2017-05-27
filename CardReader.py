import serial


def reader(ser, close=True):
    try:
        ser.isOpen()
        print "Serial port is open"
    except Exception as e:
        print ("Error")
        print e.message
        exit()
    if ser.isOpen():
        try:
            while close:
                entry_id = ser.read(size=10)
                print type(entry_id)
                return entry_id
        except Exception as e:
            print "Error on reading"
            print e.message
    else:
        print "Cannot open Serial Port"


def tester():
    ser = serial.Serial(port='COM1', baudrate='9600')
    k = reader(ser)
    ser.close()
    print "port closed"
    print k
