from eth_keys import keys
from eth_utils import to_checksum_address
from hashlib import pbkdf2_hmac

class EthAccount:
  @property
  def private_key(self):
    return self._private_key
  
  @property
  def public_key(self):
    return self._public_key
  
  @property
  def eth_address(self):
    return self._eth_address
  
  def __init__(self, private_key, public_key, eth_address):
    self._private_key = private_key
    self._public_key = public_key
    self._eth_address = eth_address

def stretch_word_to_32_bytes_using_kdf(word):
  word_bytes = word.encode('utf-8')
  salt = b'unique_salt' # no need to be secure
  iterations = 1000000
  # Derive a 32-byte key from the input word using PBKDF2
  key = pbkdf2_hmac('sha256', word_bytes, salt, iterations, dklen=32)
  return key

def from_keyword_to_private_key_hex(keyword):
  stretched_key = stretch_word_to_32_bytes_using_kdf(keyword)
  return stretched_key.hex()

def from_word_to_account(word):
  private_key_hex = from_keyword_to_private_key_hex(word)
  private_key = keys.PrivateKey(bytes.fromhex(private_key_hex))
  public_key = private_key.public_key
  eth_address = to_checksum_address(public_key.to_address())
  return EthAccount(private_key_hex, public_key.to_hex(), eth_address)

def get_ith_account(keyword, i):
  word = keyword + "-test-" + str(i)
  return from_word_to_account(word)