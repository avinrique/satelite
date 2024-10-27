import serial
import json
import socketio


serial_port = '/dev/ttyACM0' 
baud_rate = 9600


ser = serial.Serial(serial_port, baud_rate)
arr = []  
sio = socketio.Client()

sio.connect('http://127.0.0.1:3000')

while True:
    line = ser.readline().decode('utf-8').strip()

    if line.startswith("A:"):
        try:
            adxl_values = [float(value) for value in line[2:].split(',')]
            sio.emit('adxl', adxl_values)
            print("Sent adxl data to the server:", adxl_values)
        except :
             pass
       


    elif line.startswith("M:"):
        try :
            mag_values = [float(value) for value in line[2:].split(',')]
            sio.emit('mag', mag_values)
            print("Sent mag data to the server:", mag_values)
        except :
            pass
    elif line.startswith("Q:"):
        try :
             
            vth_values = [float(value) for value in line[2:].split(',')]
            sio.emit('vth', vth_values)
            print("Sent vth data to the server:", vth_values)
        except :
             pass

    elif line.startswith("C:"):
        try :
            co_values = [float(value) for value in line[2:].split(',')]
            sio.emit('co', co_values)
            print("Sent co data to the server:", co_values)
        except :
             pass

    elif line.startswith("B:"):
        try :

            bmp_values = [float(value) for value in line[2:].split(',')]
            sio.emit('bmp', bmp_values)
            print("Sent bmp data to the server:", bmp_values)
        except :
             pass
    
    elif line.startswith("G"):
        if line == "Gps out of range":
                try :
                    sio.emit('gps', "Gps out of range")
                    print("Sent gps data to the server:", line)
                except :
                     pass
        else :
                try :
                    gps_values = [float(value) for value in line[2:].split(',')]
                    sio.emit('gps', gps_values)
                    print("lat and long of gps : ", gps_values)
                except :
                     pass