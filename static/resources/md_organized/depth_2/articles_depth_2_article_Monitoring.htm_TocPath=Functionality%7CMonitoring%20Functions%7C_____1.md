# Monitoring

ê This function requires the licensing of the _Monitoring_ module.

i An overview of integrated monitoring is to be found in the web interface
under **Configuration - Monitoring**.

Configure checks which check your system at a _Time interval of 5 minutes_ and
reliably report failures:

## Checks

#### Options for all checks

Option | Description  
---|---  
**Name** | Give your check a name.  
Notification group  |  _Select a group of contacts which are to receive notifications._ If the monitoring system of your SMS Gateway notices a failure, a group of contacts will be alerted by text message or by "Automatic". The monitoring group is intended for this purpose as standard. After the failure has been cleared the SMS Gateway will send a recovery message.  ê If you have licensed the Recipient groups module, you have the option to notify further groups.  
Shipping option  |  _Select the shipping option of the notifications._ The monitoring system provides two different shipping options: "Only SMS" and Automatic". Automatic trys to deliver the notification via Telegram, if it fails the notification will be delivered by text message. ê Licensing for the Telegram module is required. This licensing is free of charge for support customers. Please contact sales@brevis.one.  
  
#### Available Checks

Name of the check |  **Arguments**  
---|---  
CheckHTTPAuth To monitor websites with HTTP authentication |  **Website** _Enter the website to be monitored, e.g.: http://www.brevis.one/secure_ User name _Enter the user name which is to be used for logging in_ **Password** Enter the _password_ for the user  
CheckHTTP To monitor websites |  **Website** _Enter the website to be monitored, e.g.: http://www.brevis.one_  
CheckPort To monitor the reachability of services |  **Host** _Enter the host to be monitored: 192.168.1.254 or www.brevis.one_ **Port** _Enter the port which is to be monitored, e.g.: 80_ **Timeout** _Enter the timeout for the reachability of the port_  
Ping To monitor availabilities |  **Host** _Specify the host to be monitored, e.g.: 192.168.1.254 or www.brevis.one_ Number of pings _Enter the number of ICMP Echo Requests per check interval to be set_ **Timeout** _Enter the timeout for the individual ICMP Echo Requests_  
  
### Re-notification time

The re-notification time is the time interval in minutes after which a new
alert is sent if a failure lasts longer.

### Maximum amount checks

The SMS Gateway Monitoring allows to have up to 200 individual checks.

### Example

  

➯ Click the Export button to save your settings, e.g. before a Firmware
update.

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

