---
slug: email-to-sms
---

# Email to SMS

ê For older devices without support, this function requires the licensing of
the E-Mail to SMS module.

i The options for this function may be found in the web interface under
**Configuration - Email to SMS.**

## 1\. Configure E-mail to SMS

1\. Firstly enter one or several accepted email domains (one domain per line),
e.g.:

sms.local

brevis.one

2\. Now enter one or several IP addresses or network addresses from which
incoming emails are to be accepted (one address per line), e.g.:

192.168.1.2

192.168.1.0/24

3\. Select the _Blacklist_ or _Whitelist_ and add one or several email
addresses of the list (one address per line):

  1. **Blacklist** \- The senders added to the list cannot use the email to SMS function.
  2. **Whitelist** \- The senders added to the list can exclusively use the email to SMS function.
  3. The use of PHP Regular Expressions is possible here, e.g.:

(.*)@baddomain.com

(.*)@anotherbaddomain.com

4\. Select the parts of the email from which the text message is generated:

  1. Subject & text
  2. Text
  3. Subject

### Advanced

#### SMTP Service

Deactivate the SMTP service if the SMS Gateway should not receive emails.

#### SMTP Port

Choose the desired port the SMS Gateway will receive emails.

The following ports cannot be used as port: 80, 443, 8080, 8443, 3306, 22,
2391, 161.

The above listed ports are already used for other SMS Gateway functions.

#### Force Encryption

This setting prevents the SMS Gateway to accept emails from unsecured
connections. The SMS Gateway will only send emails on secured connections when
activated.

#### TLS Version and higher

Set the lowest TLS version the SMS Gateway accepts emails from.

#### Encryption Ciphers

Choose between High and Medium ciphers.

➯ Examples on using Email to SMS are provided in our FAQs.

* * *

## 2\. Test E-Mail to SMS

### Test SMTP with STARTTLS

To verify your configuration you can use the Windows Powershell or a Linux
Shell.

Enter the following commands:

openssl s_client -connect 192.168.1.1:25 -starttls smtp

HELO 192.168.1.1

MAIL FROM: <john.doe@brevis.one>

rcpt to: <00491701234567@sms.local>

DATA

FROM: <john.doe@brevis.one>

TO: <00491701234567@sms.local>

Subject: Test

Text

.

QUIT

The SMS Gateway will answer now:

CONNECTED(0000012C)

depth=0 C = Germany, ST = Saarland, L = Saarbrücken, O = BASIS Europe, CN =
brevis.one-sms-gateway

verify error:num=18:self signed certificate

verify return:1

depth=0 C = Germany, ST = Saarland, L = Saarbrücken, O = BASIS Europe, CN =
brevis.one-sms-gateway

verify return:1

\---

Certificate chain

0 s:/C=Germany/ST=Saarland/L=Saarbrücken/O=BASIS Europe/CN=brevis.one-sms-
gateway

i:/C=Germany/ST=Saarland/L=Saarbrücken/O=BASIS Europe/CN=brevis.one-sms-
gateway

\---

Server certificate

\-----BEGIN CERTIFICATE-----

...

\-----END CERTIFICATE-----

subject=/C=Germany/ST=Saarland/L=Saarbrücken/O=BASIS Europe/CN=brevis.one-sms-
gateway

issuer=/C=Germany/ST=Saarland/L=Saarbrücken/O=BASIS Europe/CN=brevis.one-sms-
gateway

\---

No client certificate CA names sent

Peer signing digest: SHA512

Server Temp Key: ECDH, P-256, 256 bits

\---

SSL handshake has read 2171 bytes and written 469 bytes

\---

New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-GCM-SHA384

Server public key is 2048 bit

Secure Renegotiation IS supported

Compression: NONE

Expansion: NONE

No ALPN negotiated

SSL-Session:

Protocol : TLSv1.2

Cipher : ECDHE-RSA-AES256-GCM-SHA384

Session-ID: ...

Session-ID-ctx:

Master-Key: ...

Key-Arg : None

PSK identity: None

PSK identity hint: None

SRP username: None

TLS session ticket lifetime hint: 7200 (seconds)

TLS session ticket:

...

Start Time: 1559829035

Timeout : 300 (sec)

Verify return code: 18 (self signed certificate)

\---

250 DSN

HELO 192.168.1.1

250 brevis.one-sms-gateway

MAIL FROM: <max.mustermann@brevis.one>

250 2.1.0 Ok

rcpt to: <00491701234567@sms.local>

250 2.1.5 Ok

DATA

354 End data with <CR><LF>.<CR><LF>

FROM: <max.mustermann@brevis.one>

TO: <00491701234567@sms.local>

Subject: Test

Text

.

250 2.0.0 Ok: queued as <MessageId>

QUIT

DONE

  

* * *

## 3\. Test SMTP

Can only be tested with the option "Force Encryption" deactivated!

To verify your configuration you can use SMTPTool.

  1. Enter the IP Address of your SMS Gateway into the **server** field.
  2. Enter 25 into the **port** field.
  3. Confirm with **Connect**.
  4. The SMS Gateway should answer now:  
  
220 brevis.one SMS Gateway  
  

  5. Enter the following command into the input field **Commands** and confirm with **Send command.**  
  
HELO 192.168.1.1  
MAIL FROM: max.mustermann@brevis.one  
RCPT TO: 00491701234567@sms.local  
DATA  
FROM: max.mustermann@brevis.one  
TO: 00491701234567@sms.local  
Subject: Test  
Text  
.  
  

  6. The SMS Gateway will answer:  
  
250 localhost  
250 2.1.0 Ok  
250 2.1.5 Ok  
354 End data with <CR><LF>.<CR><LF>  
250 2.0.0 Ok: queued as ...  
  

  

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

