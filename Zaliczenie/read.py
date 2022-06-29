 #!/usr/bin/env python
 
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
import time

reader = SimpleMFRC522()
url = 'https://borowska.azurewebsites.net/api/HttpTrigger1?code=jkm-npVEhBUhgHMG99PAFkZ5hEKtfbAP2Ta5a34u28p3AzFu96_hTA=='

RED = 40
GREEN = 38
YELLOW = 36

try:
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(RED, GPIO.OUT)    
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    
    GPIO.output(YELLOW, GPIO.HIGH)
    
    id, text = reader.read()
    json = {'cardCode': id}
    print(id)
    response = requests.post(url, json = json)
    if response.status_code == 403:
        print('Zła karta')
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(RED, GPIO.LOW)
    elif response.status_code == 200:
        print('Dobra karta')
        GPIO.output(GREEN, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(GREEN, GPIO.LOW)
finally:
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.cleanup()
