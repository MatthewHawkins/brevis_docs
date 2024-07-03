# SSL support

i On delivery your SMS Gateway supports the encrypted communication via HTTPS.

i Further options on SSL support can be found in the web interface under
**Configuration - SSL support**.

## 1\. Setting up a self-signed certificate

This is the simplest method to set up a personalised certificate for the
encrypted communication with the SMS Gateway.

First complete the form.

Option | Description  
---|---  
**Country** | Enter the two-digit country code here, e.g.: _DE_.   
**Domain** | Enter the exact domain name here which is to be protected by the certificate.  
**Email** | Enter the email address of the person responsible, e.g.: _info@brevis.one_.  
Locality name | Enter your city or town here, e.g.: _Saarbrücken_.  
Organisation name  | Enter your name or company name here, e.g.: _BASIS Europe_ .  
Organisation unit name  | Enter your organisation unit name here (if present).   
State or province name  | Enter your state or province here, e.g.: _Saarland_.   
  
Then confirm by clicking on the _Create self-signed certificate_ button. The
SMS Gateway will now generate a certificate according to your requirements and
will confirm that the process was successful. Reboot the SMS Gateway.

❕ Self-signed certificates are not viewed to be secure because they have not
been verified by a trustworthy agent. This circumstance has _no_ influence on
the security of the connection. Further information is provided in our FAQs.

## 2\. Creating a Certificate Signing Request (CSR)

A CSR is a digital application to create a certificate. Complete the form and
click on the _Create CSR_ button.

The SMS Gateway creates the Certification Request in accordance with your
requirements, e.g.:

Send the CSR to a Certification agent, who will issue a certificate in
accordance with your application. The certificate must then be imported.

## 3\. Importing a certificate

If you already have a certificate, you can import it. The certificate must be
available in a .PEM file.

If the certificate has been created by way of a CSR created by the SMS
Gateway, the certificate file may contain the base64-coded certificate
exclusively, e.g.:

❕ If you have created the certificate differently, the certificate file must
contain the base64-coded certificate and the decoded private key.

ê Certificate chains are not allowed to be part of the certificate file.

Click on the _Choose file_ button and select the certificate file (.PEM) in
your file system. Then confirm by clicking on the _Import button_.

The SMS Gateway will confirm that the process was successful. Reboot the SMS
Gateway.

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

