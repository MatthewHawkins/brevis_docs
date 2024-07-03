# PHP

This section describes how to use the swagger SDK PHP client

  1. Download and extract the PHP client SDK package from the unit.  
  

  2. Navigate into the extracted directory.  
  

  3. Install dependencies using composer: composer install

i More information about the build process and some code samples can be found
in the extracted directory's README.md file.

### SSL Certificate Issues

If the gateway uses an invalid or self-signed certificate, the requests will
fail with the following message:

cURL error 60: SSL certificate problem: self signed certificate (see
https://curl.haxx.se/libcurl/c/libcurl-errors.html)

To fix this, you could either register a valid certificate for the
gateway(Recommended), or you can accept the invalid certificate by disabling
SSL verify in the created Guzzle client (Suggested for testing only):

$client = new GuzzleHttp\Client(['verify' => false])

$apiInstance = new Swagger\Client\Api\ContactsApi(

$client,

$config

);

This statement causes the application to accept any kind of certificate.

### Instruction Notes REST API for PHP Client SDK

  1. Download the PHP Client SDK  
https://<GatewayIP>/?modul=maintainance&site=restapi  
  

  2. The Autoload.php can be copied directly from the link without changes: https://github.com/yaoshanliang/swagger-client-php

a. The Autoload.php must be in the same directory as the README.md of the
Swagger client of the SDK.  
  

  3. Install GuzzleHttp via composer:

“composer require guzzlehttp/guzzle:^7.4”  
  

  4. Configure call of GuzzleHttp:

$guzzle_config = array (

'verify' => false,

'auth' => ['admin','admin']

);

a. ‘verify’ => false: so that even self signed certificates are accepted

b. ‘auth’ => [<Username>,<Password>]  
  

  5. The Guzzle Config must be added when calling the client:

new GuzzleHttp\Client($guzzle_config),

Note on the following classes:

StateResponseSim.php

MessagePayloadRecipients.php

MessagePayload.php

In the "getStateAllowableValues" function, the values in the array must be
separated by ",".

