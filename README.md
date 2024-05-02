# Project Description:
This project visualizes the uses CitiBikes stations using publically available data from March 2024 developed by @exu3 and @eburlinson for CS1210 final project. The end result will display two maps and two graphs. The maps will have the station use by the type of bike (electric versus regular) and the time of day. The graphs will have a scatter plot and a 2-D histogram, which display the uses of stations where rides start and end, with size (scatter) and color (histogram) correlating to the number of occurences.

# Instructions:
First, create a virtual environment to run the project with. This can be done with:

```sh
$ python3 -m venv citibike
```
To activate it, this command can be used:
```sh
$ . ./citibike/bin/activate
```
Next, install the dependencies that are listed below.
```
plotly
plotly.express
Flask
folium
```
These are all be 'pip-install'-able and they are listed in requirements.txt. These can be individually installed in the command line or installed with:

```sh
(citibike) $ pip install -r requirements.txt
```

To generate or update maps, run 'maps.py', and 'graphs.py' to generate or udpdate the scatter plot and the 2d-histogram. The output will be saved to the 'static' directory. 

Then, start the dev server with:

```sh
(citibike) $ flask run
```
Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the maps or plots! They will be displayed on an html page with links corresponding to each image. To view the individual images, click on the links. 
