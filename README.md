* This application allows you to keep your images securely and to store your personal data in images. 

* This application is written in Python and Qt, it has been tested on Linux (Pardus and Ubuntu) and MacOS (high sierra) operating systems.

### **Application details**

* **1** Image encryption part was done with Fernet(symmetric encryption) algorithm, this algorithm is accessed from the python module named cryptography. 
Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. Fernet also has support for implementing key rotation via MultiFernet. [Fernet](https://cryptography.io/en/latest/fernet.html)

* **2** I did the part of embedding encrypted text in the image with the python module named cryptosteganography.
A python steganography module to store messages or files protected with AES-256 encryption inside an image. Steganography is the art of concealing information within different types of media objects such as images or audio files, in such a way that no one, apart from the sender and intended recipient, suspects the existence of the message. By default steganography is a type of security through obscurity. Additionally this module also enhance the security of the steganography through data encryption. The data concealed is encrypted using AES 256 encryption, a popular algorithm used in symmetric key cryptography. [cryptosteganography](https://pypi.org/project/cryptosteganography/)
