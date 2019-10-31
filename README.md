# pihole-oled

<p align="center"><img src="./res/pihole-oled-demo.gif"></p>

## Hardware

The OLED display is connected _via_ I2C with 4 wires: `SDA`, `SCL`, `3.3V` and
`GND`.

## Installation

:warning: This project requires a Raspberry/Orange Pi with
[Pi-hole](https://pi-hole.net/) installed, the I2C bus
enabled and Python 3.

### Software requirements

Installing the following packages on debian/ubuntu:

```
sudo apt-get install python3-pip python3-setuptools python3-wheel python3-dev zlib1g-dev libfreetype6-dev libjpeg-dev build-essential libopenjp2-7 libtiff5 i2c-tools libi2c-dev
```
### Project installation

Clone this project:

```
git clone https://github.com/mattfrazer/pihole-oled.git /opt/pihole-oled
```

Install luma with pip3:

```
sudo -H pip3 install --upgrade luma.oled
```

Connect the OLED display and run the command below, you should see some
information on the display:

```
python3 pihole-oled.py
```

You can exit the script with <kbd>ctrl</kbd>+<kbd>c</kbd>.

### Systemd configuration

You can install a `systemd` service by copying the provided configuration file
using the command below. This service will automatically run the python script
mentioned in the previous section on boot:

```
sudo cp pihole-oled.service /etc/systemd/system/
```

Enable, then start the `pihole-oled.service`:

```
sudo systemctl enable /etc/systemd/user/pihole-oled.service
sudo systemctl start pihole-oled.service
```

## License

This project is released under the MIT License. See the bundled [LICENSE
file](./LICENSE) for details.
