# PocketCube
An extremely fast python library to explore the search space of the Rubik's Pocket Cube (2x2x2).
The code is optimized and uses one core, but it can be parallelized easily to make it even faster.


## How to

In order to find all configurations (states) of the [Pocket Cube](https://en.wikipedia.org/wiki/Pocket_Cube) that can be reached by scrambling it with up to 15 moves (quarter turns, that is, only 90 degrees face rotations):
```
time pypy solve_pocketcube.py 15 > all_results.txt
```
This will only take approx **30 seconds** on a i7 laptop (*Intel(R) Core(TM) i7-3537U CPU @ 2.00GHz*) with PyPy 5.1.2 with GCC 5.3.1.
You can also run it on standard CPython:
```
time python solve_pocketcube.py 15 > all_results.txt
```
It will take approx 3 minutes on the same machine running Python 2.7.12.
<!--It will take approx 3 minutes on a i7 laptop (*Intel(R) Core(TM) i7-3537U CPU @ 2.00GHz*), approx 2 minutes on a i5 desktop (*Intel(R) Core(TM) i5-2400 CPU @ 3.10GHz*).--> 
The file in output will be about 150Mb in size, containing all the scramblings with the moves to obtain each scrambling from the solved state.

Then run: 
```
wc -l all_results.txt
```
to know the number of all possible states of the pocket cube.

The following command:
```
cat all_results.txt | grep -E "( [^ ]+){14}"
```
will show the list of 276 most difficult scramblings of the pocket cube with the corresponding [God's Algorithms](https://en.wikipedia.org/wiki/God%27s_algorithm) (for further info, see [Optimal solutions](https://en.wikipedia.org/wiki/Optimal_solutions_for_Rubik's_Cube)).

The first number represents the state in an internal coding (see source code comments for more info), followed by the sequence of moves in [Singmaster notation](https://en.wikipedia.org/wiki/Rubik%27s_Cube#Move_notation) to reach that state from the solved state.

## Notes
The pocketcube library has been designed and developed from scratch by [Maurizio Atzori](http://swlab.unica.it/atzori), [Dept. Maths/Computer Science](http://dipartimenti.unica.it/matematicaeinformatica/), (University of Cagliari, Italy), on Dec 20, 2016.
If you find it useful, I'd be glad to know it.

