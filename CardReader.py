import serial


def reader():
    ser = serial.Serial(port='COM1', baudrate='9600')
    try:
        ser.isOpen()
        print "Serial port is open"
    except Exception as e:
        print ("Error")
        print e.message
        exit()

    if ser.isOpen():
        try:
            while 1:
                print ser.read_all()
        except Exception as e:
            print "Error on reading"
            print e.message
    else:
        print "Cannot open Serial Port"
