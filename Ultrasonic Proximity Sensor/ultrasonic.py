import time
import RPi.GPIO as io

io.setmode(io.BCM)
io.setup(24,io.IN)
io.setup(23,io.OUT)

while True:
    pulse_start=0
    pulse_stop=0
    duration=0
    distance=0
    io.output(23,io.LOW)
    time.sleep(.1)
    io.output(23,io.HIGH)
    time.sleep(0.000010)
    io.output(23,io.LOW)
    
    while io.input(24)==0:
        pulse_start=time.time()
        
    while io.input(24)==1:
        pulse_stop=time.time()
        
    duration = pulse_stop - pulse_start
    
    distance=duration*17150.0
    distance=round(distance,1)
    print("distance: "+ str(distance))
    
    time.sleep(0.2)
    