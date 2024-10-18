import base64

# Original string
Str = "this is string example....wow!!!"

# Encode the string to bytes, then to base64
encoded_bytes = base64.b64encode(Str.encode('utf-8'))
encoded_str = encoded_bytes.decode('utf-8')

# encoded_str = encoded_bytes.decode('utf-8') is used so that the encoded string can be printed by decoding it from bytes

print("Encoded String: ", encoded_str)

# Decode the base64 back to bytes, then to string
decoded_bytes = base64.b64decode(encoded_bytes)
decoded_str = decoded_bytes.decode('utf-8')

# decoded_str = decoded_bytes.decode('utf-8') is used so that the decoded string can be printed by decoding it from bytes

print("Decoded String: ", decoded_str)
