import machine
import math
import network
import os
import time
import utime
import pycom
from machine import RTC
from machine import SD
from machine import Timer
from L76GNSS import L76GNSS
from pytrack import Pytrack

from network import LoRa
import socket                                                         #Jose Envio LoRa
lora = LoRa(mode=LoRa.LORA)                                                      #Jose Envio LoRa
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)                               #Jose Envio LoRa
# setup as a station

import gc

time.sleep(2)
gc.enable()

# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())
utime.timezone(7200)
print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')
py = Pytrack()
l76 = L76GNSS(py, timeout=30)
chrono = Timer.Chrono()
chrono.start()
#sd = SD()
#os.mount(sd, '/sd')
#f = open('/sd/gps-record.txt', 'w')
while (True):

    coord = l76.coordinates()
    #f.write("{} - {}\n".format(coord, rtc.now()))
    #print("{} - {} - {}".format(coord, rtc.now(), gc.mem_free()))

    #Codigo Personalizado para enviar por LoRa Posicon:

    x = "witeklab-"+"12345678Z-"+str(coord[0]) + "-"+str(coord[1])
    s.setblocking(True)
    s.send(x)
    print(x)
    time.sleep(2) #Pausa entre toma de coordenadas.
