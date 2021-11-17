#   Particles in a box

##  Usage

Open a new terminal on the installation directory of your choice, then clone the repository using:

```
git clone
```

Then go to the project folder and follow the execution instructions.

```
cd PyColloid
```

Make sure you are working with the provided ``virtualenv`` activated. For that, type:

```
source venv-simulation/bin/activate
```

For executing the simulation just execute the shell script ``RUN.sh`` by typing:

```
./RUN.sh
```

You can change the parameters of the simulation by changing the [Parameters.txt](src/Parameters.txt) file. This file its by itself very self-explanatory but here is a bit of documentation:

*   **Case:** Select the method of sorting the initial state by choosing the scenario *HighAPF* (high atomic packing factor), or *LowAPF* (low atomic packing factor).
*   **Particles:** Number of particles on the simulation.
*   **Mass:** Mass of each particle (useless).
*   **Charge:** Charge of each particle (useless).
*   **Radius:** Radius of each particle (useless).
*   **BoxX:** *x* length of the box.
*   **BoxY:** *y* length of the box.

Maintain the dimensions of the box in a way that the atomic packing factor doesn't go over *0.7*^[1].

^[1]: Consult [this article](https://en.wikipedia.org/wiki/Atomic_packing_factor) for more information on *APF*.
