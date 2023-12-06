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