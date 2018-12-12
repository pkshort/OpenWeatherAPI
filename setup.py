from setuptools import setup, find_packages

with open("README.rst") as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='OpenWeatherAPI',
    version='0.1.0',
    description='Open Weather Map API app',
    long_description=readme,
    author='Paul Kevin Short II',
    author_email='pkevinshort@gmail.com',
    url='https://github.com/pkshort/OpenWeatherAPI',
    license=license,
    packages=find_packages(exclude('tests', 'docs'))
)
