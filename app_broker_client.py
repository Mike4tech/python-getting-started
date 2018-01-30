import requests
import json

CONFIG_FILE = json.load(open("config.json", "r"))

MESSAGE_TYPE_ID = "54121087-14f1-4c2a-835f-117681618cc9"
APP_ID = CONFIG_FILE["GEENY_APPLICATION_ID"]
HOST   = CONFIG_FILE["GEENY_APPLICATION_BROKER_SUBSCRIBER_URL"]
AUTH_TOKEN = CONFIG_FILE["GEENY_APPLICATION_AUTH_TOKEN"]
MAX_BATCH_SIZE = 10

class AppBrokerClient:
    def __init__(self):
        pass

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
        print uri
        response = requests.get(uri, headers = self.headers())
        print response
        return response.json()

  # def get_messages(iterator)
  #   uri = URI("#{HOST}/#{APP_ID}/messageType/#{BROKER_CONFIG[:message_type_id]}/iterator/#{iterator}")
  #   data = get(uri)
  #   JSON.parse(data.body)
  # rescue => error
  #   if data.code != 200
  #     puts "Error getting messages for iterator #{iterator}"
  #     p iterator
  #     p data
  #   end
  #   raise error
  # end

  # private

  # def set_headers(req)
  #   req['Accept'] = 'application/json'
  #   req['Content-Type'] = 'application/json'
  #   req['Authorization'] = "JWT #{AUTH_TOKEN}"
  # end
  # def request(method, uri, data=nil)
  #   req = nil
  #   if method == :get
  #     req = Net::HTTP::Get.new(uri)
  #   elsif method == :post
  #     req = Net::HTTP::Post.new(uri, 'Content-Type' => 'application/json')
  #     req.body = data.to_json
  #   end
  #   set_headers(req)
  #   Net::HTTP.start(uri.host, uri.port, :use_ssl => true) do |http|
  #     response = http.request req
  #     response
  #   end
  # end
  # def get(uri)
  #   request(:get, uri)
  # end
  # def post(uri, data)
  #   request(:post, uri, data)
  # end
