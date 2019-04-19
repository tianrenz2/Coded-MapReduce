

def encrypt(filename):
    # Parameter is the file name to be converted to binary
    with open('master/' + filename, 'r') as f:
        content = f.read()
        # for c in content:
        #     print(c)
        binary = ' '.join(format(ord(str(x)), 'b') for x in content)
        return binary

def decrypt(bin_text):
    # Parameter is the binary string to convert back to text
    text = ''
    for ch in bin_text.split(' '):
        text += chr(int(ch, 2))
    return text

file_name = '1_2_1_4.txt'   #The name of the file in master directory

en_out = encrypt(file_name)
print("Converted binary value:\n", en_out)
print("Original content:\n", decrypt(en_out))