reset

set size ratio -1
load 'gnuplot-palettes/paired.pal'
set palette positive

set terminal gif enhanced font Arial 12 animate delay 1 size 752,640
set datafile separator ","
set output '../output/output.gif'

set key autotitle columnhead
stats 'output.csv' nooutput
unset key

set xrange [0:0.8]
set yrange [0:0.8]
set grid
# unset tics

do for [i=2:int(STATS_blank)] {
    plot 'output.csv' every :::i::i using 5:6:4:3 with circles fs solid lc palette
}

set terminal png enhanced font Arial 12 size 1504,640
set output '../output/output.png'

set multiplot layout 1,2
# set key

# set size 0.5,0.5
# set origin 0,0
set title 'Distribución inicial'
plot 'output.csv' every :::2::2 using 5:6:4:3 with circles fs solid lc palette #t 'Start'

# set size 0.5,0.5
# set origin 0.5,0
set title 'Distribución final'
plot 'output.csv' every :::int(STATS_blank)::int(STATS_blank) using 5:6:4:3 with circles fs solid lc palette #t 'Stop'
unset multiplot