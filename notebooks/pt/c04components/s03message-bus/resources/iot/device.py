import paho.mqtt.client as paho
import time
import random
import json
import datetime
import time
from threading import Thread



class IoT_mqtt_publisher:

    def __init__(self, broker, port):
        self.broker = broker
        self.port = port
        self.client = None
        self.connect()
        
    def connect(self):
        self.client = paho.Client("publisher{0}".format(random.randint(0,99999999)))
        
        if(not self.client.connect(self.broker, self.port)):                     #establish connection
            print("Connected.")        
        
    def publish(self, topic, payload):
        self.client.publish(topic,payload)  
        
                


class IoT_sensor(Thread):
    
    def __init__(self, name, dimension, unity, min_value, max_value, pooling_interval):
        Thread.__init__(self)        
        self.name = name
        self.dimension = dimension    
        self.unity = unity    
        self.max_value = max_value
        self.min_value = min_value    
        self.pooling_interval = pooling_interval
        self.publisher = None
        self.flag = True


    def connect(self, publisher):
        self.publisher = publisher
        self.start()

    def stop(self):
        self.flag = False
        
    def resume(self):
        self.flag = True
        self.run()
        
    def run(self):
        
        while self.flag:
            payload = {
                "source":"sensor",
                "name":self.name,
                "type":"reading",
                "body": {
                    "timestamp": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
                    "dimension": self.dimension,
                    "value": random.uniform(self.min_value,self.max_value),
                    "unity": self.unity                
                }

            }
            time.sleep(self.pooling_interval)
            self.publisher.publish( "sensor/{0}/{1}".format(self.name, self.dimension),
                                    json.dumps(payload))

        


# def on_publish(client,userdata,result):             #create function for callback
#     print("Message published!")

#                            #create client object
# #client1.on_publish = on_publish                          #assign function to callback






# authors  = ['Asdrubal', 'Luizadino','Yarapy']
# approved = [True, False, False, False, False]

# print("publishing...")

# while(True):
#     d = feedparser.parse('http://pox.globo.com/rss/g1/')
#     for post in d.entries:
#         item ={
#                'title':    post.title,
#                'summary':  post.summary,
#                'link':     post.link,
#                'source':   'g1',
#                'author':   random.choice (authors),
#                'approved': random.choice (approved)
#               }

#         client1.publish(pub_topic,json.dumps(item)) 
#         time.sleep(random.randint(3,8))
# print("Finished publishing!")