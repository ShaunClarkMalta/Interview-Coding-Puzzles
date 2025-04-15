'''You are given the arrival times arr[] and departure times dep[] of all trains that arrive at a railway station on the same day. 
Your task is to determine the minimum number of platforms required at the station to ensure that no train is kept waiting.

At any given time, the same platform cannot be used for both the arrival of one train and the departure of another. 
Therefore, when two trains arrive at the same time, or when one arrives before another departs, additional platforms are required to accommodate both trains.'''

'''Sort Arrivals + Departures lists
platform_counter,, arrival_time,, departure_time
while not at end of lists:
    if arrival_time < departure time:
        add counter
    else:
        pass
return: platform_counter'''

def minimum_platforms(arrival_times, departure_times):
    arrival_times.sort()
    arr_counter = 0
    departure_times.sort()
    dep_counter = 0
    platform_counter = 0    #Counter of platforms needed at any given moment
    max_platforms = 1       #Maximum number of platforms needed throughout the day

    while (arr_counter < len(arrival_times)) & (dep_counter < len(departure_times)):    #Iterate through until reaching the end of the lists
        if arrival_times[arr_counter] < departure_times[dep_counter]:       #If the Arrival time is less than the Departure time, then you need another platform
            platform_counter += 1
            if (platform_counter > max_platforms):                          #Updates if you need more platforms than recorded
                max_platforms = platform_counter
            arr_counter += 1            #Also need to increment the Arrival Counter to view next timeslot
        else:                           #If the Arrival time is more than the Departure time, then a train has time to leave and you can just increment the departure counter and can decrement the platforms needed at the moment
            platform_counter -= 1
            dep_counter += 1
    return max_platforms

arr_list1 = [900, 940, 950, 1100, 1500, 1800]
dep_list1 = [910, 1200, 1120, 1130, 1900, 2000]
print(f"For Timeslots 1, you need: {minimum_platforms(arr_list1,dep_list1)} Platforms")
arr_list2 = [900, 1235, 1100]
dep_list2 = [1000, 1240, 1200]
print(f"For Timeslots 2, you need: {minimum_platforms(arr_list2,dep_list2)} Platforms")
arr_list3 = [1000, 935, 1100]
dep_list3 = [1200, 1240, 1130]
print(f"For Timeslots 3, you need: {minimum_platforms(arr_list3,dep_list3)} Platforms")