#Objective: The aim of this assignment is to deepen your understanding and application of Python sets.
#Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
#You have two sets of flight destinations, one for each airline. Write a Python program to find out:

#1. Destinations that both airlines fly to.
#2. Destinations unique to your airline.
#3. Whether there are any destinations that neither airline shares.

britt_air = {"LAX", "SFO", "ANC", "OAK", "ONT", "PHX", "BUR"}
kingdom_air = {"PHX", "ANC", "BUR", "SJC", "PSP", "LAS", "RNO"}

common_airports = britt_air & kingdom_air
print("Britt Air and Kingdomboth fly through the following airports: ", common_airports)

britt_air_specific = britt_air - kingdom_air
print("Kingdom Air doesn't share ", britt_air_specific, ".")

unshared_airports = britt_air ^ kingdom_air
print("Airports that Britt Air and Kingdom Air don't share: ", unshared_airports)