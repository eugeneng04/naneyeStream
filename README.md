Streams Naneye Camera data over TCP Socket

REQUIRES MATLAB RUNTIME

set up for Naneye 2D camera with NanoUSB2 Eval Kit

usage: "streamNaneyeImage('ip', port)" in directory, where ip is a string, port is a number

data is 250000 bytes (250 x 250 image), but due to socket protocol it won't be sent at once

example python code in python folder with some functions to decode the data
