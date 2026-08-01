class UndergroundSystem:

    def __init__(self):
        self.customers={}
        self.stations={}

        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id]=(stationName,t) #key->id, value-> (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # pop out the customer from customers map since the ride ot trip is over
        startstation,starttime=self.customers.pop(id)
        trip=startstation,stationName  # StationNmae here is end station . its cout
        
            #incerment the time by new sum
            #increment the count of trips by 1
        if trip in self.stations:
            self.stations[trip][0]+=(t-starttime)
            self.stations[trip][1]+=1
        else:
            self.stations[trip]=[t-starttime,1]

        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip=(startStation,endStation)
        return self.stations[trip][0]/self.stations[trip][1]
        


