python3 scripts/oscillator_datagen.py -m FCA -n Caltech -k 10
python3 main.py -m FCA -n Caltech -k 10 -r 4 8 12 16
python3 plotting/plot_factors.py -m FCA -n Caltech -k 10

python3 scripts/oscillator_datagen.py -m FCA -n PowerGrid -k 10
python3 main.py -m FCA -n PowerGrid -k 10 -r 4 8 12 16
python3 plotting/plot_factors.py -m FCA -n PowerGrid -k 10

python3 scripts/oscillator_datagen.py -m FCA -n Caltech -k 25
python3 main.py -m FCA -n Caltech -k 25 -r 4 8 12 16
python3 plotting/plot_factors.py -m FCA -n Caltech -k 25

python3 scripts/oscillator_datagen.py -m FCA -n PowerGrid -k 25
python3 main.py -m FCA -n PowerGrid -k 25 -r 4 8 12 16
python3 plotting/plot_factors.py -m FCA -n PowerGrid -k 25

python3 scripts/oscillator_datagen.py -m FCA -n Caltech -k 35
python3 main.py -m FCA -n Caltech -k 35 -r 4 8 12 16
python3 plotting/plot_factors.py -m FCA -n Caltech -k 35

python3 scripts/oscillator_datagen.py -m FCA -n PowerGrid -k 35
python3 main.py -m FCA -n PowerGrid -k 35 -r 4 8 12 16
python3 plotting/plot_factors.py -m FCA -n PowerGrid -k 35
