

def encrypt(filename):
    # Parameter is the file name to be converted to binary
    with open('master/' + filename, 'r') as f:
        content = f.read()
        # for c in content:
        #     print(c)
        bin_form = []
        for x in content:
            o = str(format(ord(str(x)), 'b'))
            if(len(o) < 7):
                o = '0'*(7-len(o)) + o
            bin_form.append(o)
        binary = ' '.join(bin_form)
        return binary

def decrypt(bin_text):
    # Parameter is the binary string to convert back to text
    text = ''
    for ch in bin_text.split(' '):
        ascii_code = int(ch, 2)
        if(ascii_code > 0):
            text += chr(ascii_code)
    return text

def xorTowFiles(fileA, fileB):
    ec_fileA, ec_fileB = encrypt(fileA),  encrypt(fileB)
    return Xor(ec_fileA, ec_fileB)


def Xor(ecA, ecB):
    output = []
    ec_fileA, ec_fileB = ecA.split(' '), ecB.split(' ')
    l_a, l_b = len(ec_fileA), len(ec_fileB)
    if (l_a > l_b):
        output = ec_fileA[:l_a - l_b]
        ec_fileA = ec_fileA[l_a - l_b:]
    elif (l_a < l_b):
        output = ec_fileB[:l_b - l_a]
        ec_fileB = ec_fileB[l_b - l_a:]

    for a, b in zip(ec_fileA, ec_fileB):
        output.append(bin(int(a, base=2) ^ int(b, base=2))[2:].zfill(7))
    return ' '.join(output)




file_nameA = '1_2_1_4.txt'   #The name of the file in master directory
file_nameB = '1_2_1_1.txt'

# en_out = encrypt(file_name)
# print("Converted binary value:\n", en_out)
# print("Original content:\n", decrypt(en_out))

fileA_ec = encrypt(file_nameA)
fileB_ec = encrypt(file_nameB)

print(fileA_ec)
print(fileB_ec)

res_C = xorTowFiles('1_2_1_4.txt', '1_2_1_1.txt')

out_txt = decrypt(res_C)

with open("master/out.txt", 'w') as f:
    f.write(out_txt)

print("The converted data is")
print(res_C)

print("\n Recovered: \nThe file 1 is")
print()

recover_out = decrypt(Xor(res_C, fileA_ec))

with open("master/recover_out.txt", 'w') as f:
    f.write(recover_out)