import socketio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sio = socketio.Client()


adxl_data = {'X': [], 'Y': [], 'Z': []}
mag_data = {'X': [], 'Y': [], 'Z': []}
temp_humidity_data = {'Temperature': [], 'Humidity': []}

fig_adxl = plt.figure()
ax_adxl = fig_adxl.add_subplot(111, projection='3d')
ax_adxl.set_title('ADXL345 Accelerometer Data (3D)')
ax_adxl.set_xlabel('X-axis')
ax_adxl.set_ylabel('Y-axis')
ax_adxl.set_zlabel('Z-axis')

fig_mag = plt.figure()
ax_mag = fig_mag.add_subplot(111, projection='3d')
ax_mag.set_title('Magnetometer Data (3D)')
ax_mag.set_xlabel('X-axis')
ax_mag.set_ylabel('Y-axis')
ax_mag.set_zlabel('Z-axis')

fig_temp_humidity = plt.figure()
ax_temp_humidity = fig_temp_humidity.add_subplot(111)
ax_temp_humidity.set_title('Temperature and Humidity Data')
ax_temp_humidity.set_xlabel('Time')
ax_temp_humidity.set_ylabel('Value')

@sio.event
def adxl(data):
    print('ADXL:', data)
    adxl_data['X'].append(data[0])
    adxl_data['Y'].append(data[1])
    adxl_data['Z'].append(data[2])

    ax_adxl.cla()
    ax_adxl.scatter(adxl_data['X'], adxl_data['Y'], adxl_data['Z'], label='ADXL345', c='r', marker='o')
    ax_adxl.legend()
    plt.pause(0.1)

@sio.event
def mag(data):
    print('Magnetometer:', data)
    mag_data['X'].append(data[0])
    mag_data['Y'].append(data[1])
    mag_data['Z'].append(data[2])

    ax_mag.cla()
    ax_mag.scatter(mag_data['X'], mag_data['Y'], mag_data['Z'], label='Magnetometer', c='b', marker='o')
    ax_mag.legend()
    plt.pause(0.1)

@sio.event
def vth(data):
    print('Temperature and Humidity:', data)
    temp_humidity_data['Temperature'].append(data[1])
    temp_humidity_data['Humidity'].append(data[2])

    ax_temp_humidity.cla()
    ax_temp_humidity.plot(temp_humidity_data['Temperature'], label='Temperature', c='r')
    ax_temp_humidity.plot(temp_humidity_data['Humidity'], label='Humidity', c='b')
    ax_temp_humidity.legend()
    plt.pause(0.1)

@sio.event
def connect():
    print('Connected to server')
@sio.event
def disconnect():
    print('Disconnected from server')

if __name__ == '__main__':
  
    sio.connect('http://localhost:3000')

    try:
        plt.ion()  # Enabling  interactive mode
        sio.wait()  

    except KeyboardInterrupt:
        pass
    finally:
        plt.ioff() 
        plt.show()
        sio.disconnect()
