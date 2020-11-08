#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import http.client
import urllib.parse

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

key = "FJCOCAFQMNLMO463"

def tripwire():
    if GPIO.input(4) == 1:
        print("safe")
    elif GPIO.input(4) == 0:
        print (GPIO.input(4))
        print ("Intruder")
        params = urllib.parse.urlencode({'field1': 1, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print ("connection failed")



if __name__ == "__main__":
        while True:
                tripwire()

GPIO.cleanup()
