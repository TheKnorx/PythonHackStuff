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

input_text = input(": ")
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

print(encrypted_text)
