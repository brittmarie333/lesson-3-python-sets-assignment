#Objective: The aim of this assignment is to deepen your understanding and application of Python sets.
#Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
#You have two sets of flight destinations, one for each airline. Write a Python program to find out:

#1. Destinations that both airlines fly to.
#2. Destinations unique to your airline.
#3. Whether there are any destinations that neither airline shares.

britt_air = {"LAX", "PHX", "SFO", "ANC", "OAK", "ONT"}
jet_blue = {"PHX", "ANC", "BUR", "SJC", ""}

common_airports = britt_air and jet_blue
print("Britt Air and Jet Blue both fly through the following airports: ", common_airports)

britt_air_specific = britt_air - jet_blue
print("Jet Blue doesn't share ", britt_air_specific, ".")

unshared_airports = britt_air ^ jet_blue
print("Airports that Britt Air and Jet Blue don't share: ", unshared_airports)