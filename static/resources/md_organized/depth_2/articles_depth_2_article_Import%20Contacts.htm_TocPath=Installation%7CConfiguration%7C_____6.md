# Import Contacts

ê For older devices without support, this function requires the licensing of
the _Receiver groups_ module.

➯ An import for contacts is provided in the web interface under
**Configuration - Address book - Import contacts** and**Configuration - Groups
- Import contacts**.

Fill your address book without any great manual work.

Import your contacts and add them to recipient groups at once. Keep all your
contacts always up to date with the automization function.

The contacts are imported by a CSV file.

## 1\. Setup the CSV file

The CSV file needs to be structured according to the following scheme:

## 2\. Provide the CSV file

via web server

Store the CSV file on a webserver, to update your address book regularly.

The SMS Gateway needs access to the provided CSV file.

Manuel Upload

Alternatively, you can import the data once, by uploading the file manually.
Use the _Import now_ button to start the import.

➯ Check the format of your csv file via the manuel upload.

## 3\. Configure the automatic import

Option | Description  
---|---  
**Automatic import** | Enable this function to start the import automatically. You can define a time interval for the automatic import. Use this function to keep your address book up to date.  
CSV file  | URL to the provided CSV file.  
Disable server certificate check  | Enable this option to turn off the server certificate check.   
**Interval** | Timing for the automatic import (https://en.wikipedia.org/wiki/Cron).  
Reset address book  |  Enable this option to delete all contacts and groups before the import starts.  êPlease note that all destinations in monitoring and message routing will be also deleted.  
  
➯Examples for Cron

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

