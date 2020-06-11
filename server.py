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
    message = str(msg.payload)
    print(message)
    # switch between game running or not
    # maybee state machine as in client
    if "client online" in message: # a new client wants to log on
        if not player1_id is None and not player2_id is None: # both player slots are filled
            pass
            # send rejected
        else: # a player slot is open
            id = message.split(" ")[2]
            if player1_id == None: # no player 1
                pass
                # send id accept player 1
            else: # no player 2
                pass
                # send id accept player 2

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_IP, BROKER_PORT, 60)

player1_id = None
player2_id = None

while True:
    client.loop()