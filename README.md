# OpenWeatherAPI

This application takes in a CSV file and retrieves information from the Open Weather Map API based on the cities given in the CSV and outputs a CSV file with the weather of those particular cities as well as displaying the results on the local host address: 'http://127.0.0.1:5000/'.



## Getting Started

### On Linux Terminal
After downloading or forking this project, you first want to download the libraries needed via the requirements.txt file then you can proceed to build the flask app by using the command 'export FLASK_APP=app.py' while in the same directory as weather.py (within /src). Before you can run the project, make sure to get an API key from Open Weather Map, and add the key to the config.json file under the variable name 'api_key'. Once an API key is added, you can run the app using the command 'python3 -m flask run' while in the directory /src.

### Prerequisites

Make sure to have Python 3.x installed before running the source files, either free or paid for API key from Open Weather Map. The program will automatically create an 'output.csv' file in the source directory after the program is run. Also make sure to install all packages within the requirements.txt file.


## Built With

* [Python](https://docs.python.org/3.6/) - Programming Language
* [Open Weather Map API](https://openweathermap.org/current) - API
* [Flask](http://flask.pocoo.org/docs/1.0/) - Micro web framework
