ranlet(){
echo -en "
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
0
1
2
3
4
5
6
7
8
9" > "chars"
while true
do
clear
i="0"
while [ "$i" -lt "100" ]
do echo -n "$(shuf chars -n 1)"
let i++
done
read -s
done
}