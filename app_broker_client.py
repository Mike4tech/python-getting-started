import requests
import json

CONFIG_FILE = json.load(open("config.json", "r"))
MESSAGE_TYPE_ID = "54121087-14f1-4c2a-835f-117681618cc9"
APP_ID = CONFIG_FILE["GEENY_APPLICATION_ID"]
HOST   = CONFIG_FILE["GEENY_APPLICATION_BROKER_SUBSCRIBER_URL"]
AUTH_TOKEN = CONFIG_FILE["GEENY_APPLICATION_AUTH_TOKEN"]
MAX_BATCH_SIZE = 10

class AppBrokerClient:
    def headers(self):
        return {
            'accept': "application/json",
            'content-type': "application/json",
            'authorization': 'JWT ' + AUTH_TOKEN
        }

    def get_shards(self):
        uri = HOST + "/" + APP_ID + "/messageType/" + MESSAGE_TYPE_ID
        response = requests.get(uri, headers = self.headers())
        return response.json()

    def get_iterator(self, shard_id):
        data = {
            'shardId': shard_id,
            'iteratorType': "EARLIEST",
            'maxBatchSize': MAX_BATCH_SIZE
        }
        uri = HOST + "/" + APP_ID + "/messageType/" + MESSAGE_TYPE_ID + "/iterator"
        iterator = requests.post(uri, json=data, headers=self.headers())
        return iterator.json()

    def get_messages(self, iterator):
        uri = HOST + "/" + APP_ID + "/messageType/" + MESSAGE_TYPE_ID + "/iterator/" + iterator
        response = requests.get(uri, headers = self.headers())
        return response.json()
