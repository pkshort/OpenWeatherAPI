# Created by P. Kevin Short II

import csv
import logging
import requests
import tablib
import time

class WeatherData:
    """
        load in csv file
        call weather API for locations
        output csv: location, temperature, wind speed, weather description
    """

    def __init__(self, config):
        self.config = config
        #logging.debug("Initialize class")

    def get_api_data(self):
        with open(self.config['csv_file']) as csv_file:
            csv_data = csv.DictReader(csv_file, delimiter=',')
            api_key = self.config['api_key']
            base_url = "http://api.openweathermap.org/data/2.5/weather?appid={}&q={}&units={}"

            # imperial units switches the temperature from Kelvin to Farenheit
            units = self.config['units']

            # built output header
            output_header = [
                    "Location",
                    "Current Temperature",
                    "Wind Speed",
                    "Description"
                    ]

            # output file - output.csv
            output_csv = self.config['output_file']

            #logging.debug("Output header {}".format(output_header))

            # opening output file
            with open(output_csv, mode = "w") as output_file:
                output_writer = csv.writer(output_file, delimiter=',')
                output_writer.writerow(output_header)
                # looping through input file
                # DictReader is a dictionary within a dictionary, therefore
                # a nested loop is necessary
                for row in csv_data:
                    for key, value in row.items():
                        # API is throttled to 60 times per second
                        # sleep ensures that the API is called under 60/sec
                        time.sleep(float(self.config['api_throttle']))
                        city_name = str(value)
                        # Call the API using the fully formatted URL
                        try:
                            my_json = requests.get(base_url.format(api_key, city_name, units)).json()
                        except:  #pylint: broad except to capture API throttling
                            logging.error("API Call failed: {}".format(base_url.format(api_key, city_name, units )))
                            continue

                        # if statement to make sure the API call was successfull
                        if my_json["cod"] == 200:

                            # retrieving the data from the json response
                            rec = my_json["main"]
                            current_temp = rec["temp"]
                            wind = my_json["wind"]
                            wind_speed = wind.get("speed")
                            weather = my_json["weather"]
                            weather_desc = weather[0]["description"]

                            # output_writer writes to csv file
                            output_writer.writerow([str(city_name),
                                                    str(current_temp),
                                                    str(wind_speed),
                                                    str(weather_desc)])

                            #logging.debug("{},{},{},{}".format(str(city_name),
                                                               #str(current_temp),
                                                               #str(wind_speed),
                                                               #str(weather_desc)))
                        else:
                            logging.debug("API Call returned {}".format(my_json["cod"]))
                            logging.error("Error getting data for city {}".format(city_name))
            return

    def display_data(self):
        """
        Use tablib to format the csv data quickly
        """
        dataset = tablib.Dataset()
        with open(self.config['output_file']) as f:
            dataset.csv = f.read()
        return dataset.html
