import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

BROKER_IP = "192.168.178.61" # this is my local mqtt broker
BROKER_PORT = 1883           # standard mqtt broker port
BROKER_TOPIC = "Games/Pong"
CLIENT_ID = int(time.time()*1000)      # use time as id

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if str(rc) == "0":
        print("Connected with broker")
    else:
        print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(BROKER_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_IP, BROKER_PORT, 60)


# i need a state machine inside the pygame code
# first state is establishing connection which is done by sending
publish.single(BROKER_TOPIC, payload=f"client online {CLIENT_ID}", hostname=BROKER_IP, port=BROKER_PORT)
# second state is waiting for response, either rejected, when server is full, or accepted
#     with player number 1 or 2
# third state is waiting for second player (if first)
# forth state is game
# fifth state is victory or defeat screen
# then the program exits

while True:
    client.loop()