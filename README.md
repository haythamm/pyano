#Pyano<br>
Ver. 1.0

**Generates a .wav file containing the synthesized digits of pi (or any numbers given as input).**
<br><br>In the current configuration, numbers 0-9 are assigned ascending notes, with the length of each note depending on whether or not the
previous number is a multiple of 2, 3.
<br><br>
###How do I pi?
Place a text file containing the digits you like to synthesize into the py_files directory, then run main.py
<br>The script will generate a .wav file for every txt in the py_files directory.

######Note: If you have a MASSIVE file (100,000+ digits), you may need to split the file into parts.
###Requirements
* Python 3+
* PySynth
* Numpy
