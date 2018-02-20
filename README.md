# microbit-sonicpi

This is just a set of notes on a quick experiment to trigger [Sonic Pi](http://sonic-pi.net/) from a [micro:bit](http://microbit.org/) connected to the same machine via serial port and communicating via [OSC](http://opensoundcontrol.org/spec-1_0) over UDP.

This uses David Whale's [bitio](https://github.com/whaleygeek/bitio) library and the python-osc library.

# Installation

Follow [installation instructions for bitio](https://github.com/whaleygeek/bitio)

Install python-osc library, doing something like this:

    pip3 install python-osc

Ensure Sonic-Pi is running and the OSC Server is running. (Look in Prefs: IO)

Load and run the sonic-pi sketch `rx-sonicpi.rb`

Flash bitio hex onto a microbit

Run the python demo program `button_triggers.py` (the first time you run it it will ask you to unplug and replug your micro:bit, to detect port).
If you don't have bitio installed formally, you'll need it in your path.  One way to do this is on the command-line, assuming you're on a *nix sort of OS: 

    PYTHONPATH=~/your/path/to/bitio/src/ python3 button_triggers.py


Press buttons on the micro:bit and tilt it on various axes.  You should hear random notes being triggered, with different amount of cutoff depending on the amount of pitch (nose-down / nose-up tilt around the horizontal axis).  You should also see "cue" messages appearing in Sonic Pi's cues log, looking something like `/osc/mbit/neill [99, 85, "tri"]`

Now you're free to modify the python script and the Sonic Pi sketch to change when messages are sent to Sonic Pi, what they contain, and what Sonic Pi does with them!
