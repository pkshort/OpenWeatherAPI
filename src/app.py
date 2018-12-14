#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open Weather API - Takes in CSV file and outputs the current weather based
On locations given
"""

import json
import logging
import os
import sys
import signal
from flask import Flask

from weather import WeatherData

# ----> Basic application setup <----
with open('config.json') as file:
    config = json.load(file)
logging.basicConfig(level=logging.DEBUG, format=config['log_format'])


# Flask server setup
APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_FOLDER = os.path.join(APP_ROOT_FOLDER, 'templates')
STATIC_FOLDER = os.path.join(APP_ROOT_FOLDER, 'static')
PROGRAM_NAME = 'OpenWeatherAPI'
APP = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)


# ---->  Setup a signal handler to shutdown Flask <----
def handler(signum, frame):
    #pylint: disable=unused-argument
    """ This will capture shutdown events - handle any cleanup items in this function
        both parameters are required but not used by the program """
    logging.debug('Shutting down server')
    exit()


# Capture both the ctl-c and kill signals
signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGINT, handler)



# ----> Application Routes go here <----
@APP.route('/')
def display():
    """ Default route - for now process and return the data"""
    weather = WeatherData(config)
    weather.get_api_data()
    return APP.response_class(weather.display_data(), 200)


@APP.route('/version')
def version():
    """ Respond with the program version """
    return APP.response_class("My Application v 0.1", 200)


# Main
if __name__ == '__main__':
    # Install Control+C signal handler
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))
    # Startup flask app
    APP.run(host='0.0.0.0', port=5000, debug=True)
