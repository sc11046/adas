import smbus
import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
    
PinTrig=10
PinEcho=8
PWMpin= 12
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
# Define some device parameters
I2C_ADDR = 0x3f# I2C device address
LCD_WIDTH = 16 # Maximum characters per line
# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_BACKLIGHT = 0x08 # On
#LCD_BACKLIGHT = 0x00 # Off
ENABLE = 0b00000100 # Enable bit
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
#Open I2C interface
#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1
def lcd_init():
    # Initialise display
    lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction

    lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 

    lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size

    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
    time.sleep(E_DELAY)
def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = the data
    # mode = 1 for data and 0 for command
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

# High bits
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
# Low bits
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)
def lcd_toggle_enable(bits):
# Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
    time.sleep(E_DELAY)
def lcd_string(message,line):
    # Send string to display
    message = message.ljust(LCD_WIDTH," ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)
        
def main():
    
    lcd_init() 
    startTime=0
    stopTime=0  
    GPIO.setup(PinTrig, GPIO.OUT) 
    GPIO.setup(PinEcho, GPIO.IN)
    GPIO.setup(PWMpin, GPIO.OUT) 
    Servo=GPIO.PWM(PWMpin, 50) 
    Servo.start(0)          
    while True:  
        GPIO.output(PinTrig, False) 
        time.sleep(2)
        # trigger
        print ('Calculating Distance. 1 nanosec pulse')
        GPIO.output(PinTrig, True) 
        time.sleep(0.00001) 
        GPIO.output(PinTrig, False) 
        # echo
        while GPIO.input(PinEcho) == 0: 
            startTime = time.time()
        while GPIO.input(PinEcho) == 1: 
            stopTime = time.time()
        Time_interval= stopTime - startTime
        Distance = Time_interval * 17000
        Distance = round(Distance, 2)
        print ('Distance => ', Distance, 'cm')
        if Distance < 3 : 
            lcd_string("open door",LCD_LINE_1)
            Servo.ChangeDutyCycle(3)
            time.sleep(2)
            marks = [3,2,1]            
            for i in marks :
                GPIO.output(seg,fnd[i])
                time.sleep(1)
            lcd_string("close door",LCD_LINE_1)
            time.sleep(1)
            
        else :
            Servo.ChangeDutyCycle(0)
            Servo.stop()
            GPIO.cleanup()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
      pass
    finally:
        lcd_byte(0x01, LCD_CMD)