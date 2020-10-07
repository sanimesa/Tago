import paho.mqtt.client as mqtt
import sys

#Definitions
#put your device token here
device_token = '2d474459-de11-4677-8012-f30c0ef2515b'   

broker_address = "mqtt.tago.io"
broker_port = 1883
keep_alive_broker_connection = 60
subscribe_topic = "mqtt_temp_test_device"

#put any name here, TagoIO doesn't validate this username.
mqtt_username = 'mqtt_client' 

#MQTT password must be the device token (TagoIO does validate this password)
mqtt_password = device_token 

#Callback - broker connection completed
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Connected to MQTT broker. Result: "+str(rc))

    #subscribe to custom MQTT topic chosen for TagoIO Action
    client.subscribe(subscribe_topic)

#Callback - received message from TagoIO platform (via MQTT)
def on_message(client, userdata, msg):
    msg_received = str(msg.payload)
    txt_msg = "[MSG] Topic: {topic} / Message(payload): {received}"
    print(txt_msg.format(topic=msg.topic, received=msg_received) )

#Main program
try:
    print("[STATUS] Initializing MQTT...")
    client = mqtt.Client()
    client.username_pw_set(mqtt_username, mqtt_password)

    #Setting up the MQTT callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    #MQTT broker connection
    client.connect(broker_address, broker_port, keep_alive_broker_connection)

    #Wait forever for received messages from TagoIO platform (via MQTT) in 
    #'on_message' callback
    client.loop_forever()

except KeyboardInterrupt:
    print("\nThis application is being terminated.")
    sys.exit(0)