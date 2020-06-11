import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

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
    global player1_id
    global player2_id

    message = str(msg.payload)
    print(message)
    # switch between game running or not
    # maybee state machine as in client
    if "client online" in message: # a new client wants to log on
        id = message.split(" ")[2][:-1]

        if player1_id is not None and player2_id is not None: # both player slots are filled
            # send reject
            publish.single(BROKER_TOPIC, payload=f"{id} rejected", hostname=BROKER_IP, port=BROKER_PORT)
        else: # a player slot is open
            if player1_id == None: # no player 1
                # send id accept player 1
                publish.single(BROKER_TOPIC, payload=f"{id} accepted player 1", hostname=BROKER_IP, port=BROKER_PORT)
                player1_id = id
            else: # no player 2
                # send id accept player 2
                publish.single(BROKER_TOPIC, payload=f"{id} accepted player 2", hostname=BROKER_IP, port=BROKER_PORT)
                player2_id = id

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

player1_id = None
player2_id = None

client.connect(BROKER_IP, BROKER_PORT, 60)

while True:
    client.loop()