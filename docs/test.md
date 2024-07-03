[![EN](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)](#) [![DE](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)](#)

You are here: [Installation](#) > [Setting Up the Gateway](#) > [First steps](#) > DX1 Edition - Quick Start Guide

# Desktop Extended Edition (DX1) - Quick Start Guide

## Scope of delivery

- brevis.one SMS Gateway - DX Edition
- Power supply unit
- CISCO RS 232 cable
- Antenna
- Rack-mount-brackets

[![Scope of Delivery](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)](#)

## brevis.one SMS Gateway

**Front:**

![Front](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)

**Back:**

![Back](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)

## 1. Rack mounting

- With the included rack-mount-brackets, the gateway can be easily mounted in the rack.

![Rack Mounting](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)

## 2. Insert the SIM card

**IMPORTANT:** Before inserting the SIM card, please remove the PIN from the SIM card and disconnect the gateway from the power. Here you should wait 2 minutes until the capacitors have discharged and you insert the SIM card. This also applies if you change the SIM card! Check whether the SIM is correctly engaged. A clicking noise must be audible.

- Insert the SIM card (Standard SIM).

![SIM Insert](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)

## 3. Screw on the antenna

- Screw the antenna to the SMA connector.

## 4. Connect network and console cable RS232

- Connect an RJ-45 network cable. Please use the Ethernet port ETH0. The ports ETH1 and ETH2 are without function!
- Connect the console cable to the serial port to be able to connect via PUTTY.

## 5. Connect the power cable

- Connect the power cable to the device. The power indicator will now light up.

## 6. Network configuration

- If your network has a DHCP server, the DX Edition can be assigned an IP address. If no DHCP is available, the device starts with the default IP: 192.168.1.1
- If you do not know the IP address assigned by DHCP, you can query it via the Console RS232 port. To do this, connect your PC to the gateway using a terminal program (e.g.: PUTTY) and the CISCO console cable.
- The speed of the interface is 115200 baud (8N1).

![Putty](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)

- Click on the *Open* Button and press *Enter*.
- A text-based interface appears in which the current IP address is shown under the Version menu option. The IP address can be altered as you wish under the Network menu option.

![Com2 Putty](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)

- If you make the network settings using the serial port, they will only be temporary and will be lost when the Gateway is restarted.
- Permanent network settings should be made in the web interface.
- You can now access the web interface via the IP address. Log in here with the following information:
  - User name: **admin**
  - Password: **admin**

## 7. Licensing

![Licensing](https://docs.brevis.one/current/en/Skins/Fluid/Stylesheets/Images/logo-brevis.one-white_229x55.png)

- After logging into the web interface, you must request a licence for your Gateway. As long as this process has not been completed you will constantly be requested to do so after logging in.
- For this purpose, please complete the form and press on the Request button. The Serial number you will find on the Gateway ([Where can I find the serial number of my SMS Gateway?](#)).
- You will then receive a licensing request which you can request through the Servicedesk ([https://brevis.one/en/licreq.html](https://brevis.one/en/licreq.html)).
- After our licensing team has processed the request, you will receive a licensing file which you should upload at this point to the SMS Gateway.

## 8. SIM card

**Warning:** Before inserting the SIM card, enter the correct PIN on the Gateway. If you do not do this, the SIM card could be locked. Even if no PIN is set up on the card, you should check the preferences. We suggest not using a PIN to avoid problems with SMS routing.

- Select SIM card from the Configuration menu option.
- Enter the PIN of the inserted SIM card here.
- Select Reboot / shut down from the Configuration menu option.
- Restart the SMS Gateway.

## 9. Send a test message

- Enter the IP in your browser and log in again.
- Then select send to number from the SMS menu option.
- You can now send a text message on the screen which then appears by entering a telephone number and a message.
- Further assistance is provided in the Help menu option.

**Related articles**

- [Firmware Update](#)
- [First steps](#)
- [Are there further modules for the SMS Gateway?](#)
- [Who has access to software updates?](#)
- [Help](#)
- [How can I update the firmware of my SMS Gateway?](#)
- [How do I get a license for my SMS Gateway?](#)
- [Who can I ask if I need support?](#)
- [I receive the message: "This is not a safe connection". What does this mean?](#)
- [Upload license](#)
- [Technical Specifications](#)
- [Support Informations](#)
