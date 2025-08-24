# Nidolya's Prospecting Tool

## What's the best build (TL;DR)
For Luck Efficiency (also known as mythic/exotic hunting builds) using my default constants (final results may vary slightly based on the constants), the best build consists of:

    Pan: Frostbite Pan (Infernal)
    Pendant: Frosthorn Pendant
    Charm: Cryogenic Preserver
    Rings: 4x Mythril and 4x Vortex

## What is this?
This is a tool written in Python to help Prospecting players optimize their builds

### Features
* Calculate optimal luck efficiency builds
  * Fully configurable options include
    * Number of top builds to view
    * Time Constants (digspeed->seconds factor, shakespeed->seconds factor, additive constant)
    * Number of ring slots
    * List of gear to consider in the builds (5* and 6*)
    * Maximum number of each ring (since I know you don't have 8 voids yet)
    * Specific stat modifiers (potions, quest rewards)
    * Enable/Disable Meteor and Totems
  * Shows luck efficiency for each build (number of rolls per second)

### Upcoming Features
* Input sets of stats and see which has a higher luck efficiency
* Money and Balance builds (not anytime soon, Modifier Boost's internal implementation is unkown)
* Ability to run script in browser

## How do I use this?
There are two ways to use this tool

### Run it yourself
1. Have Python installed
2. Download prospecting.py
3. In your terminal, navigate to the file and run `python prospecting.py`
4. Follow the steps. For full defaults, just mash enter

### Run it in an online compiler ("What is a terminal???")
1. Google "Online Python Compiler"
2. Click any link (make sure it supports command line input, most will)
3. Paste the code from prospecting.py into the online compiler
4. Hit run
5. Follow the steps. For full defaults, just mash enter

## How does it work?
The python script essentially compiles a list of all possible item combinations (based on your input) and plugs them into an equation to calculate the luck efficiency of each build.

### What is Luck Efficiency?
Luck Efficiency is a measurement that determines how much effective luck a build has, where getting more rare items in  shorter amount of time (statistically) is considered more effective. This is ultimately defined as the number of in-game rolls (to determine what item you get) per second.

Luck is the number of rolls the game makes on an item to determine what it is (with the lower roll - rarer item - taking precedence). The higher your luck, the better your odds of having a rare item.

Capacity relates to the number of items you get. A higher capacity means more items. More items means more things to roll on, which means better odds at getting a rarer item. The average number of items per pan is equal to the square root of your capacity.

Thus, we can calculate the average number of rolls per pan as (luck * sqrt(capacity) * .625)
* On average, 50% of items have full luck applied, 25% have no luck applied, and 25% have a random value within 0-1x luck. This averages out to .625

This is great, but doesn't tell the whole story. Now that we know how many rolls are applied per pan, we need to know how fast we're able to do a pan (dig and shake), since the faster we can pan, the more items we get in a given time-frame -> the more rolls we make in a time frame.

The time per pan is equal to the time spent digging, time spent shaking, and time spent doing everything else (moving between shore and water, waiting for animations to complete, lag, etc).

1. Time spent digging:
  The total time spent digging is equal to the number of digs we have to complete multiplied by how fast it takes to complete one dig (in seconds).
    * Number of digs is equal to our capacity divided by our dig strength (times 1.5 if making perfect digs), rounded up to the nearest integer (if we have 100 capacity, and we fill 30 of it per dig, we need to do 4 digs to fill it up). This is expressed as ceil(capacity / (dig strength * 1.5)) 
        * ceil is just a function that rounds a number up to the nearest integer
    * Time spent per dig is a function that it inversely proportional to our dig speed (a higher dig speed means we spend less time on each dig). This is expressed as (c / dig speed), where c is some constant factor.
        * What is this constant factor? It's just a number of seconds that correlates dig speed to time. This exact value is not known, and seems to depend on a variety of non-controllable factors, including latency and framerate. In personal tests, I've found this to be about 2 (which means that, at 100% dig speed, it takes about 2 seconds from when you first click dig to when you can effectively begin clicking dig again). As such, I leave this constant defaulted around 2, but feel free to test and chance this as you will.
  
  Thus, we can define the time spent digging as (ceil(capacity / (dig strength * 1.5)) / (c / dig speed))

2. Time spent shaking:
  This is exactly the same as time spent digging, but without the 1.5x factor, and a different constant. In my own tests, this seems to be about .35 (which means that, at 100% shake speed, we can complete three shakes in about 1 second)

3. Additional time spent:
  This is everything else that isn't immediately included with digging and shaking. Such as moving around, waiting for the shake animation to finish (if you sandshake, reduce this value), lag, and whatever else.

  This can easily be measured on your own. 1st, calculate the first two constants measured above, then time yourself fully completing 100 pans (or more), then divide by that number. Subtract the time spent digging and shaking calculated above, and you have your additive constant! For my preliminary tests, this was in the range of about 4.7 seconds.

Add these all up, and you get the total time it takes to complete one pan. Rolls per pan / second per pan = rolls / second.

Thus, we can define our final luck efficiency measurement as:
* (Luck * sqrt(capacity * .625)) / ((ceil(capacity / (dig strength * 1.5)) / (c1 / dig speed)) + (ceil(capacity / shake strength) / (c2 / shake speed)) + c3)
Plug in the constants you want and your stats, and you have your final measurement!
