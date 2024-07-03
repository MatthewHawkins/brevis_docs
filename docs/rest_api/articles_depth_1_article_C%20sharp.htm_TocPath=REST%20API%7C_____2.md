---
slug: c_sharp
---

# C#

This section describes how to generate the swagger SDK client dll files, in
order to use them in your C# Project. By repeating the following steps, the
client SDK dll files will be created on your machine:

  1. Download and extract the C# client SDK package from the unit.  
  

  2. Navigate into the extracted directory.  
  

  3. Execute the build.bat script file using the following command:

.\build.bat  
  

  4. The script will generate the following dll files in the bin/ subdirectory:

\- IO.Swagger.dll

\- JsonSubTypes.dll

\- Newtonsoft.Json.dll

\- RestSharp.dll  
  

  5. Add these .dll files to your project, and you should be able to query the gateway's api using the SDK classes.

i More information about the build process and some code samples can be found
in the extracted directory's README.md file.

### SSL Certificate Issues

If the gateway uses an invalid or self-signed certificate, the requests will
fail with the following message:

cIO.Swagger.Client.ApiException: 'Error calling MessagesPost: The underlying
connection was closed: Could not establish trust relationship for the SSL/TLS
secure channel.'

To fix this, you could either register a valid certificate for the gateway
(recommended), or you can accept the invalid certificate by adding the
following line in your C# code (suggested for testing only):

System.Net.ServicePointManager.ServerCertificateValidationCallback = ((sender,
certificate, chain, sslPolicyErrors) => true);

This statement causes the application to accept any kind of certificate.

