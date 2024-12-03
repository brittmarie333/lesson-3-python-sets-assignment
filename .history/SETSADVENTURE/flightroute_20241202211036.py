#Objective: The aim of this assignment is to deepen your understanding and application of Python sets.
#Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
#You have two sets of flight destinations, one for each airline. Write a Python program to find out:

#1. Destinations that both airlines fly to.
#2. Destinations unique to your airline.
#3. Whether there are any destinations that neither airline shares.

britt_air = {"LAX", "PHX", "SFO", "ANC"}
jet_blue = {"PHX", "ANC", "BUR", "SJC"}

common_airports = britt_air and jet_blue
