# Monitor the SMS Gateway

The SMS Gateway offers a status page from which information may be obtained:
_http:// <IP Adresse Gateway>/check.php?option=<option> (the option parameter
is optional, you will have all values if you leave it out)_

You can have this monitored by your monitoring system using a check_http for
example.

## The options at a glance

Option | Description  
---|---  
disk | Specifies how much internal memory is occupied (bytes).   
failed | Number of messages which could not be sent.   
load | Indicates the loading of the SMS Gateway.   
que | Specifies how many messages are in the queue.   
signal  |  Specifies the signal strength. No number is returned if there is a modem fault.   
state |  Specifies the Simcard status: | Output | Description  
---|---  
SIM_NOT_INSERTED  | Simcard not inserted   
NO_SIGNAL  | No available Signal   
SIGNAL_OK  | Good Signal   
SIGNAL_WARNING  | Signal is weaker than -89 dB   
SIGNAL_TOO_WEAK  | Signal is weaker than -99 dB   
time |  Returns a Unix timestamp. To monitor the system time of the SMS Gateway.   
total | Specifies how many messages the gateway has sent in total.   
uptime | Specifies how much time has passed since the last reboot of the SMS Gateway.   
  
## Plug-in for Icinga and Nagios

There is already a ready to use plug-in for Icinga and Nagios using which you
can monitor your SMS Gateway. The plug-in is here.

Related articles

  * Can I automate the sending of text messages?
  * Can I automate the sending of text messages?
  * Can I connect my SMS Gateway to Centreon?
  * Can my SMS Gateway send notifications from Check_MK?
  * Can I connect my SMS Gateway to Nagios, Icinga 1 or Icinga 2?
  * Can I connect my SMS Gateway to SNAG-View? 
  * Can I connect my SMS Gateway to Zabbix?
  * Can I monitor the functions of the SMS Gateway?
  * How can I import checks into integrated monitoring?
  * Messages Status
  * Monitor the SMS Gateway
  * HTTP API
  * Firmware Update
  * How can I update the firmware of my SMS Gateway?
  * Help

