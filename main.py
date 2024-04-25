"""
main.py
"""

# todo:
# - create FeatureGroups for each layer
# - legend to toggle on/off layers

import folium
import csv

from datetime import datetime

TIME_COLORS = {
    "twilight": "#808080",   # Grayish
    "sunrise": "#FFA500",    # Orangeish
    "morning": "#FFFF00",    # Yellow
    "afternoon": "#00FF00",  # Green
    "evening": "#FF4500",    # Orange-red
    "night": "#000080"       # Navy blue
}


def get_hour(datetime_str):
    # parse the datetime string into a datetime object
    dt_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    return dt_object.hour


# specify location
m = folium.Map(location=(40.730610, -73.935242),
               tiles="cartodb positron", zoom_start=12)

start_coordinates = []
end_coordinates = []
bike_type = []
ride_id = []
started_at = []

with open("./2023-citibike-tripdata/1_January/202301-citibike-tripdata_1.csv") as d:
    reader = csv.reader(d)
    for row in reader:
        start_lat, start_lng = (row[8], row[9])
        end_lat, end_lng = (row[10], row[11])
        start_coordinates.append((start_lat, start_lng))
        end_coordinates.append((end_lat, end_lng))
        bike_type.append(row[1])
        ride_id.append(row[0])
        started_at.append(row[2])
        # print(coorsdinates)

start_coordinates.pop(0)
end_coordinates.pop(0)


# associate colors to bike type
line_colors = []
for b in bike_type:
    if b == "classic_bike":
        line_colors.append('#00A9B4')  # light blue
    elif b == "electric_bike":
        line_colors.append('orange')
    else:
        line_colors.append('red')

start_hour = []
for t in started_at:
    try:
        hour = get_hour(t)
        start_hour.append(hour)
    except ValueError:
        start_hour.append(999)


lcft = []  # LineColorsForTime :)
for h in start_hour:
    if 0 < h < 3:
        lcft.append(TIME_COLORS["twilight"])
    elif 4 < h < 7:
        lcft.append(TIME_COLORS["sunrise"])
    elif 8 < h < 11:
        lcft.append(TIME_COLORS["morning"])
    elif 12 < h < 15:
        lcft.append(TIME_COLORS["afternoon"])
    elif 16 < h < 19:
        lcft.append(TIME_COLORS["evening"])
    elif 20 < h < 23:
        lcft.append(TIME_COLORS["night"])


# generate polylines

for i in range(len(ride_id)-10):
    # for i in range(len(start_coordinates)):
    try:
        if end_coordinates[i]:
            polyline = [[float(start_coordinates[i][0]), float(start_coordinates[i][1])], [
                float(end_coordinates[i][0]), float(end_coordinates[i][1])]]
            folium.PolyLine(
                locations=polyline,
                color=lcft[i],
                weight=1,
            ).add_to(m)
            # print("new line added to the map")
        else:
            # do nothing
            # some rows don't have end coords for some reason
            print("ride never finished")
    except ValueError:
        print(
            f"bad data at line {i}, id: {ride_id[i]}, start x: {start_coordinates[i][0]} start y: {start_coordinates[i][1]} end x: {end_coordinates[i][0]} end y: {end_coordinates[i][1]}")


m.save("index.html")
