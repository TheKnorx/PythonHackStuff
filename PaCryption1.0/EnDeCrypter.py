import os

# Library #
# Normal signs :
a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'
h = 'h'
i = 'i'
j = 'j'
k = 'k'
l = 'l'
m = 'm'
n = 'n'
o = 'o'
p = 'p'
q = 'q'
r = 'r'
s = 's'
t = 't'
u = 'u'
v = 'v'
w = 'w'
x = 'x'
y = 'y'
z = 'z'
_1 = '1'
_2 = '2'
_3 = '3'
_4 = '4'
_5 = '5'
_6 = '6'
_7 = '7'
_8 = '8'
_9 = '9'
_0 = '0'
z1 = '!'
z2 = '?'
z3 = '('
z4 = ')'
z5 = '='
z6 = '-'
z7 = '.'
z8 = ","
empty = ' '
# Encrypted Signs :
en_a = 'h'
en_b = 'a'
en_c = '.'
en_d = 'n'
en_e = 'b'
en_f = 'j'
en_g = 'p'
en_h = '4'
en_i = 'm'
en_j = ' '
en_k = 'c'
en_l = '7'
en_m = 'o'
en_n = '6'
en_o = 'l'
en_p = 'y'
en_q = 'i'
en_r = 'r'
en_s = ')'
en_t = 'x'
en_u = 'w'
en_v = 'u'
en_w = '9'
en_x = 't'
en_y = 'z'
en_z = '5'
en_1 = 'q'
en_2 = 'v'
en_3 = '2'
en_4 = '?'
en_5 = '\"'
en_6 = '-'
en_7 = '8'
en_8 = '1'
en_9 = 's'
en_0 = 'e'
en_z1 = '('
en_z2 = 'g'
en_z3 = 'f'
en_z4 = '!'
en_z5 = '/'
en_z6 = '3'
en_z7 = 'd'
en_z8 = "#"
en_empty = '='
# End Library #

while True:
    try:
        # os.system("cat Cryption.txt")
        print("Use Ctrl-D (i.e. EOF) to exit or (not recommended) Ctrl-C.")
        print("\n")
        print("Encrypter:        1")
        print("Decrypter:        2")
        print("\n")
        nC = input("Mode: ")
        try:
            nC = int(nC)
        except:
            continue
        if nC == 1:
            print("Encrypion-mode\n")
            print("Dont't use: §, $, %, &, _, ', *, ß, ~, {, }, [, ], ^, ′\n")
            input_text = input("Text to encrypt: ")
            input_text.lower()
            zerlegung_text = list(input_text)

            encrypted_text = ""

            for element in zerlegung_text:
                if element == a:
                    encrypted_text += en_a
                if element == b:
                    encrypted_text += en_b
                if element == c:
                    encrypted_text += en_c
                if element == d:
                    encrypted_text += en_d
                if element == e:
                    encrypted_text += en_e
                if element == f:
                    encrypted_text += en_f
                if element == g:
                    encrypted_text += en_g
                if element == h:
                    encrypted_text += en_h
                if element == i:
                    encrypted_text += en_i
                if element == j:
                    encrypted_text += en_j
                if element == k:
                    encrypted_text += en_k
                if element == l:
                    encrypted_text += en_l
                if element == m:
                    encrypted_text += en_m
                if element == n:
                    encrypted_text += en_n
                if element == o:
                    encrypted_text += en_o
                if element == p:
                    encrypted_text += en_p
                if element == p:
                    encrypted_text += en_q
                if element == r:
                    encrypted_text += en_r
                if element == s:
                    encrypted_text += en_s
                if element == t:
                    encrypted_text += en_t
                if element == u:
                    encrypted_text += en_u
                if element == v:
                    encrypted_text += en_v
                if element == w:
                    encrypted_text += en_w
                if element == x:
                    encrypted_text += en_x
                if element == y:
                    encrypted_text += en_y
                if element == z:
                    encrypted_text += en_z
                if element == _1:
                    encrypted_text += en_1
                if element == _2:
                    encrypted_text += en_2
                if element == _3:
                    encrypted_text += en_3
                if element == _4:
                    encrypted_text += en_4
                if element == _5:
                    encrypted_text += en_5
                if element == _6:
                    encrypted_text += en_6
                if element == _7:
                    encrypted_text += en_7
                if element == _8:
                    encrypted_text += en_8
                if element == _9:
                    encrypted_text += en_9
                if element == _0:
                    encrypted_text += en_0
                if element == z1:
                    encrypted_text += en_z1
                if element == z2:
                    encrypted_text += en_z2
                if element == z3:
                    encrypted_text += en_z3
                if element == z4:
                    encrypted_text += en_z4
                if element == z5:
                    encrypted_text += en_z5
                if element == z6:
                    encrypted_text += en_z6
                if element == z7:
                    encrypted_text += en_z7
                if element == z8:
                    encrypted_text += en_z8
                if element == empty:
                    encrypted_text += en_empty

            print("\nEncrypted Text:    ", encrypted_text)
            input("\nPress any Key to return to the main menu: \n")
        if nC == 2:
            print("Decryption-mode:\n")
            input_text = input("Text to decrypt: ")
            input_text.lower()
            encrypted_text = list(input_text)

            decrypted_text = ""

            for element in encrypted_text:
                if element == en_a:
                    decrypted_text += a
                if element == en_b:
                    decrypted_text += b
                if element == en_c:
                    decrypted_text += c
                if element == en_d:
                    decrypted_text += d
                if element == en_e:
                    decrypted_text += e
                if element == en_f:
                    decrypted_text += f
                if element == en_g:
                    decrypted_text += g
                if element == en_h:
                    decrypted_text += h
                if element == en_i:
                    decrypted_text += i
                if element == en_j:
                    decrypted_text += j
                if element == en_k:
                    decrypted_text += k
                if element == en_l:
                    decrypted_text += l
                if element == en_m:
                    decrypted_text += m
                if element == en_n:
                    decrypted_text += n
                if element == en_o:
                    decrypted_text += o
                if element == en_p:
                    decrypted_text += p
                if element == en_p:
                    decrypted_text += q
                if element == en_r:
                    decrypted_text += r
                if element == en_s:
                    decrypted_text += s
                if element == en_t:
                    decrypted_text += t
                if element == en_u:
                    decrypted_text += u
                if element == en_v:
                    decrypted_text += v
                if element == en_w:
                    decrypted_text += w
                if element == en_x:
                    decrypted_text += x
                if element == en_y:
                    decrypted_text += y
                if element == en_z:
                    decrypted_text += z
                if element == en_1:
                    decrypted_text += _1
                if element == en_2:
                    decrypted_text += _2
                if element == en_3:
                    decrypted_text += _3
                if element == en_4:
                    decrypted_text += _4
                if element == en_5:
                    decrypted_text += _5
                if element == en_6:
                    decrypted_text += _6
                if element == en_7:
                    decrypted_text += _7
                if element == en_8:
                    decrypted_text += _8
                if element == en_9:
                    decrypted_text += _9
                if element == en_0:
                    decrypted_text += _0
                if element == en_z1:
                    decrypted_text += z1
                if element == en_z2:
                    decrypted_text += z2
                if element == en_z3:
                    decrypted_text += z3
                if element == en_z4:
                    decrypted_text += z4
                if element == en_z5:
                    decrypted_text += z5
                if element == en_z6:
                    decrypted_text += z6
                if element == en_z7:
                    decrypted_text += z7
                if element == en_z8:
                    decrypted_text += z8
                if element == en_empty:
                    decrypted_text += empty

            print("\nDecrypted Text:     ", decrypted_text)
            input("\nPress any Key to return to the main menu: \n")
        if nC != 1 or 2:
            continue

    except EOFError:
        exit(1)
