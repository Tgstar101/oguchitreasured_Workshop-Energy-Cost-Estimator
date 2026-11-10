# oguchitreasured_Workshop-Energy-Cost-Estimator

# Workshop Energy Cost Estimator

## What it does
This Program asks for each machine's name, power in watts and hours used per day. It then calculates the daily and monthly energy use in kWh and the cost at the user's local tariff, and prints a table with the totals.

## How to run i
Install Python 3, then run: python energy_cost_estimator.py

## Sample output
How many machines do you have? 3
Enter your tariff (cost per kWh, e.g. 209.5): 209.5

Machine 1 of 3
  Name: Lathe
  Power in watts: 1500
  Hours used per day (0 to 24): 6

Machine 2 of 3
  Name: Welding machine
  Power in watts: 4000
  Hours used per day (0 to 24): abc
  Invalid input. Please type a number (e.g. 5 or 2.5).
  Hours used per day (0 to 24): 2

==============================================================
Machine              Daily kWh   Monthly kWh    Monthly cost
--------------------------------------------------------------
Lathe                     9.00        270.00        56565.00
Welding machine           8.00        240.00        50280.00
Drill                     2.25         67.50        14141.25
--------------------------------------------------------------
TOTAL                    19.25        577.50       120986.25
==============================================================
Daily cost: 4032.88
Workshop rating: HIGH usage - look for ways to save energy

Biggest energy user: Lathe
If it runs 1 hour less per day, you save 45.00 kWh and 9427.50 per month.


## My own twist
The program finds the machine that uses the most energy and shows how much energy and money you would save per month if it ran 1 hour less each day. It also gives the whole workshop a usage rating (low, moderate or high).

## What I learned
I learned to check input before using it, so the program does not crash when someone types a letter instead of a number. I also learned how a function can return a value that I use in other parts of the program.
I learnt how to use try expect.

## Author
OGUCHI TREASURED GINIKACHIM, ND2 Mechatronics Engineering, YABA COLLEGE OF TECHNOLOGY (YABATECH).
