#yep put "_" for station names in there sir

class UndergroundSystem:

    def __init__(self):
        self.stationdict = defaultdict(list)
        self.customers = defaultdict(list)

    #customer with id, check in here at time t
    #only can check in 1 place, 1 time
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id].append((t,stationName))

    #checkout at id, here, time t
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, start_station = self.customers[id][0][0], self.customers[id][0][1]
        self.stationdict[start_station + "_"+ stationName].append(t - start_time)
        del self.customers[id]
 

    #get average time from start to end station
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.stationdict[startStation +"_"+ endStation]) / len(self.stationdict[startStation +"_"+ endStation])
        


#store average time of trips here
# {stationname : [time, time, time] }


# {id : [(time1 start_station), (time2 end_station)]}

# everytime we get time2, we clear it out, add the time into stationame 




# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)