---
slug: java
---

# Java

This section describes how to generate the swagger SDK client jar using Maven
or Gradle.

### Maven

To build the client SDK jar using maven, repeat the following steps:

  1. Download the java SDK zip file from the unit.  
  

  2. Extract the zip file.  
  

  3. Navigate into the extracted zip directory.  
  

  4. Execute the following command to build the client SDK jar:

maven clean package  
  

  5. You can find the java client SDK jar in the `target/` directory.

### Gradle

To build the client SDK using Gradle, repeat the following steps:

  1. Download the java SDK zip file.  
  

  2. Extract the zip file.  
  

  3. Navigate into the extracted zip directory.  
  

  4. Execute the gradlew.bat file.  
  

  5. Execute the following command to build the client SDK jar:

gradle build  
  

  6. You will find the jar file in the `build/libs/` subdirectory.

For more information about building the client SDK jar, check the SDK's
README.md file.

### Additional Dependencies

When adding the generated jar into your project's build path, keep in mind
that you will need to reference the swagger client dependencies as well. If
you're using maven or gradle in your Java project, simply copy the
dependencies from maven's pom.xml or gradle's gradle.properties file into your
project's build file. If you're not using gradle or maven, the following jars
need to be added to the build path:

threetenbp-1.3.5.jar

swagger-annotations-2.0.0.jar

okio-1.6.0.jar

okhttp-2.7.5.jar

logging-interceptor-2.7.5.jar

javax.annotation-api-1.3.2.jar

hamcrest-core-1.3.jar

gson-fire-1.8.3.jar

gson-2.8.1.jar

### SSL Certificate Issues

Once the jar is built successfully and added to your project's build path, you
can start creating some requests to query the api. If your gateway is running
with the default certificate or any other self-signed certificate, you will
most likely get the following Exception for each request:

sun.security.validator.ValidatorException: PKIX path building failed:
sun.security.provider.certpath.SunCertPathBuilderException: unable to find
valid certification path to requested target

at
java.base/sun.security.validator.PKIXValidator.doBuild(PKIXValidator.java:439)

at
java.base/sun.security.validator.PKIXValidator.engineValidate(PKIXValidator.java:306)

at java.base/sun.security.validator.Validator.validate(Validator.java:264)

at
java.base/sun.security.ssl.X509TrustManagerImpl.validate(X509TrustManagerImpl.java:313)

at
java.base/sun.security.ssl.X509TrustManagerImpl.checkTrusted(X509TrustManagerImpl.java:222)

at
java.base/sun.security.ssl.X509TrustManagerImpl.checkServerTrusted(X509TrustManagerImpl.java:129)

at
java.base/sun.security.ssl.CertificateMessage$T12CertificateConsumer.checkServerCerts(CertificateMessage.java:629)

at
java.base/sun.security.ssl.CertificateMessage$T12CertificateConsumer.onCertificate(CertificateMessage.java:464)

at
java.base/sun.security.ssl.CertificateMessage$T12CertificateConsumer.consume(CertificateMessage.java:360)

at java.base/sun.security.ssl.SSLHandshake.consume(SSLHandshake.java:392)

at
java.base/sun.security.ssl.HandshakeContext.dispatch(HandshakeContext.java:444)

at
java.base/sun.security.ssl.HandshakeContext.dispatch(HandshakeContext.java:422)

at
java.base/sun.security.ssl.TransportContext.dispatch(TransportContext.java:183)

at java.base/sun.security.ssl.SSLTransport.decode(SSLTransport.java:171)

at java.base/sun.security.ssl.SSLSocketImpl.decode(SSLSocketImpl.java:1403)

at
java.base/sun.security.ssl.SSLSocketImpl.readHandshakeRecord(SSLSocketImpl.java:1309)

at
java.base/sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:440)

at
java.base/sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:411)

at
com.squareup.okhttp.internal.io.RealConnection.connectTls(RealConnection.java:192)

at
com.squareup.okhttp.internal.io.RealConnection.connectSocket(RealConnection.java:149)

at
com.squareup.okhttp.internal.io.RealConnection.connect(RealConnection.java:112)

at
com.squareup.okhttp.internal.http.StreamAllocation.findConnection(StreamAllocation.java:184)

at
com.squareup.okhttp.internal.http.StreamAllocation.findHealthyConnection(StreamAllocation.java:126)

at
com.squareup.okhttp.internal.http.StreamAllocation.newStream(StreamAllocation.java:95)

at com.squareup.okhttp.internal.http.HttpEngine.connect(HttpEngine.java:281)

at
com.squareup.okhttp.internal.http.HttpEngine.sendRequest(HttpEngine.java:224)

at com.squareup.okhttp.Call.getResponse(Call.java:286)

at com.squareup.okhttp.Call$ApplicationInterceptorChain.proceed(Call.java:243)

at com.squareup.okhttp.Call.getResponseWithInterceptorChain(Call.java:205)

at com.squareup.okhttp.Call.execute(Call.java:80)

at io.swagger.client.ApiClient.execute(ApiClient.java:840)

at
io.swagger.client.api.MessagesApi.messagesPostWithHttpInfo(MessagesApi.java:543)

at io.swagger.client.api.MessagesApi.messagesPost(MessagesApi.java:529)

at brevis.one.Demo.main(Demo.java:82)

Caused by: sun.security.provider.certpath.SunCertPathBuilderException: unable
to find valid certification path to requested target

at
java.base/sun.security.provider.certpath.SunCertPathBuilder.build(SunCertPathBuilder.java:141)

at
java.base/sun.security.provider.certpath.SunCertPathBuilder.engineBuild(SunCertPathBuilder.java:126)

at
java.base/java.security.cert.CertPathBuilder.build(CertPathBuilder.java:297)

at
java.base/sun.security.validator.PKIXValidator.doBuild(PKIXValidator.java:434)

... 33 more

This exception is thrown because the gateway's certificate is invalid i.e. not
signed by a CA. To fix this issue, you can either install a valid
certificate(Recommended), or you can repeat the following steps in order to
tell java that you trust the gateway's certificate(Suggested only for
testing):

  1. Download the gateway's certificate as "DER encoded binary X.509 (.CER)" using any browser.  
  

  2. Navigate to your java home directory.  
  

  3. Navigate into its lib/security subdirectory.  
  

  4. Execute the following command to add the downloaded certificate to the list of accepted certificates:

<!--mdx escape-->
..\\..\bin\keytool.exe -import -trustcacerts -keystore cacerts -storepass
changeit -noprompt -alias smsgw -file `<path_to_downloaded_certificate>`

i Replace `<path_to_downloaded_certificate>` with the actual path of the
downloaded certificate file. It is important to execute this command in this
specific directory as it will add the certificate to the cacerts file from
that directory.

Once you followed the steps mentioned above, you will get past the SSL related
exceptions but the requests might still fail if you're trying to acces the
gateway using it's IP or a different hostname than the one described in the
certificate:

io.swagger.client.ApiException: javax.net.ssl.SSLPeerUnverifiedException:
Hostname 10.66.115.129 not verified:

certificate: sha1/9UKaRIiZ5plr7Be+qy0X8NwMqMw=

DN: CN=braintower-sms-gateway, O=Braintower Technologies GmbH, L=Sankt
Ingbert, ST=Saarland, C=Germany

subjectAltNames: [braintower-sms-gateway, braintower-sms-gateway.brain-
tower.net, 192.168.24.202, localhost, 127.0.0.1]

at io.swagger.client.ApiClient.execute(ApiClient.java:844)

at
io.swagger.client.api.MessagesApi.messagesPostWithHttpInfo(MessagesApi.java:543)

at io.swagger.client.api.MessagesApi.messagesPost(MessagesApi.java:529)

at brevis.one.Demo.main(Demo.java:89)

This exception is thrown because the CN(Common Name) of the gateway's
certificate refers to "braintower-sms-gateway" by default and you're trying to
access the gateway using it's IP or a different name. To get around this
Exception, in your java code you can create a so called "null hostname
verifier" which accepts all hostnames for all the accepted certificates.
Alternatively you could only validate the one IP/hostname of the gateway.

The following example shows how to add a custom hostname verifier to accept
any hostname when querying the messages API:

```java
MessagesApi apiMessages = new MessagesApi();

ApiClient client = apiMessages.getApiClient();
client.getHttpClient().setHostnameVerifier(new HostnameVerifier() {

@Override

public boolean verify(String hostname, SSLSession session) {

return true;

}

});
```
i You must add your custom hostname verifier to each API class you want to
acces. It does not suffice to add it once to the ApiClient class.
