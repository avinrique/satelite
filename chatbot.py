
import socketio
import google.generativeai as genai
from datetime import date
sio = socketio.SimpleClient()
genai.configure(api_key="AIzaSyCRUpuFm2Nc17FbHNL-Fv-zNeogCDlqKBg")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
model = genai.GenerativeModel('gemini-pro')
sensor_data = {"adxl345" : None,
               "hmc345" : None,
               "temperature":None,
               "humidity" : None,
               "SolarPanelvolatge" : None,
               "altitude": None,
               "pressure" : None,
               "gps lat , long" : None,
               "carbon_monooxide" : None,
               "carbon dixoide" :None}
#chat history 
chat = model.start_chat(history=[])
chat.send_message("you are a chatbot design to provide info to the user about the cubesat made here. here I Avinav Gupta the leader of the group. with mmy team mates Harsha G , Naveen Gowda and Devdarshan made a cube satellite from arduino uno and raspberry pi. we are from bmsit banlore of ise department sec A.")
chat.send_message(f"""todays date is {date.today()}, well this satellite is a small project here the cubesat consist of few sensors like adxl345 , hmc5883 ,
                      bmp180, dth11, solar panel with voltage sensor to sense the voltage in solar panel, gps6mv2,mq2 sesor for co2 and co.
                      here we are also using 2 arduinos as tranciever and reciver 2 nrf24 module for communication. 
                      We are using 1 arduino with nrf as ground station and another for sattelite. we are also using 2 servo motor with solar panel to activate andmove solar panel.
                      here we are connecting our ground sttaion with a laptop and using serial communication for interacting with the data coming from arduino,
                      after that we are using a python 
                      program to get serial info coming from arduino and using socketio to send it to node server for displaying  and other stuffs
                      here we are also plotting the data from the adxl in 3d magnetometer (hmc) in 3d and (tempreature&humidity in 2d) we are also having a web interface and a chatbot intregation
                      so that people can come and question on the inputbox and can get a better experience from human like response , the estimated cost of the cubesat is 30000 inr but can go down to 15000 inr
                      , the sattelite in in the ground""" , safety_settings={'HARASSMENT':'block_none'})
chat.send_message(f"okey other than things related to the chatbot you are not supposed to answer and also try to give short answer as short as possible ")
chat.send_message("when some que like what is this or what is it is asked then you are suppossed to tell about the satellite not that this is a chatbot.only when they ask about the chatbot answer about yourself")
# chat.send_message("the sensor data that we are getting right now is ")
# chat.send_message("""you will also be getting the sensor data with the prompt, dont panic do do anything with data unless asked about them 
#                   the data of sensor will be in this format {'adxl345': [0.24, -1.1, -11.1], 'hmc345': [-34.18, -47.91, 27.76], 'temperature': 27.1, 'humidity': 73, 'SolarPanelvolatge': 0.52, 'altitude': 881.74, 'pressure': 91175, 'gps lat , long': 'Gps out of range', 'carbon_monooxide': 206, 'carbon dixoide': 402}
#                 now if they ask about the ccondition that is related to the data then only provide the answer else discard the data""")
@sio.event
def chatMessage(data):
    print(data)
    check = model.generate_content(f"""is this prompt '''{data}''' asking about the current situation of this settalite or current condition of temperature ,altitude, pressure ,
                           voltage, humidity , acceleration , magnetometer,co2 co, gps loction, then only then just response with "Yes" and nothing else
                                   look here how it works  
**Main Prompt:**                                   
**User:** Hey, whats the cuurent humidity?

**Chatbot:** The current humidity accrding  to  the satelite data is 73.

**Not Discarded Sensor Data:**

'adxl345': 0.27, -1.06, -11.06, 'hmc345': -34.18, -48.82, 27.86], 'temperature': 27.1, 'humidity': 73, 'SolarPanelvolatge': 0.9, 'altitude': 880.83, 'pressure': 91183, 'gps lat , long': 'Gps out of range', 'carbon_monooxide': 211, 'carbon dixoide': 410

**Reason for not Discarding:**
The sensor data is  relevant to the user's question, which is about the current condition of a CubeSat. The chatbot correctly identifies that this information is needed to answer the user's question and therefore it uses it . if it was about the cubesat rather than the condition of cubesat then it would be a big "NO" so check twuce if the prompt is asking about the realtime data and condition or not .

**User:** Hey, what is this?

**Chatbot:** This is a CubeSat, a small satellite used for research and educational purposes. It consists of several cubic units, each measuring 10 centimeters on a side. It is equipped with various sensors to collect data and communicate with the ground station.

**Explanation:** The chatbot provides a concise and informative answer to the user's question, explaining what a CubeSat is and its purpose.

**Discarded Sensor Data:**

'adxl345': 0.27, -1.06, -11.06, 'hmc345': -34.18, -48.82, 27.86], 'temperature': 27.1, 'humidity': 73, 'SolarPanelvolatge': 0.9, 'altitude': 880.83, 'pressure': 91183, 'gps lat , long': 'Gps out of range', 'carbon_monooxide': 211, 'carbon dixoide': 410

**Reason for Discarding:**

The sensor data is not relevant to the user's question, which is about the general nature and purpose of a CubeSat. The chatbot correctly identifies that this information is not needed to answer the user's question and therefore discards it.
I hope this demonstration is helpful. Please let me know if you have any other questions. 

                                    '""")
    print(check.text)
    if "yes" in check.text.lower() :
        response = chat.send_message(f"""well this is the sensor data'''{sensor_data}''' , okey if you find some pattern than say your opinion or just answer whats asked, where the prompt is '''{data}''' , answer in a way that everyone can understand and answer short """)
        sio.emit('responsemsg', response.text)
    else:
        response = chat.send_message(data)
        sio.emit('responsemsg',response.text)
        print(sensor_data)

@sio.event
def adxl(data):
    sensor_data['adxl345'] = data

@sio.event
def mag(data):
    sensor_data["hmc345"] = data

@sio.event
def co(data):
    sensor_data["carbon_monooxide"] = data[0]
    sensor_data["carbon dixoide"] = data[1]
@sio.event
def vth(data):
    sensor_data["SolarPanelvolatge"] = data[0]
    sensor_data["temperature"] = data[1]
    sensor_data["humidity"] = data[2]

@sio.event
def gps(data):
    sensor_data["gps lat , long"] = data

@sio.event
def bmp(data):
    sensor_data["pressure"] = data[0]
    sensor_data["altitude"] = data[1]



@sio.event
def connect():
    print('Connected to server')

# Event handler for 'disconnect' event
@sio.event
def disconnect():
    print('Disconnected from server')




if __name__ == '__main__':
  
    sio.connect('http://localhost:3000')

    try:   
        sio.wait()  # Wait for events
    except KeyboardInterrupt:
        sio.disconnect()
