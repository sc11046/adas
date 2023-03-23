import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# 사용할 핀번호 대입. 핀은 사용자에 맞게 조절
LED= 11
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(LED, GPIO.OUT)
PWM_LED= GPIO.PWM(LED, 50) # Hz
PWM_LED.start(0) # 초기 duty rate 값 0-100
try:
    while True: 
        Duty_led= input('Enter Brightness (0 to 100):')
        duty= int(Duty_led)
        print('Duty rate: ',duty)
        # ChangeDutyCycle(rate) 함수는 duty cycle 변경 rate= 0-100
        PWM_LED.ChangeDutyCycle(duty)
finally:
    PWM_LED.stop()
    print('Cleaning up!') 
    GPIO.cleanup()