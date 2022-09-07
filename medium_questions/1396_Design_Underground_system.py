"""
time_for_transit = {(inStation:outStation):[3, 5, 1]}

in_system = {id:(station, t)}

in_system = {32:(Paradise, 8), 27:(Leyton, 10)}


{(in_system[id][0], stationName):t-in_system[id][1]}
time_for_transit = {("Leyton", "Waterloo"):[12]}

getAverageTime sum(time_for_transit[("Leyton", "Waterloo")])/len(...)
"""
import collections

class UndergroundSystem:

    def __init__(self):
        self.time_for_transit = collections.defaultdict(list)
        self.in_system = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_system[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.start_station = self.in_system[id][0]
        start_time = self.in_system[id][1]
        self.time_for_transit[(self.start_station, stationName)].append(t-start_time)
        del self.in_system[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        num = sum(self.time_for_transit[(startStation, endStation)])
        denom = len(self.time_for_transit[(startStation, endStation)])
        return num/denom

    # Actual Solution
    def __init__(self):
        self.check_in_data = {}
        self.journey_data = collections.defaultdict(lambda : [0, 0])
                
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        # Access and remove the data for id. Note that removing it is actually
        # optional, but we'll discuss the benefits of it in the space complexity
        # analysis section.
        start_station, start_time = self.check_in_data.pop(id)
        self.journey_data[(start_station, end_station)][0] += (t - start_time)
        self.journey_data[(start_station, end_station)][1] += 1
            
    def getAverageTime(self, start_station: str, end_station: str) -> float:
        total_time, total_trips = self.journey_data[(start_station, end_station)]
        # The average is simply the total divided by the number of trips.
        return total_time / total_trips