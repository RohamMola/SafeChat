from Crypto.Cipher import AES
import socket;
import select;
import errno;
import sys;
import os;
<<<<<<< HEAD
import pyaudio;
import threading;
=======
>>>>>>> 2868e70a64e79addc0453fd46caf02d3197e2fe6
from Crypto import Random;
from Crypto.PublicKey import RSA;
from Crypto.Util import Counter;
import hashlib;
from termcolor import colored;

<<<<<<< HEAD
class VoIP:
    _chunk_size = 1024;
    _audio_format = pyaudio.paInt32;
    _channels = 1;
    _rate = 20000;
    def __init__(self, chunk_size, audio_format, channels, rate):
        super().__init__();
        self._chunk_size = chunk_size;
        self._audio_format = audio_format;
        self._channels = channels;
        self._rate = rate;
        self.p = pyaudio.PyAudio();
        self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size);
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size);

    def receive_server_data(self, socket):
        while True:
            try:
                username_length = int(username_header.decode('utf-8').strip());
                rusername = client_socket.recv(username_length).decode('utf-8');
                message_header = client_socket.recv(HEADER_LENGTH);
                message_length = int(message_header.decode('utf-8').strip());
                message = client_socket.recv(message_length);
                decrypted_message = AESDecrypt(key_256, message);
                self.playing_stream.write(decrypted_message);
            except:
                pass;
        
    def send_data_to_server(self, socket, key):
        while True:
            try:
                data = self.recording_stream.read(self._chunk_size);
                send(socket, AESEncrypt(key, data), "byte");
            except Exception as e:
                pass;

def UploadFile(socket, address, key, buffer=2048):
    """address = address.encode('utf-8');
    address_enc = AESEncrypt(key, address);
    address_header = f"{len(address_enc):<{HEADER_LENGTH}}".encode('utf-8');
    socket.send(address_header + address_enc);"""
    f = open(address, 'rb');
    l = f.read(buffer);
    while (l):
        data = AESEncrypt(key, l);
        data_header = f"{len(data):<{HEADER_LENGTH}}".encode('utf-8');
        client_socket.send(data_header + data);
        l = f.read(buffer);
    f.close();

def DownloadFile(socket, name, key, buffer=2048):
    f = open(name, 'wb');
    user_data = receive_message(socket);
    l = receive_message(socket)["data"];
    l = AESDecrypt(key_256, l);
    while(l):
        if (l != "SFTP END".encode('utf-8')):
            f.write(l);
            user_data = receive_message(socket);
            l = receive_message(socket)["data"];
            l = AESDecrypt(key, l);
        else:
            print(colored("SFTP END", "green"));
            break;
    f.close();

=======
>>>>>>> 2868e70a64e79addc0453fd46caf02d3197e2fe6
def AESEncrypt(key, plaintext):
    IV = os.urandom(16);
    ctr = Counter.new(128, initial_value=int.from_bytes(IV, byteorder='big'));
    aes = AES.new(key, AES.MODE_CTR, counter=ctr);
    return IV + aes.encrypt(plaintext);

def AESDecrypt(key, ciphertext):
    IV = ciphertext[:16];
    ctr = Counter.new(128, initial_value=int.from_bytes(IV, byteorder='big'));
    aes = AES.new(key, AES.MODE_CTR, counter=ctr);
    return aes.decrypt(ciphertext[16:]);

def send(client_socket, message, type="string"):
    if type == "byte":
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8');
        client_socket.send(message_header + message);
    elif type == "string":
        message_sender = message.encode('utf-8');
        message_sender_header = f"{len(message_sender):<{HEADER_LENGTH}}".encode('utf-8');
        client_socket.send(message_sender_header + message_sender);

def sendEncrypted(client_socket, message, AESKey):
    message_encrypted = AESKey.encrypt(message);
    message_sender = message_encrypted.encode('utf-8');
    message_sender_header = f"{len(message_sender):<{HEADER_LENGTH}}".encode('utf-8');
    client_socket.send(message_sender_header + message_sender);

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH);
        if not len(message_header):
            return False;
        message_length = int(message_header.decode('utf-8').strip());
        return {'header': message_header, 'data': client_socket.recv(message_length)};
        pass;
    except:
        return False;

def recieveEncryptedMessage(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH);
        if not len(message_header):
            return False;
        message_length = int(message_header.decode('utf-8').strip());
        return {'header': message_header, 'data': AESKey.decrypt(client_socket.recv(username_length).decode('utf-8'))};
    except Exception as e:
        return False;

<<<<<<< HEAD
def prompt(specialmessage=""):
    sys.stdout.write("<You> %s" %specialmessage);
=======
def prompt():
    sys.stdout.write("<You> ");
>>>>>>> 2868e70a64e79addc0453fd46caf02d3197e2fe6
    sys.stdout.flush();

HEADER_LENGTH = 10;
FLAG_READY = "Ready";
FLAG_QUIT = "Quit";

hasher = hashlib.sha512();

random_generator = Random.new();
RSAKey = RSA.generate(4096, random_generator.read);
public = RSAKey.publickey().exportKey();
private = RSAKey.exportKey();
public_hash = hashlib.sha512(public);
#public_hash = hasher.update(public);
public_hash_hexdigest = public_hash.hexdigest();

print("Your Public Key: %s" %public);
print("Your Private Key: %s" %private);
print("Your Public SHA512 Hash: %s" %public_hash_hexdigest);

IP = str(input("Enter Server IP Address: "));
Port = int(input("Enter Socket Port: "));
user_username = str(input("Username: "));

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print("Connecting to Server...");
    client_socket.connect((IP, Port));
    print(colored("Connected!", "green"));
    client_socket.setblocking(False);
except BaseException:
    print(colored("Error Occured During Connection Phase!", "red"));
    exit(1);

send(client_socket, public + ":".encode('utf-8') + public_hash_hexdigest.encode('utf-8'), "byte");

'''while(True):
    try:
        fGet_header = client_socket.recv(HEADER_LENGTH);
        break;
    except Exception:
        pass


#fGet_header = client_socket.recv(HEADER_LENGTH);
fGet_length = int(fGet_header.decode('utf-8').strip());
try:
    fGet = client_socket.recv(fGet_length);
except Exception as e:
    print(colored("Error Occurred During Initial Handshake Sequence!", "red"));
    print(e);
    exit(1);
'''
while(True):
    fGet = receive_message(client_socket);
    if fGet == False:
        continue;
    else:
        break;
split = fGet["data"].split("(:0x0:)".encode('utf-8'));
toDecrypt = ''.encode('utf-8');
for i in range(0, len(split) - 1):
    toDecrypt += split[i];
#toDecrypt = split[0];
serverPublic = split[len(split) - 1];
print("Server's Public Key: %s" %serverPublic);
#decrypted = RSA.importKey(private).decrypt(eval(toDecrypt.replace("\r\n", '')));
decrypted = RSA.importKey(private).decrypt(toDecrypt);
splittedDecrypt = decrypted.split(":0x0:".encode('utf-8'));
ttwoByte = splittedDecrypt[0];
session_hexdigest = splittedDecrypt[1];
serverPublicHash = splittedDecrypt[2];
print("Client's AES Key In Hash: %s" %session_hexdigest);
sess = hashlib.sha512(ttwoByte);
#sess = hasher.update(ttwoByte);
sess_hexdigest = sess.hexdigest();
hashObj = hashlib.sha512(serverPublic);
#hashObj = hasher.update(serverPublic);
server_public_hash = hashObj.hexdigest();
print(colored("Matching Server's Public Key & AES Key...", "yellow"));
if server_public_hash == serverPublicHash.decode('utf-8') and sess_hexdigest == session_hexdigest.decode('utf-8'):
    print(colored("Sending Encrypted Session Key...", "blue"));
    (serverPublic, ) = RSA.importKey(serverPublic).encrypt(ttwoByte, None);
    send(client_socket, serverPublic, "byte");
    print(colored("Creating AES Key...", "blue"));
    key_256 = ttwoByte;
    #AESKey = AES.new(key_256, AES.MODE_CTR, counter=lambda: counter);
    #AESKey = AES.new(key_256, AES.MODE_CBC, IV=key_256);
    try:
        #ready_header = client_socket.recv(HEADER_LENGTH);
        while(True):
            ready = receive_message(client_socket);
            if ready == False:
                continue;
            else:
                break;
    except Exception as e:
        print(colored("Error Occurred During Second Phase Of Handshake Sequence!", "red"));
        print(e);
        exit(1);
    #ready_length = int(ready_header.decode('utf-8').strip());
    #ready = client_socket.recv(ready_length);
    #ready_msg = AESKey.decrypt(ready);
    ready_msg = AESDecrypt(key_256, ready["data"]);
    if ready_msg == FLAG_READY.encode('utf-8'):
        print(colored("Client Is Ready To Communicate!", "green"));
    else:
        print(colored("Server's Public || Session Key Doesn't Match. Shutting Down Socket!", "red"));
        client_socket.close();
        exit(1);

username = user_username.encode('utf-8');
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8');
client_socket.send(username_header + username);

prompt();

while(True):
    socket_list = [sys.stdin, client_socket];
    read_sockets, write_socket, error_socket = select.select(socket_list, [], [], 0);
    for socks in read_sockets:
        if socks == client_socket:
            try:
                username_header = client_socket.recv(HEADER_LENGTH);
                if not len(username_header):
                    print("Connection Closed By The Server");
                    sys.exit();
                username_length = int(username_header.decode('utf-8').strip());
                rusername = client_socket.recv(username_length).decode('utf-8');
                message_header = client_socket.recv(HEADER_LENGTH);
                message_length = int(message_header.decode('utf-8').strip());
                message = client_socket.recv(message_length);
                decrypted_message = AESDecrypt(key_256, message);
<<<<<<< HEAD
                if decrypted_message[:13] == "SFTP Initiate".encode('utf-8'):
                    print("Incoming File....");
                    prompt("Enter File Name: ");
                    name = sys.stdin.readline().strip();
                    if (name == "x0default0x"):
                        DownloadFile(socks, decrypted_message[13:].strip(), key_256, 2048);
                    else:
                        DownloadFile(socks, name, key_256, 2048);
                    #address_data = receive_message(socket)["data"];
                    #address_data = AESDecrypt(key_256, address_data).decode('utf-8');
                    prompt();
                    continue;
=======
>>>>>>> 2868e70a64e79addc0453fd46caf02d3197e2fe6
                print(f"{rusername} > {decrypted_message.decode('utf-8')}");
                prompt();
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("Reading error: {}".format(str(e)));
                    sys.exit();
                continue;
            except Exception as e:
                print("General Error {}".format(str(e)));
                sys.exit();
        else:
            message = sys.stdin.readline();
            if message:
<<<<<<< HEAD
                if message == "?:0x0VoIPtestcmd\n":
                    message = message.encode('utf-8');
                    message = AESEncrypt(key_256, message);
                    message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8');
                    client_socket.send(message_header + message);
                    voip_handle = VoIP(512, pyaudio.paInt32, 1, 44100);
                    voip_receive_thread = threading.Thread(target=voip_handle.receive_server_data, args=(socks, )).start();
                    voip_handle_thread = threading.Thread(target=voip_handle.send_data_to_server, args=(socks, key_256, )).start();
                elif message[:15] == "?:0x0FTPtestcmd":
                    ftp_flag = ("SFTP Initiate" + message[16:]).encode('utf-8');
                    send(client_socket, AESEncrypt(key_256, ftp_flag), "byte");
                    #prompt("Enter File Path: ");
                    #address = sys.stdin.readline().strip();
                    address = message[16:];
                    UploadFile(client_socket, address.strip(), key_256, 2048);
                    send(client_socket, AESEncrypt(key_256, "SFTP END".encode('utf-8')), "byte");
                    prompt();    
                else:
                    message = message.encode('utf-8');
                    message = AESEncrypt(key_256, message);
                    message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8');
                    client_socket.send(message_header + message);
                    prompt();
=======
                message = message.encode('utf-8');
                message = AESEncrypt(key_256, message);
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8');
                client_socket.send(message_header + message);
                prompt();
>>>>>>> 2868e70a64e79addc0453fd46caf02d3197e2fe6
