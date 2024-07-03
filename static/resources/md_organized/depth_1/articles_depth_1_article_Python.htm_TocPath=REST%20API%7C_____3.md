# Python

This section describes how to use the swagger SDK Python client

  1. Download and extract the Python client SDK package from the unit.  
  

  2. Navigate into the extracted directory.  
  

  3. Install dependencies: python setup.py install --user

On windows , you can launch power shell as administrator and just run: python
setup.py install  

i More information about the build process and some code samples can be found
in the extracted directory's README.md file.

### SSL Certificate Issues

If the gateway uses an invalid or self-signed certificate, the requests will
fail with the following message:

connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is
being made to host. Adding certificate verification is strongly advised

To fix this, you could either register a valid certificate for the
gateway(Recommended), or you can accept the invalid certificate by disabling
SSL verify(Suggested for testing only):

import swagger_client

configuration = swagger_client.Configuration()

configuration.verify_ssl = False

This statement causes the application to accept any kind of certificate.

