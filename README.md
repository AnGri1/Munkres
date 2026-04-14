To understand the Munkres algorithm I created a short article on medium dedicated to this.
The use case was in that context about football players and roles on the pitch.
Assuming every player can play in any role but with different performances the objective of the algorithm is
to find the best association of player with roles maximizing the performances overall.

Maximizing is the inverse of minimizing but the logic is the same.

https://andrea-grianti.medium.com/the-hungarian-algorithm-a-use-case-for-football-managers-2527ad3097ef

In that specific context the problem is much more complex because there are also constraints that the algorithm does not take into account (i.e. 
number of players =11, modules and so on.)

The example you can find in this sample python program is based on a random generated matrix where rows are resources 
and columns are the different "dimensions" whose values need to be minimized (or maximized).

The library is a open source python library: from munkres import Munkres

Kind regards Andrea Grianti

