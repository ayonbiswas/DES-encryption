import binascii
# 64bit initial permutation
IPtable = (58, 50, 42, 34, 26, 18, 10, 2,
           60, 52, 44, 36, 28, 20, 12, 4,
           62, 54, 46, 38, 30, 22, 14, 6,
           64, 56, 48, 40, 32, 24, 16, 8,
           57, 49, 41, 33, 25, 17, 9, 1,
           59, 51, 43, 35, 27, 19, 11, 3,
           61, 53, 45, 37, 29, 21, 13, 5,
           63, 55, 47, 39, 31, 23, 15, 7)
#48bit key permutation
EPtable = (32, 1, 2, 3, 4, 5,
           4, 5, 6, 7, 8, 9,
           8, 9, 10, 11, 12, 13,
           12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21,
           20, 21, 22, 23, 24, 25,
           24, 25, 26, 27, 28, 29,
           28, 29, 30, 31, 32, 1)

#32bit SBOX OUTPUT PERMUTATION
PFtable = (16, 7, 20, 21, 29, 12, 28, 17,
           1, 15, 23, 26, 5, 18, 31, 10,
           2, 8, 24, 14, 32, 27, 3, 9,
           19, 13, 30, 6, 22, 11, 4, 25)

#64bit final inverse permutation
FPtable = (40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25)

#56bit key pre_permutation
PC1table = (57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4)
#48bit key final_permutation
PC2table = (14, 17, 11, 24,  1,  5,  3, 28,
            15,  6, 21, 10, 23, 19, 12,  4,
            26,  8, 16,  7, 27, 20, 13,  2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32)

sBox = 8 * [64 * [0]]

sBox[0] = (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
           0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
           4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
           15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13)

sBox[1] = (15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
           3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
           0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
           13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9)

sBox[2] = (10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
           13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
           13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
           1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12)

sBox[3] = (7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
           13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
           10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
           3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14)

sBox[4] = (2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
           14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
           4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
           11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3)

sBox[5] = (12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
           10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
           9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
           4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13)

sBox[6] = (4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
           13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
           1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
           6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12)

sBox[7] = (13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
           1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
           7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
           2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11)

LShift = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)

#initialisation vector
IV ='0000000000000000000000000000000000000000000000000000000000000000'
#key
k = '0000110000110010001011100101001100111101011110000110101011100011'
#length of input
length = 0
def permutate(original, fixed_key):
    new = ''
    c = len(original) - len(fixed_key)
    if c < 0:
        original = original.zfill(len(fixed_key))

    for i in fixed_key:

        new += original[i - 1]

    return new


def left_half(bits):
    return bits[:len(bits)/2]


def right_half(bits):
    return bits[len(bits)/2:]

def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return  rotated_right_half + rotated_left_half

def key_generate(k,t):
    bits = permutate(k,PC1table)
    for i in xrange(t):
        bits = shift(bits)
    return permutate(bits,PC2table)

def xor(bits, key):
    new = ''
    for bit, key_bit in zip(bits, key):
        new += str(((int(bit) + int(key_bit)) % 2))
    return new

def S(bits, i):
    row = int(bits[0] + bits[5], 2)

    col = int(bits[1] + bits[2]+bits[3]+bits[4], 2)

    return ('{0:02b}'.format(sBox[i][row * 16 + col])).zfill(4)

def F_right(bits, key):
    L = left_half(bits)
    R = right_half(bits)
    bits = permutate(R, EPtable)
    bits = xor(bits, key)
    s_output = ''

    for i in range(8):

        s_input = bits[6*i:6*(i+1)]
        s_buff = S(s_input,i)

        s_output = s_output+s_buff

    p_bits = permutate(s_output, PFtable)
    return xor(p_bits,L)

def F_left(bits, key):
    L = left_half(bits)
    R = right_half(bits)
    bits = permutate(L, EPtable)
    bits = xor(bits, key)
    s_output = ''

    for i in range(8):

        s_input = bits[6*i:6*(i+1)]
        s_buff = S(s_input,i)

        s_output = s_output+s_buff

    p_bits = permutate(s_output, PFtable)
    return xor(p_bits,R)

def encrypt(plain_text,t):
    bits = plain_text
    key = key_generate(k,t)

    temp = F_right(bits,key )
    return right_half(bits) + temp

def decrypt(cipher_text,t):
    bits = cipher_text
    key = key_generate(k,t)
    temp = F_left(bits, key)

    return temp + left_half(bits)

def block_cipher_encrypt(plain_text):

    bits = permutate(plain_text, IPtable)
    for i in xrange(16):
        t = LShift[i]

        bits = encrypt(bits,t)


    return permutate( bits, FPtable)

def block_cipher_decrypt(cipher_text):
    bits = permutate(cipher_text, IPtable)
    for i in xrange(16):
        t = LShift[15-i]
        bits = decrypt(bits,t)
    return permutate(  bits , FPtable)

def CBC_encrypt(plain_text):
    global length
    l = len(list(plain_text))
    length = l
    q = l//64
    r = l%64
    IV_xor = IV
    if(r >0):
        plain_text = plain_text.zfill(64*(q+1))
        q = q+1
    cipher = ""

    for i in xrange(q):
        enc_text = plain_text[i*64:64*(i+1)]
        enc_text = xor( enc_text , IV_xor)
        tt = block_cipher_encrypt(enc_text)
        cipher += tt
        IV_xor = tt

    return cipher

def CBC_decrypt(cipher_text):
    global length
    l = len(list(cipher_text))
    q = l // 64
    r = l % 64
    IV_xor = IV
    if (r > 0):
        cipher_text = cipher_text.zfill(64 * (q + 1))
        q = q + 1

    decipher = ""
    for i in xrange(q):

        dec_text = block_cipher_decrypt(cipher_text[i * 64:64 * (i + 1)])
        dec_text = xor(dec_text, IV_xor)
        decipher += dec_text
        IV_xor = cipher_text[i * 64:64 * (i + 1)]
    return decipher[q*64 - length:]


"""a = "0000000000110010001011100101001100111101011110000111110101010111111001010010101010"
#b = "1010100000110001001111010000100110010110101111100010100000011101"
B = "0000000000101000001010100101011111011001110101000101010100111111"
e = CBC_encrypt(a)
d = CBC_decrypt(e)"""
text = input()
n = bin(int(binascii.hexlify(text), 16))


n = str(n)
n = n[2:]

e = CBC_encrypt(n)
d = CBC_decrypt(e)
k = "0b"+str(d)

d = int(k, 2)

out = binascii.unhexlify('%x' % d)

print n
print e
print k


print int(n,2)-int(k,2)
print out

