#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation

# This example shows how you can use the MQTT client in a class.

# import context  # Ensures paho is in PYTHONPATH

import paho.mqtt.client as mqtt
import time

class MqttHandler(mqtt.Client):

    HOST_IP = "192.168.178.114"
    PORT = 1883
    KEEP_ALIVE = 30
    TOPIC_LIGHTS = "lights/config"
    TOPIC_HORNS = "horns/config"

    def __init__(self) -> None:
        self.horns_config = 0
        self.lights_config = 0
        super().__init__()
        self._connect()
        self.loop_start()

    def _connect(self):
        self.reconnect_delay_set(min_delay=1, max_delay=120)
        self.connect_async(host=self.HOST_IP,
                           port=self.PORT,
                           keepalive=self.KEEP_ALIVE)
    
    def on_connect(self, mqttc, obj, flags, rc):
        print("MQTT handler connected rc: "+str(rc))
        self.subscribe(topic=self.TOPIC_LIGHTS)
        self.subscribe(topic=self.TOPIC_HORNS)

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")
        time.sleep(1)

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

        if msg.topic == self.TOPIC_LIGHTS:
            self.lights_config = msg.payload
            print("new lights config", self.lights_config)
        elif msg.topic == self.TOPIC_HORNS:
            self.horns_config = msg.payload
            print("new horns config", self.horns_config)    

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

if __name__ == "__main__":
    handler = MqttHandler()
    count = 0
    while True:

        try: 
            time.sleep(2)
        except KeyboardInterrupt:
            handler.disconnect()
            break