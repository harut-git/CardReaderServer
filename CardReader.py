import serial


def reader():
    while 1:
        # m = input('Enter an ID\n')
        # return m
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
                    entry_id = ser.read(size=10)
                    print type(entry_id)
                    return entry_id
            except Exception as e:
                print "Error on reading"
                print e.message
        else:
            print "Cannot open Serial Port"
