import board
from digitalio import DigitalInOut
import adafruit_character_lcd.character_lcd as characterlcd

lcd_rs = DigitalInOut(board.GP7)
lcd_en = DigitalInOut(board.GP6)
lcd_d4 = DigitalInOut(board.GP22)
lcd_d5 = DigitalInOut(board.GP26)
lcd_d6 = DigitalInOut(board.GP27)
lcd_d7 = DigitalInOut(board.GP28)

lcd_columns = 16
lcd_rows = 2

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

lcd.cursor = True
lcd.blink = True
lcd.message = "Hello\nCircuitPython!"
