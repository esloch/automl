import time


spaces = ( "  " )

for position in range(50):
    with open('drawings/marc.txt') as f:
        object_ = f.read().strip()
    print(f'{spaces * position}{object_}', end='\r')
    time.sleep(.1)
