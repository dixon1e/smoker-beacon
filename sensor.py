#!/usr/bin/env python
#
# Code harvested 00:35 MDT 24 NOV 2015 and derived from these sources:
#
# -*- coding: utf-8 -*-

"""
* (sensor.py) function:
    * Reads the thermocouple breakout board SparkFun_MAX31855K_Thermocouple
    * Adds the reading to a ZeroMQ queue
"""

import os
import zmq
import sys
import time
import timeit
import datetime
import serial ## Load the serial library
import logging

logging.basicConfig(filename='/var/log/sensor/sensor.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

# Set up ZeroMQ
port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:%s" % port)

# Sleep interval in seconds
interval = 1.0

# Write out our PID file so we can kill this process later
def writePidFile():
  pid = str(os.getpid())
  f = open('/var/run/sensor/sensor.pid', 'w')
  f.write(pid)
  f.close()

## Figure out how to open SPI
something = "something SPI"

## set up the sensor SPI bus
logging.info("******** SPI ******** ")
logging.debug("Connecting to: " + something)

## do anything needed here

logging.info("******** SPI ******** ")
logging.debug("Connected to: " + something)

## Begin infinite loop
while True:
  time.sleep(interval)
  start_time = timeit.default_timer()

## Read the breakout board
  logging.info("******** SPI ******** ")
  logging.debug("Reading: " + something)

## Wait for data to come in
  s = something
  elapsed = timeit.default_timer() - start_time

## Here's the elapsed reading time
  logging.debug("Read cycle time: %s", str(elapsed))

## Catch any other formatting problems
  logging.debug("SPI Value: %s", something)

## Capture, parse and convert value
# set value from something
  value = something
  
## Send the data to the queue
  msg = value
  socket.send(msg)
  logging.debug("MSG: %s", msg)

## End infinite loop

## Close the port, be a good citizen
# close something

