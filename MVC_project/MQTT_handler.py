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
from PyQt5.QtCore import *

class MqttHandler(mqtt.Client, QObject):

    HOST_IP = "192.168.178.114"
    PORT = 1883
    KEEP_ALIVE = 30
    TOPIC_LIGHTS = "lights/config"
    TOPIC_HORNS = "horns/config"

    connectedSignal = pyqtSignal()
    disconnectedSignal = pyqtSignal()

    def __init__(self) -> None:
        mqtt.Client.__init__(self)
        QObject.__init__(self)

    def connect_to_broker(self):
        self._connect()
        self.loop_start()

    def _connect(self):
        self.reconnect_delay_set(min_delay=1, max_delay=120)
        self.connect_async(host=self.HOST_IP,
                           port=self.PORT,
                           keepalive=self.KEEP_ALIVE)
    
    def on_connect(self, mqttc, obj, flags, rc):
        print("MQTT handler connected rc: "+str(rc))
        self.connectedSignal.emit()
    
    def on_disconnect(self, mqttc, obj, flags, rc):
        print("MQTT handler disconnected rc: "+str(rc))
        self.disconnectedSignal.emit()

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")
        time.sleep(1)

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    @pyqtSlot(int)
    def pub_light_config(self, config):
        if self.is_connected():
            self.publish(topic=self.TOPIC_LIGHTS, payload=config)

    @pyqtSlot(int)
    def pub_horn_config(self, config):
        if self.is_connected():
            self.publish(topic=self.TOPIC_HORNS, payload=config)


if __name__ == "__main__":
    handler = MqttHandler()
    handler.connect_to_broker()
    count = 0
    while True:

        try: 
            handler.pub_horn_config(count)
            handler.pub_light_config(count+1)
            count = count+1
            time.sleep(2)
        except KeyboardInterrupt:
            handler.disconnect()
            break
        
