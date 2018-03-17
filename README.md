# Tank-Raspberry-pi-3
Tank-Raspberry-pi-3 is an tank with remote controle.<br>

###### The vehicle
This is a raspberry pi 3 with a L293D as motor driver, a NRF24L01 for remote controle and an U-blox neo 6M for GPS.<br>

###### Radio control
* Atmega328P-20PU
* 2 joystick
* switch button...

### connection

##### NRF24L01
* VIN   -> 3.3V
* GND   -> GND
* CSN   -> SPI0 CS0 (GPIO 08)
* CE    -> GPIO25
* MOSI  -> MOSI (GPIO10)
* SCK   -> SCK  (GPIO 11)
* MISO  -> MISO (GPIO9)
* IRQ   -> Nothing

##### L293D
* coming...
