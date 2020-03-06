<<<<<<< HEAD
# SafeChat
=======
# SafeChat

SafeChat is a TCP/IP socket chat program with RSA handshake protocol AES symmetric encryption and SHA512 hashing. It supports multi client encryption and communication.

This program was created in order to demonstrate simple cryptography and socket programming concepts. It is not intended for commercial use!

# Library Dependancies

  - PyCrypto (Download Link: https://pypi.org/project/pycrypto/)
  - Termcolor (Download Link: https://pypi.org/project/termcolor/)
# Usage
Run the server module on the appropriate machine:
    `python3 server.py`
You will be asked to enter the IP address of the interface & a static Port to use. When you see the output **Listening for connections on {IP}:{Port}...** the server is ready.

Every client has to run the client module in order to connect and initiate comms:
    `python3 client.py`
You will be asked to enter the IP address of the interface, a static Port and a username as an identifier in the chatroom. When you see the prompt **<You>** you can start sending/receiving messages.

# Future Plans
1. Increased security through improved encryption protocol (Forward Secrecy, EC).
2. Dynamic send/receive collision aversion.
3. Data Integrity (Hash Check).
4. File sending capabilities.
5. Integration of HMAC.
6. VoIP, VideoChat

Note: Thanks to mjm918 for parts of the handshake protocol outline.
>>>>>>> 2868e70a64e79addc0453fd46caf02d3197e2fe6
