# Dump the first 256 bytes of the I2C device located at 0x50
i2cdump -y 1 0x50

# Scan and list I2C devices
i2cdetect -y 1

# Use eeprog to read 2048 bytes from an I2C eeprom chip, and print the contents as hex
./eeprog -x /dev/i2c-1 0x50 -r 0x0:0x800

# Use eeprog to read 2048 bytes from an I2C eeprom chip, and write the contents to file
./eeprog -o example.bin /dev/i2c-1 0x50 -r 0x0:0x800

# Use flashrom to detect an SPI device
flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=512 -V

# Use flashrom to write the contents to an SPI device to file
flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=2000 -r example.bin
