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

LSHIFT_MAP = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def initialpermutation(input):
    hasilIP = ""
    for bit in IP:
         hasilIP += input[bit-1]
    return hasilIP

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

def lshift(c, d):
    for i in xrange(16):
        if LSHIFT_MAP[i] == 1:
            c = '%s%s' % (c[1:], c[0])
            d = '%s%s' % (d[1:], d[0])
        else:
            c = '%s%s' % (c[2:], c[0:2])
            d = '%s%s' % (d[2:], d[0:2])
        # print c,d
        cidi = c+d
        hasilPC2 = PC2(cidi)
        print hasilPC2 

    return (c, d)

    # plain = raw_input('Enter your input:')
def run():
    # plainbin = ''
    # for x in plain:
    #     plainbin += format(ord(x), '08b')
    # # plainbin = plainbin.split(' ')
    # # print plainbin
    #
    key = raw_input('Enter your key:')
    keybin = ''
    for x in key:
        keybin += format(int(x, 16), '04b')
    keybin = [keybin[i:i+8] for i in range(0, len(keybin), 8)]
    keybin = ''.join(keybin)
    # print keybin

    # hasilIP = initialpermutation(plainbin)
    # l0 = hasilIP[:len(hasilIP)/2]
    # r0 = hasilIP[len(hasilIP)/2:]

    hasilPC1 = PC1(keybin)
    c0 = hasilPC1[:len(hasilPC1)/2]
    d0 = hasilPC1[len(hasilPC1)/2:]
    # print c0

    (c, d) = lshift(c0, d0)


if __name__ == '__main__':
    run()
