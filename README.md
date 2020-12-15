* This application allows you to keep your images securely and to store your personal data in images. 

* This application is written in Python and Qt, it has been tested on Linux (Pardus and Ubuntu) and MacOS (High sierra) operating systems.


### **Application details**

* Image encryption part was done with Fernet(symmetric encryption) algorithm, this algorithm is accessed from the python module named cryptography.

Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. Fernet also has support for implementing key rotation via MultiFernet. [Fernet](https://cryptography.io/en/latest/fernet.html)

* I did the part of embedding encrypted text in the image with the python module named cryptosteganography.

A python steganography module to store messages or files protected with AES-256 encryption inside an image. 

Steganography is the art of concealing information within different types of media objects such as images or audio files, in such a way that no one, apart from the sender and intended recipient, suspects the existence of the message. By default steganography is a type of security through obscurity. 

Additionally this module also enhance the security of the steganography through data encryption. The data concealed is encrypted using AES 256 encryption, a popular algorithm used in symmetric key cryptography. [cryptosteganography](https://pypi.org/project/cryptosteganography/)


### **The future of practice**

* The application will continue to be open source, and features such as document, pdf and audio file encryption will be introduced in the next versions.


### **Platforms**

* **Desktop** -> Available, Tested : Linux(Pardus, Ubuntu), macOS(High sierra)

* **Android** -> Is not available : Estimated 09/04/2021


## **In-app images**

![Screenshot_2020-12-15_11-28-29](https://user-images.githubusercontent.com/54184905/102191659-c5561100-3eca-11eb-8d4e-d2c4b346b984.png)

![Screenshot_2020-12-15_11-28-23](https://user-images.githubusercontent.com/54184905/102191661-c6873e00-3eca-11eb-8359-8205c546537b.png)

![Screenshot_2020-12-15_11-28-15](https://user-images.githubusercontent.com/54184905/102191665-c71fd480-3eca-11eb-8b25-be34225da45e.png)

![Screenshot_2020-12-15_11-28-41](https://user-images.githubusercontent.com/54184905/102191666-c71fd480-3eca-11eb-85ae-20340c88cbea.png)

![Screenshot_2020-12-15_11-28-35](https://user-images.githubusercontent.com/54184905/102191667-c7b86b00-3eca-11eb-86eb-d05241978d0d.png)

