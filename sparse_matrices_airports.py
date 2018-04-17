import random
from math import sqrt

def createFields(AM):
    random.seed(AM)
    wx_europe = 3154 #km
    wy_europe = 5341 #km
    init_wx = random.randint(0, wx_europe)
    init_wy = random.randint(0, wy_europe)
    longitude = []
    latitude = []
    longitude.append(init_wx)
    latitude.append(init_wy)
    while len(longitude) < 1000:
        new_x = random.randint(0, wx_europe)
        new_y = random.randint(0, wy_europe)
        cond = True
        for i in range(0, len(longitude)):
            dist = sqrt((new_x - longitude[i])**2 + (new_y - latitude[i])**2)
            if dist < 100:
                cond = False
                break
        if cond:
            longitude.append(new_x)
            latitude.append(new_y)

    return longitude, latitude

def createFlights():
    departures = []
    arrivals = []
    while len(departures) < 10000:
        new_d = random.randint(0, 999)
        new_a = random.randint(0, 999)
        if new_a != new_d:
            departures.append(new_d)
            arrivals.append(new_a)

    return departures, arrivals

def store_sparse(dep, arr, lon, lat):
    iloc = [-1] * 1000
    j = [-1] * 10000
    D = [-1] * 10000
    Next = [-1] * 10000
    for i in range(10000):
        j[i] = arr[i]
        D[i] = sqrt((lon[arr[i]] - lon[dep[i]]) ** 2 + (lat[arr[i]] - lat[dep[i]]) ** 2)
        if iloc[dep[i]] == -1:
            iloc[dep[i]] = i
        else:
            index = iloc[dep[i]]
            if Next[index] == -1:
                Next[index] = i
            else:
                while Next[index] != -1:
                    index = Next[index]
                Next[index] = i

    return iloc, j, D, Next

def printMin(iloc, j, D, Next):
    min_sum = 0
    for i in range(1000):
        index = iloc[i]
        if index != -1:
            min_dist = D[index]
            while Next[index] != -1:
                index = Next[index]
                min_dist = min(min_dist, D[index])

            min_sum = min_sum + min_dist
    print(min_sum, "km")

def main():
    longitude, latitude = createFields(1046970)
    departures, arrivals = createFlights()
    iloc, j, D, Next = store_sparse(departures, arrivals, longitude, latitude)
    printMin(iloc, j, D, Next)

if __name__ == '__main__':
    main()