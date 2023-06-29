# %% Important imports
import board
import digitalio
import adafruit_max31865

import kkblinka

# %% Create pins
clk = digitalio.DigitalInOut(board.C0)
mosi = digitalio.DigitalInOut(board.C2)
miso = digitalio.DigitalInOut(board.C1)

cs0 = digitalio.DigitalInOut(board.C3)

# %% Prepare the sensor
spi=kkblinka.SPIBitBanger(clk, mosi, miso)

sensor0 = adafruit_max31865.MAX31865(spi, cs0)

# %% Start recording
while True:
   temperature0 = sensor0.temperature
   print(f'{temperature0}')
