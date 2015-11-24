#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Code harvested 00:35 MDT 24 NOV 2015 and derived from these sources:
# http://www.wadewegner.com/2014/05/create-an-ibeacon-transmitter-with-the-raspberry-pi/
# https://github.com/tyarkoni/transitions

"""
* (dispatcher.py) Function:
    * Reads sensor
    * Posts using BLE Beacon
"""

import os
import zmq
import sys
import time
from transitions import Machine
import logging

logging.basicConfig(filename='/var/log/sensor/dispatcher.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

SLEEPVALUE = 1
MAXVALUE   = 500.0

# Setup ZeroMQ
port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:%s" % port)

# Write out our PID file so we can kill this process later
def writePidFile():
  pid = str(os.getpid())
  f = open('/var/run/sensor/dispatcher.pid', 'w')
  f.write(pid)
  f.close()

class thermocouple(object):
  def __init__(self, name, v=0.0):
      """Return object whose name is *name* and starting
      value is *value*."""
      self.name = name
      self.value = value

  def set_value(self, v):
      """Capture a value measure."""
      if value > MAXVALUE:
          raise RuntimeError('Value over maximum.')
      self.value = v
      return self.value

  def get_value(self):
      """Dequeue the next value recorded."""
      s = socket.recv()
      self.value = float(s)
      """Make the last value this value."""
      return self.value

  def last_value(self):
      """Return the previous value recorded."""
      return self.value

  def is_changing(self, v):
      """Return BOOLEAN comparing last recorded value."""
      return self.value != v

probe = thermocouple("Surt")

states=['idle', 'sensing']

transitions = [
  ['non_zero', 'idle',         'sensing'],
  ['changing', 'sensing',      'sensing'],
  ['zero',     'sensing',      'idle'],
]

machine = Machine(probe, states=states, transitions=transitions, initial='idle')

while True:
  t = probe.get_value()
  logging.debug("State and Value: %s %s", probe.state, str(t))
  
  # Accept event and fire transition "non_zero" when value is non zero.
  # Throw away event otherwise
  w = probe.get_value()
  while t == 0.0:
    sleep(SLEEPVALUE)
    t = probe.get_value()
  
  probe.non_zero()
  logging.debug("State and Value: %s %s", probe.state, str(t))
  
  # Debounce - Not every probe needs this, fake debounce
  t = probe.get_value()

  # Assume probe has debounced
  probe.changing()
  logging.info("State and Value: %s %s", probe.state, str(t))
  
  # Accept event and Trigger transition "zero" when probe value is 0.0
  # Throw away event otherwise
  t = probe.get_value()
  while not t == 0.0:
    sleep(SLEEPVALUE)
    t = probe.get_value()
  # Send the value to Beacon

  probe.zero()
  logging.debug("State and Value: %s %s", probe.state, str(t))
  
  # Probe has hit Zero, start over again
  probe.timeout()

# End Infinte Loop
