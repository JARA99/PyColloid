#   Particles in a box

A simple simulation of a group of particles in a box, with electromagnetic interactions. As an output you will get two files, a *png* with the first and last state, and a *gif* with the temporal evolution.

![](output/output.gif)

##  Usage

Open a new terminal on the installation directory of your choice, then clone the repository using:
 
```
git clone
```

Then go to the project folder and follow the execution instructions.

```
cd PyColloid
```

For executing the simulation just execute the shell script ``RUN.sh`` by typing:

```
./RUN.sh
```

You can change the parameters of the simulation by changing the [Parameters.txt](src/Parameters.txt) file. This file its by itself very self-explanatory but here is a bit of documentation:

*   **Case:** Select the method of sorting the initial state by choosing the scenario *HighAPF* (high atomic packing factor), or *LowAPF* (low atomic packing factor).
*   **APF:** Set a fixed APF, this will rewrite the number of particles, you can turn it off by tying -1.
*   **Particles:** Number of particles on the simulation.
*   **Mass:** Mass of each particle.
*   **MaxCharge:** Maximum charge of each particle.
*   **MinCharge:** Minimum charge of each particle.
*   **MaxRadius:** Maximum radius of each particle.
*   **MinRadius:** Minimum radius of each particle.
*   **MaxX:** *x* length of the box.
*   **MinY:** *y* length of the box.
*   **ForceConstant:** Parameter k used on Coulumbs law.
*   **DeltaTime:** Time of each evolving interval.
*   **Iterations:** Total of DeltaTime iterated.
*   **CollisionLoops:** Maximum iterations for calculating a collision.
*   **Palette:** Palette used for coloring the charge, you can use any of the ones listed [here](Palettes.png).
*   **Invert:** Invert the palette on plot.

Remember you can choose the palette of your choice from this list:

![](Palettes.png)


<!-- Maintain the dimensions of the box in a way that the atomic packing factor doesn't go over *0.7*.[^1]

[^1]: Consult [this article](https://en.wikipedia.org/wiki/Atomic_packing_factor) for more information on *APF*. -->



##  To Do

- [x] Program [InitialValues.py](src/InitialValues.py)
- [x] Program [TemporalEvolution.py](src/TemporalEvolution.py)
- [x] Program [CollisionDetector.py](src/CollisionDetector.py)
- [x] Program [CollisionDynamics.py](src/CollisionDynamics.py)
- [x] Program [main.py](src/main.py)
- [x] Program the plotter base
- [x] Finish the plotter  

<!-- Fork the repository for collaboration, then send your pull requests. -->