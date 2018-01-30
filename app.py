import app_broker_client

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Python!"

def load_iterator(client):
  shards = client.get_shards()
  iterator_json = client.get_iterator(shards["shards"][0]["shardId"])
  return iterator_json["shardIterator"]

def load_messages(iterator, client):
    next_iterator = iterator
    if (next_iterator == None):
        next_iterator = load_iterator(client)
        # TBD: cookies read
    return client.get_messages(next_iterator)

def get_messages(retries=0):
    client = app_broker_client.AppBrokerClient()
    try:
        iterator = request.cookies.get('iterator')
        return load_messages(iterator, client)
    except:
        if retries == 0:
            return get_messages(1)
        else:
            print("Error on retry")
            return

@app.route("/messages")
def messages():
    payload = get_messages()
    return str(payload)

app.run(host='0.0.0.0', port=3000)

###### TESTS #######

# client = app_broker_client.AppBrokerClient()
# shards = client.get_shards()
# iterator = client.get_iterator("0")
# messages = client.get_messages(iterator['shardIterator'])
# print messages
