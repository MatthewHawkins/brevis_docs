---
slug: cmd-api
---

# CMD API

To use the CMD API you first need a system user who is authorised to use the
API.

ê We recommend that you do not use the “admin” user here but that you create a
new user with restricted authorisations.

## Using the CMD API

```
The API can be addressed with the following: _https:// <SMS Gateway
IP>/commands.php_.
```

You can send data to this interface via POST or GET.

The following data are expected:

Parameter | Description  
---|---  
mode |  Mode in accordance with the following table. | Option | Description  
---|---  
halt | Use this option to shut down the SMS Gateway.   
reboot | Use this option to reboot the SMS Gateway.   
password | The user’s password.  
username  | System user authorised to access the HTTP API.  
  
## Example

https://192.168.1.1/commands.php?

username=systemuser&password=secret&mode=reboot

Related articles

  * Firmware Update
  * First steps 
  * Are there further modules for the SMS Gateway?
  * Help
  * Can I monitor the functions of the SMS Gateway?
  * How can I update the firmware of my SMS Gateway?
  * Incoming Messages
  * Monitor the SMS Gateway
  * Are there more powerful antennas for my SMS Gateway
  * Can my SMS Gateway receive and forward messages?
  * How do I get a license for my SMS Gateway?
  * What does the signal strength of the modem mean?
  * CMD API

  * I receive the message: "This is not a safe connection". What does this mean?
  * Upload license

