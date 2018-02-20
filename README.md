# microbit-sonicpi

This is just a set of notes on a quick experiment to trigger sonic pi from a micro:bit connected to the same machine via serial port and communicating via OSC over UDP.

This uses David Whale's bitio library and the python-osc library.

# Installation

Follow [https://github.com/whaleygeek/bitio](installation instructions for bitio)

Install python-osc library, doing something like this:

    pip3 install python-osc

Ensure Sonic-Pi is running and the OSC Server is running. (Look in Prefs: IO)

Load and run the sonic-pi sketch rx-sonicpi.rb

Flash bitio hex onto a microbit

Run the python demo program button_triggers.py (the first time you run it it will ask you to unplug and replug your microbit, to detect port).

Press buttons on the micro:bit and tilt it on various axes.  You should hear random notes being triggered, with different amount of cutoff depending on the amount of pitch (nose-down / nose-up tilt around the horizontal axis).  You should also see "cue" messages appearing in Sonic Pi's cues log, looking something like /osc/mbit/neill [99, 85, "tri"]

Now you're free to modify the python script and the Sonic Pi sketch to change when messages are sent to Sonic Pi, what they contain, and what Sonic Pi does with them!
