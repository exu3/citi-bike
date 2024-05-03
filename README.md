# citi-bike

This project is a visualization of Citi Bike (a NY-based bike share program) usage using publicly available data. Geospatial data is visualized with maps which show the various trips taken throughout the month and corresponding information such as the type of bike (electric vs classic) and time of day. We also used scatter plots and histograms to visualize the popularity of certain routes, plotting trips using the start and end stations with correlation to the number of occurences.

This project uses `plotly` for graphing, `folium` for maps, and `Flask` for the web server that serves the visualizations.

## Run locally

Run `./setup.sh` or follow the steps below.

Create a virtual environment.

```sh
$ python3 -m venv citibike
```

Activate the virtual environment.

```sh
$ . ./citibike/bin/activate
```

Install dependencies.

```sh
(citibike) $ pip install -r requirements.txt
```

To generate or update maps/graphs respectively, run `maps.py` and `graphs.py`. The output will be saved to the `static` directory.

Start the dev server.

```sh
(citibike) $ flask run
```

Then, open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

##### appendix: division of labor, project difficulty

Elijah worked on the graphs, and Ella worked on the maps and web interface. The estimate of project difficulty is "moderate." We used Python language features covered in the course and libraries that were not covered in the course but are well-documented online. We encountered difficulties working with large datasets and ended up just going with a specific month because it was more manageable. The effort spent on this project is roughly equivalent to that of four or five homework assignments.
