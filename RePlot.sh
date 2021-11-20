#!/bin/sh

# source venv-simulation/bin/activate

cd src/
python3 replot.py
gnuplot PlotCopy.gp
