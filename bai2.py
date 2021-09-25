#Câu a
A=[1,1,2,3,5,8,13,21,34,55,88]
B=[1,3,5,4,7,88,66,59,40,54]
C=set(A)&set(B)
print("các phần tử trùng nhau là:",C)
#Câu b
A=set(A)-set(C)
B=set(B)-set(C)
print("A:",A)
print("B:",B)