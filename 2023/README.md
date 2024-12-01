# advent-of-code-2023

## Day 1
Nothing to note in particular. As with all these puzzles, I take a "get things done" approach vs. efficiency

## Day 2
I had a facepalm moment with the first puzzle when I initially computed the sum of IDs of games that were not possible. I corrected it very inelegantly, but pretty fast though 

## Day 3
Probably could have done some optimisation and elimidate some boilerplate, but it gets stuff done!

## Day 4
One strategy I have been following for the past few days is to trial-run my solution on the toy example provided with each problem. That has proven effective as it avoided me to "debug in production" :-D.

For the first time also, I have been re-using a function accross the 2 puzzles

## Day 5
I added a small utils module to load test or "real" data

Puzzle 2 took me a bit more of time, until I realise that the `l(s)` as `location` function of `seed` is a piecewise linear function of slope 1 and varying intercept. From there it was a piece of cake to find a way to check all lower bounds of the input spaces and run function on them, instead of brute-forcing it

## Day 6
Not very challengind day, but sometimes it's good ;-)

## Day 7
This one took me longer than I expected. Maybe I'll skip day 8, maybe not...

## Day 8
I was able to brute-force the first puzzle, but not the second. I didn't notice that cycle were forming there, and Reddit gave me the LCM hint :shame:

## Day 9
Nothing special to say here, solution was pretty self evident

## Day 10
I have done puzzle 1 so far, and will ponder over puzzle 2. I'm contemplating giving up on AoC for this year to be honnest, I am already 1 day behind, and I am not sure I am willing to put in the time and thinking anymore. Let's wait and see...

Oh, also on puzzle 1, this was simply solved with a `Pipe` class allowing to got through the graph step by step, counting lenght covered. No biggie, but still involved effort. 