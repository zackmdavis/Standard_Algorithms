require 'digest'

def hmac(message, key, hash_function)
  # we use a hash function that ultimately operates on fixed-size
  # blocks; this is that fixed size
  block_size = hash_function.new.block_length

  # If the supplied key is longer than the input block size of the
  # underlying hash function, then let's use the hash of the key in
  # the following
  if key.length > block_size
    key = hash_function.digest key
  end

  # pad the key with null bytes to the block length
  key += "\x00" * (block_size - key.length)

  # key XOR 5c5c5c... (one of the arbitrary constants specified by the
  # RFC 2104 standard)
  outer = key.each_byte.map{ |byte| (byte ^ "\x5c".ord).chr }.join

  # key XOR 363636... (the other arbitrary constant specified by the
  # standard)
  inner = key.each_byte.map{ |byte| (byte ^ "\x36".ord).chr }.join

  hash_function.hexdigest(outer + hash_function.digest(inner + message))
end


puts `python3 -c 'import hashlib, hmac; print(hmac.HMAC(b"key", b"The quick brown fox jumps over the lazy dogs", hashlib.sha1).hexdigest(), "  canonical")'` 

my_hmac = hmac('The quick brown fox jumps over the lazy dogs', 'key', Digest::SHA1)
puts "#{my_hmac}   mine"
