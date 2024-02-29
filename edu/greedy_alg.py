states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {'kone': set(['id', 'nv', 'ut']),
            'ktwo': set(['wa', 'id', 'mt']),
            'kthree': set(['or', 'nv', 'ca']),
            'kfour': set(['nv', 'ut']),
            'kfive': set(['ca', 'az'])}

final_stations = set()
while states_needed:
    best_stations = None
    states_covered = set()
    for station, states_for_stations in stations.items():
        covered = states_needed & states_for_stations
        if len(covered) > len(states_covered):
            states_covered = covered
            best_stations = station
            states_covered = covered
    print(final_stations)
    final_stations.add(best_stations)
    states_needed -= states_covered
    
print(final_stations)



