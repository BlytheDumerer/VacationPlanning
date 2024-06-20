# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 01:32:08 2024

@author: blythe

This code is to reduce the need of an excel sheet in the 
initial decision on where to take a vacation.

You will be able to input the date, location, flight costs, and hotel costs.

If you are able to stay with a friend or have free lodging already then input
$0

"""
import matplotlib.pyplot as plt

class DecidingOnAVacationLocationBasedOnPrice:

    def __init__(self):
        self.Trips = []
        
    def add_trip(self, date, location, flight_cost, hotel_cost):
        trip_details = {
            "date": date,
            "location": location,
            "flight_cost": flight_cost,
            "hotel_cost": hotel_cost,
            "total_initial_cost": flight_cost + hotel_cost
        }
        self.Trips.append(trip_details)
        
    def show_trip_costs(self):
        locations = [trip["location"] for trip in self.Trips]
        costs = [trip["total_initial_cost"] for trip in self.Trips]

        plt.figure(figsize=(6, 5))
        plt.bar(locations, costs)
        plt.xlabel('Location')
        plt.ylabel('Total Initial Cost ($)')
        plt.title('Initial Trip Costs by Location')
        plt.show()

#Call the Class
vacation_decider = DecidingOnAVacationLocationBasedOnPrice()

# Add trips or Modify Trips Here
vacation_decider.add_trip("2024-07-01 - 2024-07-10 ", "Texas", 75, 0)
vacation_decider.add_trip("2024-08-15 - 2024-08-20", "France", 300, 200)
vacation_decider.add_trip("2024-09-10 - 2024-09-14", "Germany", 200, 100)

# Show trip costs
vacation_decider.show_trip_costs()