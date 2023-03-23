import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
LED = 11 # PWM pin
# 듀티비 목록 작성
# 출력 핀으로 설정, 초기출력은 로우레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
# PWM 객체 인스턴스 작성
PWM_led = GPIO.PWM(LED,GPIO.HIGH)
# PWM 신호 출력
PWM_led.start(0)
try:
    while 1:
        Duty_ratio= input('Enter Brightness (0 to 100):')
        duty= int(Duty_ratio)
        print('Duty rate: ',duty)
        # ChangeDutyCycle(rate) 함수는 duty cycle 변경 rate= 0-100
        PWM_led.ChangeDutyCycle(duty)   
# 키보드 예외 검출
except KeyboardInterrupt:
# 아무 것도 안함
    pass
finally:
    PWM_led.stop() # PWM 정지
    GPIO.cleanup()