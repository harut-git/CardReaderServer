import serial

# ser = serial.Serial(port='COM1', baudrate='9600')


def reader():
    while 1:
        k = input()
        with open("current.txt", 'w') as outfile:
            outfile.write(k)
    # try:
    #     ser.isOpen()
    #     print "Serial port is open"
    # except Exception as e:
    #     print ("Error")
    #     print e.message
    #     exit()
    # if ser.isOpen():
    #     try:
    #         while True:
    #             entry_id = ser.read(size=10)
    #             with open("current.txt", 'w') as outfile:
    #                 outfile.write(entry_id)
    #     except Exception as e:
    #         print "Error on reading"
    #         print e.message
    # else:
    #     print "Cannot open Serial Port"


reader()
