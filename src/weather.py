
# load in csv file
# call weather API for locations
# output csv: location, temperature, wind speed, weather description

import csv, requests, pprint, json, time

with open('locations.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    #api request
    api_key = "88aa68dfe44643228b20a74fbd7a47c9"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    units = "imperial"

    #setting up output header
    loc_str = "Location"
    temp_str = "Current Temperature"
    wind_str = "Wind Speed"
    desc_str = "Description"

    #built output header
    output_header = [loc_str, temp_str, wind_str, desc_str]

    #output file - output.csv
    output_csv = "output.csv"

    #opening output file
    with open(output_csv, mode = "w") as output_file:
        output_writer = csv.writer(output_file, delimiter=',')
        output_writer.writerow(output_header)
        for row in csv_reader:
            for key, value in row.items():

                    #can call API 60 times per second
                    time.sleep(.17)
                    city_name = str(value);
                    #built url
                    complete_url = (base_url + "appid=" + api_key +
                            "&q=" + city_name +
                            "&units=" + units)

                    response = requests.get(complete_url)
                    my_json = response.json()
                    #if statement to make sure the API call was successfull
                    if my_json["cod"] != "404":
                        rec = my_json["main"]
                        current_temp = rec["temp"]
                        wind = my_json["wind"]
                        wind_speed = wind.get("speed")
                        weather = my_json["weather"]
                        weather_desc = weather[0]["description"]

                        #output_writer writes to csv file
                        output_writer.writerow([str(city_name),
                                str(current_temp), str(wind_speed),
                                str(weather_desc)])


                        print("\nCity: " + str(city_name) +
                                "\n\tTemperature: " + str(current_temp) +
                                "\n\tWind Speed: " + str(wind_speed) +
                                "\n\tWeather Description: " + str(weather_desc))


                    else:
                        print("City not found..")

    #location, temperature, wind speed, description
