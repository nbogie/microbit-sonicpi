# Requires python-osc and bitio
#   To install python-osc, use:
#     pip3 install python-osc
#   To run with temp bitio library in path, on a *nix system, use:
#     PYTHONPATH=~/path/to/bitio/src/ python3 script.py

from pythonosc import udp_client
import microbit
import time

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

def mymap(v, inmin, inmax, outmin, outmax):        
    scaled = round(outmin + (v - inmin)/(inmax-inmin) * (outmax - outmin))
    return clamp(scaled, outmin, outmax)

def clamp(v, outmin, outmax):
    if (v > outmax):
        v = outmax
    elif (v < outmin):
        v = outmin 
    return v

def noteFor(isLeftButton):
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    newy = mymap(y, -1024, 1024, 0, 127)
    newx = mymap(x, -1024, 1024, 0, 127)
    syn = "tri" if isLeftButton  else "mod_pulse"
    sender.send_message('/mbit/neill', [newx, newy, syn])
    time.sleep(0.1)

while True:
    if microbit.button_a.was_pressed():
        noteFor(True)
    elif microbit.button_b.was_pressed():
        noteFor(False)
