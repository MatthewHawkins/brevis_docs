# Message Routing

ê For older devices without support, this function requires the licensing of
the Message Routing module.

i The options for this function are located in the web interface under
**Configuration - Message Routing.**

The Message Routing allows to forward incoming messages (SMS, E-Mail, Telegram
or Telegram & SMS) based on configurable rules.

## Overview of configurable rules

**Rule** | **Description**  
---|---  
AND Connection  | Specify one or more search pattern that are related to each other. Only if all search pattern matches the rule gets activated.  
Message | Specify the message text which activates this rule. On incoming emails the subject is not considered.  
Message RegEx  | Specify the message text which activates this rule (the sender will evaluate as Regular Expression). On incoming emails the subject is not considered.  
NOT Connection  | Specify one or more search pattern to ignore the rule.  
OR Connection | Specify one or more search pattern that are related to each other. If one search pattern matches the rule gets activated.  
Sender |  Specify the sender which activates this rule. **Example:**

  * 004917012345678
  * max.mustermann@brevis.one

  
Sender RegEx  |  Specify the sender which activates this rule (the sender will evaluate as Regular Expression). **Example:**

  * ^(49|43)+\d
  * (.*)@brevis.one

  
  
## GUI

Click the **Add** button in the column rule, to add a new rule.

Click the **Add** button in the column destination, to add a destination for
the forwarding.

**Choice** | **Function** | Requires License  
---|---|---  
Add contacts ( Telegram/Automatik )  | Add a contact from the addressbook. | Telegram  
Add groups ( SMS/E-Mail )  | Add a group as recipient. | recipient groups  
Add contact ( SMS/E-Mail )  | Add a contact from the addressbook. |   
Auto responder | Add a auto responder. |   
Add a group (Telegrom/Automatic) | Add a group as recipient. | Telegram  
HTTP Request  |  Add the URL to a script which conducts further processing. Example: http://example.com/incomingsms.php?from=$NUMBER$&text=$TXT$  |   
HTTP Request (iSMS Protokoll) |  Add the URL to your monitoring system, to acknowledge Nagios alerts. Example: http://example.com/isms/smsack.cgi |   
  
Use the **arrows** in the column order to sort the rules. The rules will be
processed in order from top to bottom. Multiple rules can match.

Use the option **Ignore subsequent rules** to prevent the processing of
further rules.

Search and replace:

When checking the checkmark on the field Search and replace, further options
appear:

With this option it is possible to search incoming messages with a search
pattern and replace them with the substitution.

The _first input field_ requires a search pattern in the form of a Regular
expression.

The _second input field_ requires the substitution for the search pattern.

## Examples

Examples for search and replace:

| All incoming messages (SMS) get searched through for the search pattern
**Alpha** and get replaced by **Bravo** if found.  
---|---  
  
* * *

| Example for a search pattern utilizing a Regular expression. All incoming
messages (SMS) get searched through for the search patterns **Search 1** and
**Search 2** and get replaced by **Replace** if found.  
---|---  
  
Examples for logical connections and regular expressions

* * *

* * *

* * *

| Every incoming message (SMS) will be forwarded to an E-Mail-adress  
---|---  
  
* * *

| Every incoming message (SMS) from the specified number will be forwarded.  
---|---  
  
* * *

| The incoming message (Telegram & SMS) that contains the text "meeting at"
will be forwarded.  
---|---  
  
* * *

| The incoming message (SMS) has to be sent from a german or austrian number
to get forwarded.  
---|---  
  
* * *

| The incoming message (E-Mail) have to be sent from a sender of the domain
_brevis.one_ to get forwarded.  
---|---  
  
* * *

| Every message (SMS) that was not sent from a number with 123 at the end or
that does not contain the text "Test" will be forwarded.  
---|---  
  
Related articles

  * Connecting the SMS Gateway to a Microsoft Exchange Server 2013
  * Email to SMS
  * Firmware Update
  * First steps 
  * Are there further modules for the SMS Gateway?
  * General configuration
  * Help
  * How does Email to SMS function?
  * How can I update the firmware of my SMS Gateway?
  * Message Routing
  * Can my SMS Gateway receive and forward messages?
  * How do I get a license for my SMS Gateway?
  * Forwarding
  * Who can I ask if I need support?

