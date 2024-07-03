# HTTP API

To use the HTTP API you first need a system user who is authorised to use the
API.

ê We recommend that you do not use the “admin” user here but that you create a
new user with restricted authorisations.

## 1\. Create a new system user

  1. Log in to the SMS Gateway with the _admin_ user.
  2. Navigate to the _system user_ option via _configuration_ in the menu bar.
  3. Create a new user, e.g.: _apiuser_.
  4. Manage the user authorisations using the pencil symbol at the end of the line.  
Grant the _Access to the HTTP API_ authorisation.  
Further authorisations are not required.

* * *

## 2\. Using the HTTP API

The API can be addressed with the following: _https:// <SMS Gateway
IP>/api.php_.

You can send data to this interface via POST or GET.

#### **Necessary**

**Option** | Description  
---|---  
**username** | System user authorised to access the HTTP API.  
**password** | The user’s password.  
**text** | Content of the text message.  
**to** | Recipient of the text message depending on _mode_.  
  
#### **Optional**

**Option** | **Description**  
---|---  
**hexmode** | Activates the hexadecimal format for the text field with true.  
**list** | With white a whitlist will be defined, with black a blacklist will be defined. Requires the parameter regex.   
**mode** |  Mode in accordance with the following table. Invalid modes are resulting in the default mode number. | **Option** | **to interpretation** | **Description**  
---|---|---  
group |  **to** = ID (recommended) or name of a user group | You can send a text message to a user group using this option. User groups are managed via **Configuration - Groups**. The use of groups requires the recipient groups module to be licensed.  
number | **to** = Recipient’s telephone number | You can send a text message to individual telephone numbers using this option (Standard).   
telgroup | **to** = ID (recommended) or name of a user group | You can send a message via automatic to a user group using this option. Automatic trys to deliver the notification via Telegram, if it fails the notification will be delivered by text message. User groups are managed via **Configuration - Groups**. The use of groups requires the recipient groups module to be licensed.  
telnumber | **to** = Recipient’s telephone number | You can send a message via automatic to individual telephone numbers using this option. Automatic trys to deliver the notification via Telegram, if it fails the notification will be delivered by text message.  
teluser | **to** = ID (recommended) or name of a contact in the address book | You can send a message via automatic to a contact using this option. Automatic trys to deliver the notification via Telegram, if it fails the notification will be delivered by text message. Contacts are managed via **Configuration - Address book**.  
user | **to** = ID (recommended) or name of a contact in the address book | You can send a text message to a contact using this option. Contacts are managed via **Configuration - Address book**.  
**regex** | Use a regular expression with this parameter. If the regular expression matchs the used phone number the parameter list will define its behaviour. Pay attention to a necessary URL-Encoding.  
**telauto** |  Turns off the automatic delivery option with false. If this is not deactivated, the message will be sent by SMS if the recipient's number was not used for Telegram.  
**ring** | By adding the parameter “ring” to the query string, a voice call to the recipient will be initiated. The text message given with the parameter “text” will be ignored in this case.   
**flash** | The query parameter “flash” will generate a SMS Class 0 message, so called “flash message” which typically pops up immediately on the recipient’s phone screen.   
  
ê The functions "Ring" and "Flash SMS" are only usable with newer versions
(from purchase date 2021) of the SMS Gateway. With a SIM card, which only
includes the sending of SMS, our "Ring" function does not work!

ê Licensing for the Telegram module is required. This licensing is free of
charge for support customers. Please contact sales@brevis.one.

* * *

## 3\. Error return codes

**HTTP Status Code** | **Error Output** | **Description**  
---|---|---  
400 | Error. See Gateway logs for more information.  | Wrong mode, group not existing, contact not existing or wrong number.   
400 | Error: Parameter miss. | Missing parameters.  
401 | 401 Unauthorized - Username or Password wrong.  | Username and/or password wrong.   
403 | 403 Forbidden - Your User has no right to send SMS over API.  | User has no permission to send SMS over API.   
408 | FAILED - Timeout or see Gateway logs for more information.  | Server exceeded the time limit waiting for request.   
  
i Status Codes will additionally be output as HTTP-Response-Codes

* * *

## 4\. Examples with GET

#### 4.1. Example SMS

**curl**

curl -X GET "https://<IP SMS
Gateway>/api.php?text=Test&to=00491701234567&username=apiuser&password=secret&mode=number"

**powershell**

Invoke-WebRequest -Uri "https://<IP SMS
Gateway>/api.php?text=Test&to=00491701234567&username=apiuser&password=secret&mode=number"
-Method GET

#### 4.2. Example Telegram

**curl**

curl -X GET "https://<IP SMS
Gateway>/api.php?text=Test&to=00491701234567&username=apiuser&password=secret&mode=telnumber&telauto=false"

**powershell**

Invoke-WebRequest -Uri "https://<IP SMS
Gateway>/api.php?text=Test&to=00491701234567&username=apiuser&password=secret&mode=telnumber&telauto=false"
-Method GET

#### 4.3. Example Hexmode

**curl**

curl -X GET "https://<IP SMS
Gateway>/api.php?text=48616c6c6f2064696573206973742065696e65205465737420534d53&to=00491701234567&username=apiuser&password=secret&hexmode=true"

**powershell**

Invoke-WebRequest -Uri "https://<IP SMS
Gateway>/api.php?text=48616c6c6f2064696573206973742065696e65205465737420534d53&to=00491701234567&username=apiuser&password=secret&hexmode=true"
-Method GET

* * *

## 5\. Examples with POST

#### 5.1. Example SMS

**curl**

curl -X POST -d
"text=Test&to=00491701234567&username=apiuser&password=secret&mode=number"
"https://<IP SMS Gateway>/api.php"

**powershell**

Invoke-WebRequest -Uri https://<IP SMS Gateway>/api.php -Method POST -Body
@{username='apiuser';password='secret';to='01701234567';text='Test';mode='number'}

#### 5.2. Example Telegram

curl

curl -X POST -d
"text=Test&to=00491701234567&username=apiuser&password=secret&mode=telnumber&telauto=false"
"https://<IP SMS Gateway>/api.php"

**powershell**

Invoke-WebRequest -Uri https://<IP SMS Gateway>/api.php -Method POST -Body
@{username='apiuser';password='secret';to='01701234567';text='Test';mode='telnumber';telauto='false'}

#### 5.3. Example Hexmode

**curl**

curl -X POST -d
"text=48616c6c6f2064696573206973742065696e65205465737420534d53&to=00491701234567&username=apiuser&password=secret&hexmode=true"
"https://<IP SMS Gateway>/api.php"

**powershell**

Invoke-WebRequest -Uri https://<IP SMS Gateway>/api.php -Method POST -Body
@{username='apiuser';password='secret';to='01701234567';text='48616c6c6f2064696573206973742065696e65205465737420534d53';hexmode='true'}

❕ URL encoding

A few special symbols and spaces cannot be sent via the HTTP API without URL
encoding. Use the percentage sign to code the content of your message.

Related articles

  * Can I automate the sending of text messages?
  * Email to SMS
  * Firmware Update
  * First steps 
  * Are there further modules for the SMS Gateway?
  * Help
  * How does Email to SMS function?
  * How can I update the firmware of my SMS Gateway?
  * HTTP API
  * Message Routing
  * Can my SMS Gateway receive and forward messages?
  * How do I get a license for my SMS Gateway?
  * Can the SMS Gateway send to landline numbers?
  * Sending messages via the web interface

