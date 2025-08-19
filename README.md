Luck Efficiency = (luck * sqrt(capacity) * .65) / (panning time) = (L*sqrt(C))/P
	Where panning time (P) is the time it takes to pan (dig, move, shake, move, repeat)
	
P is most accurately measured as opposed to calculated, as it has too many factors
	but we can mathematically represent it
	
P = (total dig time) + constant + (total shake time) + constant + constant
	this last constant could be lag, animation glitches, etc
	= oD + oS + c
		the final constant (c) can only be measured, though we'll do a few trials to get an idea
		so that it can be used in the equation
		
oD (total dig time) = (number of digs needed) * (time per dig) = nd * td -> where nd and td are individual vars
	nd (number of digs) = ceiling(capacity / (dig strength * 1.5)) = ceiling(C / (mD * 1.5))
		We multiply dig strength by 1.5 for perfect digs
		ceiling takes the nearest int rounded up
	td (time per dig) = constant / (dig speed) = constant / sD
		Dividing by speed as a higher speed is less time
		We want to get this in terms of seconds. It'd be easy if 100% dig speed = 1 second to dig
			but we don't know this, it will be revealed after measurement
			
oS (total shake time) = (number of shakes needed) * (time per shake) = ns * ts
	ns (number of shakes) = ceiling(capacity / (dig speed)) = ceiling(C / (mS))
		No additional factor here, as shakes are always perfect and = to your shake strength
	ts (time per shake) = constant / (shake speed) = constant / sS
		Same as digs, we want this in seconds, constant will be figured out during testing
		
Thus, luck efficiency = 
								    (L * sqrt(C) * .65)
	-------------------------------------------------------------------------- (this is a divide line lol)
	(ceiling(C / (mD * 1.5)) * (c1 / sD)) + (ceiling(C / mS) * (c2 / sS)) + c3
	
Now, let's try to find a relatively accurate measurement for these constants, which we can only do 
	by measuring it in game

	First, we'll try to find c1 and c2 (which are the digging speed and shake speed factors), which hopefully are
		just = 1
	
	We can do this by calculating how much time it takes to do 2 digs at different speeds
		- Set 1 (58% dig speed, 2 digs per pan) = 7.16s, 6.87s, 6.94s (divide by 2) = 3.495s avg per dig
			3.495 * .58 = 2.0271
		- Set 2 (173% dig speed, 7 digs per pan) = 8.98s, 8.86s, 8.62s (divide by 7) = 1.26s avg per dig
			1.26 * 1.73 = 2.1798
		If we take the average, we get a constant of ~2.1. This can definitely be refined with
			more trials but I'll take this.
			As a note, the factor itself largely comes from the actual dig animation that plays out
				which I forgot existed until I did this trial lol
	
	Repeat for shake (should be a bit easier)
		- Set 1 (90% shake speed, 18 shakes per pan) = 7.53s, 7.11s, 7.14s = .403333333s
			.4... * .9 = .363
		- Set 2 (129% shake speed, 17 shakes per pan) = 5.01s, 4.95s, 4.84s = .2901960784s
			.29... * 1.29 = .3743519411
		Average gives us the constant factor of ~.37
	
	Now we can start to simplify, our overall luck efficiency equation looks like
		                     L * √(C) * .65
		-----------------------------------------------
		(2.1 * ⌈C / (mD * 1.5)⌉) + (.37 * ⌈C / mS⌉) + c
		 ----------------------     --------------
				   sD                     sS
	
	The only remaining portion to calculate is the final constant, which denotes any additional time aspects
		primarily movement and lag and the like. Honestly this should probably just be ignored, but for
		the sake of it, I'll do a simple measurement.
		
	Constant Trial:
		Stats: mD = 321, C = 788, sD = 173%, mS = 38, sS = 335%
		Results: 28 full pans completed in 4:25 (265 seconds) = 9.4642857143 seconds/pan
			Plugging the data in we get (2.1*ceil(788/(321*1.5)))/1.73 + (.37*ceil(788/38))/3.35 + c = 9.46
				= (2.1*2)/1.73 + (.37*21)/3.35 + c = 9.46 
				= 2.4277... + 2.319... + c = 9.46
				-> c = 4.71, which I'll round to 4.7
			As a reminder, the time 4.7s here = movement (to shore and to water) + 
				animations (shake finish primarily, as dig finish moreso impacts dig time already calculated)
				+ any slight server lag, user delay, and any other miniscule time slowdown
				
So, the final results, with constant factors supplied through (a small set of) manual tests we have
Luck Efficiency = 
		                  L * √(C) * .65
		-------------------------------------------------
		(2.1 * ⌈C / (mD * 1.5)⌉) + (.37 * ⌈C / mS⌉) + 4.7
		 ----------------------     --------------
				   sD                     sS
where:
	L = luck
	C = capacity
	mD = dig strength
	sD = dig speed (number, not percent [175% = 1.75])
	mS = shake strength
	sS = shake speed (number, not percent [175% = 1.75])

Additional flaw with previous equation -> assumes a 10% stat boost for 6* gear, this is not accurate
	e.g. Fossil Crown 5* luck = 250, Fossil Crown 6* luck = 260. This is a 4% increase
	All 6* gear has manually increased thresholds, the % is different per stat, so they'll have to be
		manually added in
	
SUMMARY


Luck Efficiency = (luck * sqrt(capacity)) / (time per pan)
	Time per pan = (time digging) + (time shaking) + constant1
		Time digging = (ceiling(capacity / (dig strength * 1.5)) / dig speed) * constant2
		Time shaking = (ceiling(capacity / (shake strength)) / shake speed) * constant3
		Constant1 = non-stat time per pan (animations, movement, lag, etc)
		Constant2 = conversion of dig speed to time-per-dig (in seconds)
					this also includes non-stat based time (animations, user action, lag, etc)
		Constant3 = conversion of shake speed to time-per-dig (in seconds)
					this also includes non-stat based time (animations, user action, lag, etc)
	We can calculate constant2 and constant 3 by doing x actions (dig/shake), and taking average
		then plugging in to get the factor
	We can plug this in (the whole denominator) and calculate constant 1 by doing x pans
		and taking the average, then pluggin in to get the factor
	I did some minor testing on 2 sets of equipment (slow speed and fast speeds) and averaged
		out to 2.1 for dig conversion, .37 for shake conversion, and 4.7s for additional pan time
		
Using my test results, Luck Efficiency = 
											  L * √(C) * .65
							-------------------------------------------------
							(2.1 * ⌈C / (mD * 1.5)⌉) + (.37 * ⌈C / mS⌉) + 4.7
							 ----------------------     --------------
									   sD                     sS
where:
	L = luck
	C = capacity
	mD = dig strength
	sD = dig speed (number, not percent [175% = 1.75])
	mS = shake strength
	sS = shake speed (number, not percent [175% = 1.75])
	
With this, we can run simulations on all possible equipment combinations
I'll include the results here

Some notes:
- This assumes all gear are 5* and 100%
	6* gear is NOT a 10% boost for each stat, if people provide me with screenshots of
		100% values for 6* I can run calculations for those instead
- This assumes you have the bonuses from the 4 stackable money based potions, and all quests
	Final builds are the same even without that assumption
- Enchantmants are fairly balanced, there is marginal difference between
	Infernal, Cosmic, Divine, Destructive, and Prismatic (Infernal allows for 2 apoc setup)
- Cryogenic Preserver beats out Fossil Crown by ~14%
	Whether or not this 14% is worth the money lost by not using Fossil Crown is up to individual
- Changing the constants has marginal difference on the final winning builds
	Modifying or removing them entirely occasionally allows for 1 prismatic or 1 solar
		to work with 7 mythrils, but overall is still the same (including the .65 luck constant)
- Forcing the script to limit rings to a max of 4 each shows that all combinations
	of apocs, solars, and prismatics all have very similar final stats
	I won't show all of these, but the winner was 1 apoc 3 solar (with infernal)
- This assumes no totems or meteor
	There is little to no change under totems and meteor (though the 2 apoc build no longer wins)
	
	