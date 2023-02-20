# Introduction

The python script `jugs` solves the water jugs problem using search algorithms,
namely *depth-first* and *breadth-first* search

In [Die Hard III](https://www.youtube.com/watch?v=2vdF6NASMiE) the bad guy
threatens to explode a bomb if the *water jugs* problem is not solved. In the
movie, there are two jugs, with a maximum capacity of 3 and 5 gallons each. Both
are initially empty and the goal is to find a sequence of operations that leaves
exactly four gallons of water in one of the jugs (obviously, in the larger one,
since the smaller could not accomodate a volume larger than its maximum
capacity). The only allowed operations are either to empty a jug, to fill it up
to its maximum capacity or to pour water from one jug to the other. To stop
these threats once and for all, a solution to any variant of the water jugs
problem is given here. Well, the only condition preserved is that there are
still two jugs, so maybe future bad guys create other instances with more jugs!

# Dependencies #

`jugs` has no  dependency with any third-party packages.

# Installation #

`jugs` is provided *as is*. Thus, it has not been configured to be used with any
package installer. To give it a try, just simply clone this repo with:

``` sh
    $ git clone https://github.com/clinaresl/water-jugs
```

Next, go to the directory `water-jugs/` and try any of the [examples](#examples)
provided below.

# Usage #

`jugs` has only one mandatory argument, `--algorithm`. Choices are `depth-first`
or `breadth-first`. Other arguments serve to the purpose of posing different
variants and are optional:

* `--small`, `--large`: set the maximum capacity of either the small or large
  jug respectively. By default, 3 and 5
  
* `--small_initial`, `--large_initial`: set the initial volume used in the small
  and large jug. By default, 0
  
* `--target`: set the target volume in one of the jugs. By default, 4

# Examples #

To solve the original problem, try:

``` sh
    $ ./jugs.py --algorithm depth-first
    (0, 0) -- (3, 0) -- (3, 5) -- (0, 5) -- (3, 2) -- (0, 2) -- (2, 0) -- (2, 5) -- (3, 4)
    Elapsed time: 0.001 seconds
```

using *depth-first* search. To use *breadth-first* search:

``` sh
    $ ./jugs.py --algorithm breadth-first
    (0, 0) -- (0, 5) -- (3, 2) -- (0, 2) -- (2, 0) -- (2, 5) -- (3, 4)
    Elapsed time: 0.001 seconds
```

which produces a solution path no larger than the solution found with
*depth-first*. The reason is that *breadth-first* search produces optimal
solutions in this domain because the cost of each operator is the same,
cannonically equal to one, so that solutions at depth *d* have a cost precisely
equal to *d* indeed.

The effect of *depth-first* search finding ridiculously long sequences becomes
apparent when slightly modifying the problem to consider that the jugs initially
contain some volume of water. Say the smaller contains 1 gallon and the larger 3
gallons originally. Compare the solutions found:

``` sh
    $ ./jugs.py --algorithm depth-first --small_initial 1 --large_initial 3 
    (1, 3) -- (0, 3) -- (0, 0) -- (3, 0) -- (3, 5) -- (0, 5) -- (3, 2) -- (0, 2) -- 
    (2, 0) -- (2, 5) -- (3, 4)
    Elapsed time: 0.001 seconds
    
    $ ./jugs.py --algorithm breadth-first --small_initial 1 --large_initial 3 
    (1, 3) -- (0, 4)
    Elapsed time: 0.000 seconds

```

Both algorithms are *complete*, meaning that they find a solution, provided that
any exists. If not, they exit without finding a solution. Say for example that
the target volume exceeds the capacity of both jugs. To exemplify the usage of
all other options, an entirely different case is proposed next where the
capacity of each jug, the initial volume and the target volume have been
modified ---note the target volume is larger than the maximum capacity of any
jug and thus the instance is unsolvable, yet both algorithms detect this case:

``` sh
    $ ./jugs.py --algorithm depth-first --small 10 --large 16 --small_initial 1 --large_initial 3 
                --target 20  
    No solution found!
    Elapsed time: 4.632 seconds
    
    $ ./jugs.py --algorithm breadth-first --small 10 --large 16 --small_initial 1 --large_initial 3 
                --target 20  
    No solution found!
    Elapsed time: 4.675 seconds

```

# Remarks #

The purpose of this repository is to provide a didactical example of how to
implement *brute-force* search algorithms. Thus, a few remarks are done below
for the sake of clarity/readability:

1. The source code is crowded of comments. Hope it becomes clear that
   *programming* is entirely different of *coding*. While there is no
   intellectual exercise in the latter, it really requires to be heavily
   experienced for doing the former correctly. Comments help to understand all
   the way from *programming* (mentally devising an algorithm that solves the
   problem at hand) to *coding* ---just telling the computer, the dumbest of all
   devices how to do things specifying very clearly every single step to take.
   
2. In *breadth-first* search, customary practice is to store *backpointers* in
   the *closed* list to recover the solution path once the goal is about to be
   expanded ---or generated even! This is not done here and the *closed* list is
   implemented as a linear set over instances of states (named `JUGState` in
   this implementation). Thus, to be able to get the solution path, every state
   carries a copy of the path from the start state to it. This is horrible!! and
   this should be avoided in general. In this case, because the state space is
   tiny (even for larger maximum capacities of both jugs), and because
   didactical means are above efficient coding, that measure has been adopted
   but the interested reader should be warned that this is never done in true
   commercial efficient implementations.
   
3. As noted in the comments also, *breadth-first* search is generally
   implemented with a *priority queue*, just a sorted list that insert nodes in
   ascending order of their cost. In this specific case, all operators have the
   same cost (and thus it is usually said that this is a *unit domain*), so that
   a plain list suffices. However, general implementations of algorithms such as
   *Dijkstra* or *uniform cost search* would require sorting nodes in ascending
   order of their cost.
   
4. Other than this, the implementation has been designed to be easy to extend,
   modify, etc. Feel free to use this code, to copy it, to make pull requests,
   or whatever

# Author #

Carlos Linares Lopez <carlos.linares@uc3m.es>  
Computer Science Department  
Universidad Carlos III de Madrid

