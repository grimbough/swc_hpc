#!/usr/bin/env python

import resource
import platform
from argparse import ArgumentParser
from sys import stdout
from time import sleep

def occupy_memory(length):
    '''Create a list of ones of length <length>, to occupy memory in the system.'''
    try:
        size = int(length)
    except TypeError:
        raise "Expected an integer value for size parameter, got '{}''".format(length)
    print "List length is", format(length)
    list_of_ones = []
    for i in range(length):
        list_of_ones.append(1)

def wait_for(seconds):
    '''Suspend execution for <seconds> seconds, to control the length of time
    that the script takes to run.'''
    try:
        seconds = int(seconds)
    except TypeError:
        raise "Expected an integer value for time parameter, got '{}'".format(seconds)
    print "Wait time is", format(seconds), "seconds"
    sleep(seconds)

parser = ArgumentParser() # Use argparse.ArgumentParser to create a simple user interface
parser.add_argument("--time",   "-t", default=10, type=int,
                    help="Time (in whole seconds) that this script should take to run.")
parser.add_argument("--length", "-l", default=0,  type=int,
                    help="Length of list to generate. This approximates the amount of memory that the script will take up when it runs. Must be an integer.")

# parse arguments from the command line
args   = parser.parse_args()
secs   = args.time
list_length = args.length

print "Current host is:", format(platform.node())

occupy_memory(list_length)
wait_for(secs)

# fetch the memory being used by the script and print it out
mem_used = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000.0
print "Memory usage:", format(mem_used), " MB"
