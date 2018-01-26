import requests
import json

CONFIG_FILE = json.loads(open("config.json", "r").read())

# CONFIG = JSON.parse(File.read("config.json"))
# BROKER_CONFIG = {
#   message_type_id: "54121087-14f1-4c2a-835f-117681618cc9",
#   iterator_type:  'EARLIEST',
#   max_batch_size:  10
# }

class AppBrokerClient:
    def __init__(self):
        pass
