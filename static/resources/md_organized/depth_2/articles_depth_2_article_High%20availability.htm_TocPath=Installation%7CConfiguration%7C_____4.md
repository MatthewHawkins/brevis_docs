# High availability

ê For older devices without support, this function requires the licensing of
the High Availability module.

i The options for this function can be found in the web interface under
**Configuration - High availability.**

## 1\. Configure the high availability

  1. Before you start configuring the high availability, you must either configure both gateways with a static IP address or set your DHCP service so that both gateways always have the same IP address.

The static IP address can be found under "Configuration -> Network".

**IMPORTANT NOTE:** Both gateways must be in the same network (VLAN).

  2. Activate the high availability and select a mode. Ensure that the same mode is activated for both devices.  
  

  3. Assign a virtual IP address from the network of the two SMS Gateways. The web interface will be available under this IP address.  
  

  4. Enter an SHA1 coded character string as secret. 
     * The secret is an alphanumeric string to identify cluster nodes to each other, the secret have to be 40 characters long
     * SHA1 Generator  
  

  5. Enter the IP address of the other SMS Gateway.  
  

  6. Enter the hostname of the other SMS Gateway.  
  

  7. Save your settings.  
  

  8. Restart both SMS Gateways.

* * *

## 2\. Example configuration

#### 2.1. Primary SMS Gateway (Master Node)

#### 2.2. Backup SMS Gateway (Slave Node)

ê For older devices without support, both SMS Gateways require identically
licensed modules so that the primary SMS Gateway can be fully replaced in the
case of a failure.

Related articles

  * Firmware Update

  * First steps 

  * Are there further modules for the SMS Gateway?

  * Help

  * High availability

  * How does high availability function?

  * How can I update the firmware of my SMS Gateway?

  * How do I get a license for my SMS Gateway?

  * Who can I ask if I need support?

  * I receive the message: "This is not a safe connection". What does this mean?

  * Upload license

