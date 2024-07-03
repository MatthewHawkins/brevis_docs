---
slug: sim-card
---

# SIM Card

ê We recommend that the SMS Gateway is switched off before the SIM card is
replaced. We do not recommend to use multi sim cards.

i The settings for the SIM card are provided in the web interface under
**Configuration - SIM card**.

❕ The SMS Gateway requires a Mini-SIM card. You will require an adapter for
smaller formats. See picture below.

Furthermore old SIM card models should not be used since the functionality can
not be guaranteed using them.

Option | Description  
---|---  
PIN |  Secret number Enter the PIN of your SIM card here. Only then should you insert the SIM card in the SMS Gateway! ❕ We basically recommend that the PIN query of the SIM card be deactivated to prevent any resultant problems (e.g. locking of the SIM card due to a false or missing PIN in the configuration of the SMS Gateway). Leave this field empty in this case.  
Multipart |  _Mode for sending text messages_. Select _Multipart_ in order to send messages as a text message with more than 160 characters. Select _Split_ in order to divide longer messages into several text messages with a maximum of 160 characters each.  
Blocktime | _Number of seconds for which the modem is blocked after a malfunction_.  
Block after x failures  | _Number of unsuccessful send attempts before the modem is blocked_.  
  
### Error message SIM_NOT_INSERTED

Causes of error message:

  * SIM is invalid (contract expired, contract ended, SIM blocked)

  * SIM is electrically defective

  * SMS gateway defective

Please run the following tests:

1\. Switch off the device completely (completely off!). Remove and reinsert
SIM. Make sure that the SIM fully engages. Switch on the SMS gateway again.
This procedure is sometimes successful if an electrical fault, e.g. due to
static electricity, could have been the cause.

2\. Remove the SIM card and test it in a smartphone. You can also send and /
or receive an SMS from your smartphone. This is the most reliable way to check
that everything is OK with the SIM and the contract with the provider. If the
SIM in a smartphone does not work either, the fault can be found in the SIM
itself or in the contract.

Related articles

  * Firmware Update

  * First steps 

  * Are there further modules for the SMS Gateway?
  * Who has access to software updates?

  * Help

  * How can I update the firmware of my SMS Gateway?

  * How do I get a license for my SMS Gateway?

  * Who can I ask if I need support?

  * I receive the message: "This is not a safe connection". What does this mean?

  * Upload license

  * Technical Specifications
  * Support Informations

