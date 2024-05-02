"""
5/1/2024
Elijah Burlinson

This program takes a csv file and extracts the variables based on a string, an empty list, and the filename.
The csv file must be saved in the same directory as this program to work.
The most common source of error is mispelled file or variable names when using dict_counts.
As user input will not be a part of generating the graphs, no input validation was included in this script.
"""
import csv
import plotly.graph_objects as go


# this should be the first function used when plotting two variables.
# It takes two strings, which need to be the column names in the csv file.
# These will be the two available variables.
def dict_counts(filename, par_1, par_2, lst_1, lst_2, dct, column_names_):
    with open(filename, 'r') as f_:
        reader = csv.reader(f_)
        for row in reader:
            column_names_.append(row)
            break
        x = column_names_[0].index(par_1)
        y = column_names_[0].index(par_2)
        next(f_)
        for row in reader:
            lst_1.append(row[x])
            lst_2.append(row[y])
            # check if starting/stoping location is a key
            # if key, increment count by one
            # if not, add it to the dictionary w/ct 1
            if (row[x], row[y]) not in dct:
                d[row[x], row[y]] = 1
            if (row[x], row[y]) in dct:
                d[row[x], row[y]] += 1
    return dct, lst_1, lst_2, column_names


# this function takes two variables and uses the counts of each combination to determine size and color.
def scatter(x_lst, y_lst, count_lst, par_1, par_2):
    fig = go.Figure(data=[go.Scatter(
        x=x_lst, y=y_lst,
        mode='markers',
        marker=dict(size=count_lst, color=count_lst)
    )])
    fig.update_layout(title=f'Scatter Plot of {par_1} and {par_2}')
    # fig.write_html("./static/scatter.html")
    return fig.show()


# this function takes two variables and uses the counts for the color, same as the above.
def twod_histogram(lst1, lst2, cts_, par_1, par_2):
    fig = go.Figure(go.Histogram2d(
        colorscale='Viridis', x=lst1, y=lst2, z=cts_))
    fig.update_layout(title=f'Histogram of {par_1} and {par_2}')
    fig.write_html("./static/histogram.html")
    return fig


if __name__ == '__main__':
    rideable_type = []
    start_station = []
    end_station = []
    member_casual = []
    column_names = []
    d = {}
    # the above lists are the variables used to code this project.
    # Note: start_station and end_station give the largest/most visually interesting graphs.
    # the 2d-histograms are the most visually appealing AND readable.
    # was not sure if there should be more variety in graph types.
    # happy to make more if desired!
    # DICTIONARY FORMAT: d = {(x1, y1) : COUNT, (x1, y2): COUNT....}

    # parameter names, to save time on typing out the names (and typos)
    # use these in the par_1 and par_2 positions for the string arguments
    # other parameters are available in different csv files, best to double check the file.
    ssn = 'start_station_name'
    rt = 'rideable_type'
    esn = 'end_station_name'
    mc = 'member_casual'

    # COLOR NAMES
    # to change the color gradient
    # these should be changed in the function, I didn't want to add yet another argument
    # feel free to add one if you want to easily change the color gradient though
    blackb = 'Blackbody'
    blr = 'Bluered'
    erh = 'Earth'
    elc = 'Electric'
    grs = 'Greens'
    vrs = 'Viridis'
    rnb = 'Rainbow'

    # scatter plot
    dict_counts('./data/202309-citibike-tripdata_1.csv',
                'start_station_name',
                'end_station_name', start_station, end_station, d,
                column_names)
    # print(column_names)

    cts = []  # this and the two below lines get the counts from the dictionary
    for v in d.values():
        cts.append(v)
    scatter(start_station, end_station, cts, ssn, esn)

    # 2D histogram
    d1 = {}
    dict_counts('./data/202309-citibike-tripdata_1.csv',
                rt,
                ssn,
                rideable_type, start_station, d1,
                column_names)

    cts1 = []
    for f in d1.values():
        cts1.append(f)
    twod_histogram(rideable_type, start_station, cts1, rt, ssn)
