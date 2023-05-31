import hashlib
import time
import uuid
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def hash_msg(msg):
    sha256 = hashlib.sha256()
    sha256.update(msg.encode('utf-8'))
    res = sha256.hexdigest()
    return res
 
def get_mac_address():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])
  
def create_license(key, data_str, s_file):
  license_bytes = bytes(data_str, 'utf-8')
  
  cipher = AES.new(key, AES.MODE_EAX)
  ciphertext, tag = cipher.encrypt_and_digest(license_bytes)
  
  file_out = open(s_file, "wb")
  [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
  file_out.close()
  
def open_license(key, s_file):
  file_in = open(s_file, "rb")
  nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
  file_in.close()
  
  # let's assume that the key is somehow available again
  cipher = AES.new(key, AES.MODE_EAX, nonce)
  data = cipher.decrypt_and_verify(ciphertext, tag)
  print("open_license data is {}" .format(data))
  return data

def time_data_to_stamp(time_data):
  time_data_str = time.strptime(time_data, "%Y-%m-%d %H:%M:%S)
  return time.mktime(time_data_str)

def check_license(data, local_license_dict):
  data_list = data.split("/")
  if data_list[0] == local_license_dict["mac"] and data_list[1] == local_license_dict['psw']:
    exp_time_stamp = time_data_to_stamp(data_list[1])
    if exp_time_stamp > local_license_dict['local_time']:
      return True
  else:
    return False
                                



  
