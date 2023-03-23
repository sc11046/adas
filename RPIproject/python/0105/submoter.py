import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# 핀 설정
seg = [11,13,15,19,21,23,29,31] # GPIO pin
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
fnd = [(1,1,1,1,1,1,0,0), #0
    (0,1,1,0,0,0,0,0), #1
    (1,1,0,1,1,0,1,0), #2
    (1,1,1,1,0,0,1,0), #3 
    (0,1,1,0,0,1,1,0), #4
    (1,0,1,1,0,1,1,0), #5
    (1,0,1,1,1,1,1,0), #6
    (1,1,1,0,0,1,0,0), #7
    (1,1,1,1,1,1,1,0), #8
    (1,1,1,1,0,1,1,0)] #9
    
def main():
    duty_ratio= 0
    MaxDuty= 12
    PWMpin= 12
    # GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PWMpin, GPIO.OUT) 
    Servo=GPIO.PWM(PWMpin, 50) 
    Servo.start(0)
    print('Wating for 1 sec') 
    time.sleep(1) 
    print('Rotating at interval of 0-12 degrees')
    while duty_ratio <= MaxDuty:
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
        duty_ratio+= 1
        for i in range(duty_ratio):
            GPIO.output(seg,fnd[i])
    if duty_ratio > MaxDuty:
        duty_ratio= 0
        Servo.ChangeDutyCycle(duty_ratio)
        Servo.stop()
        GPIO.cleanup()
        
        print('Everythings cleanup')
if __name__ == '__main__':
    main()