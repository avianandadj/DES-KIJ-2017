PCONE = [57,  49,  41,  33,  25,  17,   9,
        1,  58,  50,  42,  34,  26,  18,
       10,   2,  59,  51,  43,  35,  27,
       19,  11,   3,  60,  52,  44,  36,
       63,  55,  47,  39,  31,  23,  15,
        7,  62,  54,  46,  38,  30,  22,
       14,   6,  61,  53,  45,  37,  29,
       21,  13,   5,  28,  20,  12,   4]

IP = [58,  50,  42,  34,  26,  18,  10,   2,
      60,  52,  44,  36,  28,  20,  12,   4,
      62,  54,  46,  38,  30,  22,  14,   6,
      64,  56,  48,  40,  32,  24,  16,   8,
      57,  49,  41,  33,  25,  17,   9,   1,
      59,  51,  43,  35,  27,  19,  11,   3,
      61,  53,  45,  37,  29,  21,  13,   5,
      63,  55,  47,  39,  31,  23,  15,   7]

PCTWO = [14,  17,  11,  24,   1,   5,
       3,   28,  15,   6,  21,  10,
       23,  19,  12,   4,  26,   8,
       16,   7,  27,  20,  13,   2,
       41,  52,  31,  37,  47,  55,
       30,  40,  51,  45,  33,  48,
       44,  49,  39,  56,  34,  53,
       46,  42,  50,  36,  29,  32]

E = [32,   1,   2,   3,   4,   5,
      4,   5,   6,   7,   8,   9,
      8,   9,  10,  11,  12,  13,
     12,  13,  14,  15,  16,  17,
     16,  17,  18,  19,  20,  21,
     20,  21,  22,  23,  24,  25,
     24,  25,  26,  27,  28,  29,
     28,  29,  30,  31,  32,   1]

LSHIFT_MAP = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

SBOXES = {0:
            [[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
             [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
             [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
             [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]],
          1:
            [[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
             [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
             [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
             [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]],
          2:
            [[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
             [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
             [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
             [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]],
          3:
            [[ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
             [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
             [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
             [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]],
          4:
            [[ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
             [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
             [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
             [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]],
          5:
            [[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
             [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
             [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
             [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]],
          6:
            [[ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
             [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
             [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
             [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]],
          7:
            [[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
             [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
             [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
             [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]}

P = [16,   7,  20,  21,
     29,  12,  28,  17,
      1,  15,  23,  26,
      5,  18,  31,  10,
      2,   8,  24,  14,
     32,  27,   3,   9,
     19,  13,  30,   6,
     22,  11,   4,  25]

IP_INVERSE = [40,   8,  48,  16,  56,  24,  64,  32,
              39,   7,  47,  15,  55,  23,  63,  31,
              38,   6,  46,  14,  54,  22,  62,  30,
              37,   5,  45,  13,  53,  21,  61,  29,
              36,   4,  44,  12,  52,  20,  60,  28,
              35,   3,  43,  11,  51,  19,  59,  27,
              34,   2,  42,  10,  50,  18,  58,  26,
              33,   1,  41,   9,  49,  17,  57,  25]


def initialpermutation(input):
    hasilIP = ""
    for bit in IP:
         hasilIP += input[bit-1]
    return hasilIP

def IPInverse(input):
    hasilIPInverse = ""
    for bit in IP_INVERSE:
         hasilIPInverse += input[bit-1]
    return hasilIPInverse


def PC1(input):
    hasilPCONE = ""
    for bit in PCONE:
        # print bit
        hasilPCONE += input[bit-1]
    return hasilPCONE

def PC2(input):
    hasilPC2 = ""
    for bit in PCTWO:
        # print bit
        hasilPC2 += input[bit-1]
    return hasilPC2

def EPerm(input):
    hasilEPerm = ""
    for bit in E:
        # print bit
        hasilEPerm += input[bit-1]
    return hasilEPerm

def lshift(c, d):
    cidi = []
    k = []
    for i in xrange(16):
        if LSHIFT_MAP[i] == 1:
            c = '%s%s' % (c[1:], c[0])
            d = '%s%s' % (d[1:], d[0])
        else:
            c = '%s%s' % (c[2:], c[0:2])
            d = '%s%s' % (d[2:], d[0:2])
        cidi.append(c+d)
        k.append(PC2(cidi[i]))
    return (cidi, k)

def xor(k, hasilEPerm):
    bits = []
    # print k
    for i in xrange(len(hasilEPerm)):
        b1 = int(k[i])
        b2 = int(hasilEPerm[i])
        xor_bit = int(bool(b1) ^ bool(b2))
        bits.append(xor_bit)

    return ''.join(map(str, bits))

def PPermutation(input):
    hasilPPerm = ""
    for bit in P:
        # print bit
        hasilPPerm += input[bit-1]
    return hasilPPerm

def iterations(r0, k):
    E = EPerm(r0)
    f = []
    hasilxor = xor(k, E)
    # print k, E
    s = []
    for n in xrange(len(hasilxor) / 6):
        start = 6 * n
        end = (6 * n) + 6
        b = hasilxor[start:end]
        i = int(b[0])*2**1 + int(b[-1])*2**0
        j = (int(b[1])*2**3 + int(b[2])*2**2 + int(b[3])*2**1 + int(b[4])*2**0)
        s.append(str(bin(SBOXES[n][i][j]))[2:].rjust(4, '0'))
    s = ''.join(s)

    f = PPermutation(s)
    return f

def run():
    IV = '0000000000000000000000000000000000000000000000000000000000000000'
    # print len(IV)
    #input plain message
    plainbin = ''
    arrayplain = []
    plain = raw_input('Enter your input:')
    for i in xrange(0, len(plain), 8):
        msg_block = plain[i:i+8]
        arrayplain.append(msg_block)
    # print arrayplain[len(arrayplain)-1]

    if len(plain) % 8 == 0:
        arrayplainbin = []
        for plain in arrayplain:
            for x in plain:
                plainbin += format(ord(x), '08b')
            arrayplainbin.append(plainbin)
            plainbin = ''
    else:
        if len(plain) < 8:
            for loop in range(0, abs(len(plain)-8)):
                plain = plain+'0'

            arrayplainbin = []
            for x in plain:
                plainbin += format(ord(x), '08b')
            arrayplainbin.append(plainbin)
            plainbin = ''
        else:
            for loop in range(0, abs(len(arrayplain[len(arrayplain)-1])-8)):
                arrayplain[len(arrayplain)-1] = arrayplain[len(arrayplain)-1]+'0'
            arrayplainbin = []
            for plain in arrayplain:
                for x in plain:
                    plainbin += format(ord(x), '08b')
                arrayplainbin.append(plainbin)
                plainbin = ''


    #input key
    key = raw_input('Enter your key:')
    keybin = ''
    for x in key:
        keybin += format(int(x, 16), '04b')
    keybin = [keybin[i:i+8] for i in range(0, len(keybin), 8)]
    keybin = ''.join(keybin)

    crypto = []
    for binmsg in range(0, len(arrayplainbin)):
        #permutationcompression-1
        hasilPC1 = PC1(keybin)
        c0 = hasilPC1[:len(hasilPC1)/2]
        d0 = hasilPC1[len(hasilPC1)/2:]
        #get CiDi and K+
        (cd, k) = lshift(c0, d0)

        #initialpermutation
        # print arrayplainbin[binmsg]
        message = xor(arrayplainbin[binmsg], IV)
        hasilIP = initialpermutation(message)
        l0 = hasilIP[:len(hasilIP)/2]
        r0 = hasilIP[len(hasilIP)/2:]
        l = [l0, r0]
        r = [r0]
        for round_i in range(0,len(k)):
            f = iterations(r0, k[round_i])
            r.append(xor(l[round_i], f))
            l.append(r[round_i+1])
            r0 = r[round_i+1]
        binerakhir = IPInverse(r[16]+l[16])
        crypto.append(hex(int(binerakhir, 2))[2:])
        binerakhir = IV
    crypto = ''.join(crypto)
    print crypto

if __name__ == '__main__':
    run()
