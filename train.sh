python3 scripts/oscillator_datagen.py -m FCA -n NWS -k 10
python3 scripts/oscillator_datagen.py -m FCA -n ER -k 10 
python3 scripts/oscillator_datagen.py -m FCA -n BA -k 10 
python3 scripts/oscillator_datagen.py -m FCA -n NWS -k 25 
python3 scripts/oscillator_datagen.py -m FCA -n ER -k 25 
python3 scripts/oscillator_datagen.py -m FCA -n BA -k 25 
python3 scripts/oscillator_datagen.py -m FCA -n NWS -k 35 
python3 scripts/oscillator_datagen.py -m FCA -n ER -k 35 
python3 scripts/oscillator_datagen.py -m FCA -n BA -k 35 
python3 scripts/oscillator_datagen.py -m FCA -n NWS -k 50
python3 scripts/oscillator_datagen.py -m FCA -n ER -k 50 
python3 scripts/oscillator_datagen.py -m FCA -n BA -k 50 

python3 main.py -m FCA -n NWS -k 10 -r 4 8 12 16
python3 main.py -m FCA -n ER -k 10 -r 4 8 12 16
python3 main.py -m FCA -n BA -k 10 -r 4 8 12 16
python3 main.py -m FCA -n NWS -k 25 -r 4 8 12 16
python3 main.py -m FCA -n ER -k 25 -r 4 8 12 16
python3 main.py -m FCA -n BA -k 25 -r 4 8 12 16
python3 main.py -m FCA -n NWS -k 35 -r 4 8 12 16
python3 main.py -m FCA -n ER -k 35 -r 4 8 12 16
python3 main.py -m FCA -n BA -k 35 -r 4 8 12 16
python3 main.py -m FCA -n NWS -k 50 -r 4 8 12 16
python3 main.py -m FCA -n ER -k 50 -r 4 8 12 16
python3 main.py -m FCA -n BA -k 50 -r 4 8 12 16
