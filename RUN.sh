#!/bin/sh

source venv-simulation/bin/activate

cd src/
python3 main.py
gnuplot PlotCopy.gp
