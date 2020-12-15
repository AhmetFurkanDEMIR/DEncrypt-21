* This application allows you to keep your images securely and to store your personal data in images. 

* This application is written in Python and Qt, it has been tested on Linux (Pardus and Ubuntu) and MacOS (High sierra) operating systems.


### **Application details**

* Image encryption part was done with Fernet(symmetric encryption) algorithm, this algorithm is accessed from the python module named cryptography.

Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. Fernet also has support for implementing key rotation via MultiFernet. [Fernet](https://cryptography.io/en/latest/fernet.html)

* I did the part of embedding encrypted text in the image with the python module named cryptosteganography.

A python steganography module to store messages or files protected with AES-256 encryption inside an image. 

Steganography is the art of concealing information within different types of media objects such as images or audio files, in such a way that no one, apart from the sender and intended recipient, suspects the existence of the message. By default steganography is a type of security through obscurity. 

Additionally this module also enhance the security of the steganography through data encryption. The data concealed is encrypted using AES 256 encryption, a popular algorithm used in symmetric key cryptography. [cryptosteganography](https://pypi.org/project/cryptosteganography/)

* All modules used in the application.

```python
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptosteganography import CryptoSteganography
from cryptography.hazmat.primitives import hashes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from cryptography.fernet import Fernet
from PyQt5.QtGui import QIcon
from PIL import Image
import cryptography
import base64
import sys
import os
import io
```


### **Running the application**

* Install all necessary packages for the application with the command below.

```linux
pip3 install -r requirements.txt
```

* After installing the packages, you can use the application by running the following command while in the same directory as the application.

```linux
python3 main.py
```


### **The future of practice**

* The application will continue to be open source, and features such as document, pdf and audio file encryption will be introduced in the next versions.


### **Platforms**

* **Desktop** -> Available, Tested : Linux(Pardus, Ubuntu), macOS(High sierra)

* **Android** -> Is not available : Estimated 09/04/2021


### **Official Launch Trailer**

* [Link](https://www.linkedin.com/posts/1dfurkan_python-qt-qt5-activity-6744545395138953216-pYsB)


### **In-app images**

<p align="center">
  <img src="https://user-images.githubusercontent.com/54184905/102191665-c71fd480-3eca-11eb-8b25-be34225da45e.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/54184905/102191661-c6873e00-3eca-11eb-8359-8205c546537b.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/54184905/102191659-c5561100-3eca-11eb-8d4e-d2c4b346b984.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/54184905/102191667-c7b86b00-3eca-11eb-86eb-d05241978d0d.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/54184905/102191666-c71fd480-3eca-11eb-85ae-20340c88cbea.png" />
</p>


