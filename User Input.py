"""
Draft of input menu for user
4/24/24

This is a possible decision tree for users, beginning with the parameter, then graph type, then other choices like
the year. It doesn't yet have input validation or the specific graph choices for each parameter.
To Do:
-graph options for each parameter
-input validation
-way to call the programs that graph the data?
"""
print('Hello! This program displays graphs of CitiBike data in NYC from years #### to ####')
par = input('Choose a parameter: rideable type, start station, end station, or member status.)
if par == 'rideable type':
    rideable_graphs = input('Choose a way to display the data: ')
elif par == 'start station': #combine start and end station into one?
    start_graphs = input('Choose a graph type: ')
elif par == 'end station':
    end_graphs = input('Choose a graph type: ')
elif par == 'member status':
    member_graphs = input('Choose a graph type: pie, ') # pie chart is a not fun option but it's available
else:
    print('Invalid parameter')

