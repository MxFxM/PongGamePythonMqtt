import paho.mqtt.client as mqtt

BROKER_IP = "192.168.178.61" # this is my local mqtt broker
BROKER_PORT = 1883         # standard mqtt broker port
BROKER_TOPIC = "Games/Pong"

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

while True:
    client.loop()