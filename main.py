"""
main.py
"""

import folium
import csv

# specify location
m = folium.Map(location=(40.730610, -73.935242),
               tiles="cartodb positron", zoom_start=12)

start_coordinates = []
end_coordinates = []
bike_type = []
with open("./2023-citibike-tripdata/1_January/202301-citibike-tripdata_1.csv") as d:
    reader = csv.reader(d)
    for row in reader:
        start_lat, start_lng = (row[8], row[9])
        end_lat, end_lng = (row[10], row[11])
        start_coordinates.append((start_lat, start_lng))
        end_coordinates.append((end_lat, end_lng))
        bike_type.append(row[1])
        # print(coorsdinates)

start_coordinates.pop(0)
end_coordinates.pop(0)


# associate colors to bike type
line_colors = []
for b in bike_type:
    if b == "classic_bike":
        line_colors.append('#ADD8E6')  # light blue
    elif b == "electric_bike":
        line_colors.append('orange')
    else:
        line_colors.append('grey')
# generate polylines

for i in range(1000):
    # for i in range(len(start_coordinates)):
    try:
        # polyline = [list(start_coordinates[i]), list(end_coordinates[i])]
        polyline = [[float(start_coordinates[i][0]), float(start_coordinates[i][1])], [
            float(end_coordinates[i][0]), float(end_coordinates[i][1])]]
        folium.PolyLine(
            locations=polyline,
            color=line_colors[i],
            weight=1,
        ).add_to(m)
        print("new line added to the map")
    except ValueError:
        print("bad data")


# print([float(start_coordinates[0][0]), float(start_coordinates[0][1])],
#       [float(end_coordinates[0][0]), float(end_coordinates[0][1])])
# test_line = [
#     [40.75972414, -73.973664165],
#     [40.7770575, -73.97898475]
# ]

# folium.PolyLine(
#     locations=test_line,
#     color="#FF0000",
#     weight=3,
# ).add_to(m)


m.save("index.html")
