# Telegram Configuration

ê **Licensing for the Telegram module is required. This licensing is free of
charge for support customers. Please contact**sales@brevis.one**.**

i The options for this function are provided in the web interface under
**Configuration - Telegram**.

ê To be able to use the Telegram functionality of the SMS gateway, you need a
SIM card ready for reception with a number already registered with Telegram in
your SMS gateway.

The registration process is described below.

## User interface

Option | Description  
---|---  
Status of the Telegram registration  | You can see the status of the Telegram sign in at the top (Success, Error).   
Telegram Number  | The phone number Telegram is signed in on, the format of the phone number has to be international format: 0049 1701234567.   
Telegram Testnumber  | Phone number you can sent a test message via the Send button, the test number can have the formats 049* 01* or +49*.   
Telegram Username  | The user name of the Telegram account, has to be two names separated by one space.   
  
Option | Description  
---|---  
Sender Blacklist/Whitelist  | Select between a Blacklist or Whitelist to restrict the Telegram recieving, the numbers have to have the format 491701234567.   
Stop sending Telegram  | Deactivate the delivery of Telegram messages.   
  
## Sign Up for Telegram

i The sign up process can not be done via the Telegram Web App, reachable
under: https://web.telegram.org

To start using the Telegram functionality of the SMS Gateway, a SIM card with
an already registered Telegram account is needed.

To register for Telegram, please follow these steps:

  1. Navigate to the Telegram website: https://telegram.org/.
  2. Choose your corresponding platform (Android, IOS, Windows, etc.) and download/start it.
  3. Type in the phone number in the field **Phone**.
  4. You should now receive a verification code from Telegram via SMS.
  5. Enter the code received in the Telegram app.
  6. Enter your Name and Surname.
  7. Registration has been completed þ.
  8. **Important:** After the registration has been completed, the account must be signed off on the device used for registration, otherwise the sign up on the SMS Gateway cannot take place.

## Communication with the Telegram servers

Telegram uses the communication protocol MTProto. MTProto can use various
network protocols to communicate. HTTP, HTTPS, TCP, UDP.

## Internet connection failure

Telegram sends messages via Automatic on default. Automatic trys to send the
message via Telegram, if it fails the message will be delivered by text
message.

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

