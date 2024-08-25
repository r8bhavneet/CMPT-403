import subprocess
import sys
import secrets
import time


def query_oracle(ciphertext, byte_string):
    with open(ciphertext, 'wb') as c:
        c.write(byte_string)
    result = subprocess.check_output(['python3', 'oracle.py', ciphertext])
    return result[0]



def decrypt_block(block, iterate):

    # Extract yN and yN-1 from the ciphertext
    y_N_blocks = (-16 * iterate)

    if iterate == 1:
        y_N = block[y_N_blocks:]
    else:
        y_N = block[y_N_blocks: y_N_blocks + 16]

    # y_N = block[-16:]  # Last 16 bytes
    y_N_prev = block[y_N_blocks - 16 : y_N_blocks]  # Second to last 16 bytes
    
    # y_N = block[-16:]
    
    
    
    random_string = b''
    for i in range(15):
        random_string += secrets.token_bytes(1)
   
    
    decrypt_y_N_16 = None
    combined = b''
    count =0
    for i in range(256):
        combined = random_string + bytes([i]) + y_N
        filename = 'output'
        result = query_oracle(filename, combined)
        # print('hello: ', result)
        if result == 48:
            continue
        else:
            for j in range (15):
                byte = bytearray(combined)
                byte[j] = secrets.token_bytes(1)[0]
                byte_string = bytes(byte)
                result2 = query_oracle(filename, byte_string)

                if result2 == 48:
                    decrypt_y_N_16 = i ^ (17 - (j + 1))
                    break
                elif j < 14:
                    continue
                else:
                    decrypt_y_N_16 = i ^ 1
                    break
            break
    x_N_16 = decrypt_y_N_16 ^ y_N_prev[-1]

    return bytes([x_N_16]), bytes([decrypt_y_N_16]), byte_string

def decrypt_remaining_bytes(block, iterate, byte_s,  decrypt, byte_string):

    # Extract yN and yN-1 from the ciphertext
    y_N_blocks = (-16 * iterate)
    

    if iterate == 1:
        y_N = block[y_N_blocks:]
    else:
        y_N = block[(y_N_blocks): (y_N_blocks+16)]

    # y_N = block[-16:]  # Last 16 bytes
    y_N_prev = block[(y_N_blocks - 16):y_N_blocks]  # Second to last 16 bytes

    modified_byte = bytearray(decrypt)
    modified_byte[-1] = modified_byte[-1] ^ (17 - (byte_s + 1))
    decrypt_new = bytes(modified_byte)
    
    random_string = b''
    for i in range(byte_s):
        random_string += secrets.token_bytes(1)

    decrypt_y_N_k = None
    k = 0
    combined = b''
    while True:
       
        combined = random_string + bytes([k]) + decrypt_new + y_N
        filename = 'output1'
        result = query_oracle(filename, combined)
        if result == 48:
            k += 1
            continue
        else:
            decrypt_y_N_k = k
            break
    
    x_N_k = decrypt_y_N_k ^ y_N_prev[byte_s]
    return bytes([x_N_k]), bytes([decrypt_y_N_k])


def decrypt(ciphertext):

    total_bytes = len(ciphertext)
    total_blocks = total_bytes // 16 
    x = b''
    
    count = 0
    for i in range(1, total_blocks):
        
        decrypt = b''
        x_N = b''

        count = count + 1
        print(count) 

        x_N_16, decrypt_N_16, byte_string = decrypt_block(ciphertext, i)
        x_N += x_N_16
        decrypt += decrypt_N_16
        print(f"x_N block: {x_N}, first decrypt: {decrypt}")

        for byte in reversed(range(15)):
            x_N_new, decrypt_new = decrypt_remaining_bytes(ciphertext, i, byte,  decrypt, byte_string)
            x_N = x_N_new + x_N
            decrypt = decrypt_new + decrypt
        
        x = x_N + x

    message = x.decode('utf-8')
    output_file = 'plaintext.txt'  # Specify your file path/name here
    with open(output_file, 'w') as file:
        file.write(message)
    print(message)

    




if __name__ == '__main__':
   start_time = time.time()
   with open(sys.argv[1], 'rb') as f:
        ciphertext = f.read()
   decrypt(ciphertext)
   end_time = time.time()
   print(f"took {end_time - start_time} seconds")
   sys.exit()

