# Chaos Game
Something-something-something Chaos Theory

The Chaos Game is a zero-player game, in that it is just a set of rules to play out, rather than an interactive program (as one would expect of a game)
The idea is that you select any n-number of points, and place them in space. Then, starting at another random point, you jump from that location to a point that is halfway between it and one of the initial n points. At this halfway point, you draw a dot, and repeat the process from your new current position.
This implementation has just 3 points -- colored red, green, and blue -- but they are a list, and could be grown to any n-number of target points. They are also colored, and the halfway destination point is colored to match.

Modification Ideas:
Interpolation of color based on range to the target points
New color based on average/interp. of target color & previous color(s)
Parameterized target points (count, location, and color)
Actually account for the need to move in a negative direction instead of just dividing everything by 2 like a hack (!!!)

This code is a bit of a mess, and the initial implementation I made had been tweaked and broken. This is my "fixed" version. "Fixed" because it is just 59 lines of actual code and I've still managed to create an unnecessary class.
