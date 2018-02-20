# microbit-sonicpi

A simple experiment to trigger sonic pi from a microbit connected via serial port.

This uses David Whale's bitio library and the python-osc library.

# Installation

Follow [https://github.com/whaleygeek/bitio](installation instructions for bitio)

Install python-osc library, doing something like this:

    pip3 install python-osc

Ensure Sonic-Pi is running and the OSC Server is running. (Look in Prefs: IO)

Load and run the sonic-pi sketch rx-sonicpi.rb

Flash bitio hex onto a microbit

Run the python demo program button_triggers.py (the first time you run it it will ask you to unplug and replug your microbit, to detect port).

Press buttons on the micro:bit and tilt it on various axes.  You should see messages appearing in Sonic Pi's cues log, such as /osc/mbit/neill [99, 85, "tri"]

Now you're free to modify the python script and the Sonic Pi sketch to change when messages are sent to Sonic Pi, what they contain, and what Sonic Pi does with them!
