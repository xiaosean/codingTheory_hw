# Date: 20161231
# Author: b10315007 林詠翔
# 
# win10 64bits
# python 3.5 use numpy
# use cmd input next line will install numpy
# pip install numpy
# 
# referenced
# https://isite.tw/2015/03/18/13087

import numpy as np

# 若 Parity Check Bits 的數量為 R，原始資料長度為 K，總資料長度為 N，則 2**R ≧ K + R + 1。
def getR(num):
	R = 0
	while q**R < num:
		R += 1
	print("check bits R =", R)
	return R
def get_C_pos(index):
	return  k + index
# get I
def get_indentify_matrix(size):
	c = np.zeros((size, size), int)
	for i in range(size):
		c[i][i] = 1
	return c
def find_mat_ind_by_row(src_mat, find_row):
	for index, row in enumerate(src_mat):
		# print("row[k:]", row[k:], "find row", find_row)
		if(str(row[k:]) == str(find_row)):
			return index
	raise "getMatchIndex error"
# -----------------------------------
# example
# q = 2
# n = 18
# dim_k = 4



# ----------------------------
# hw input
# input r
# input_r = 2
# base
# q = 3
# code_length
# n = int((3**input_r-1)/2)
# dim_k = (3**input_r - input_r - 1)/2
# [n, dim)k, d]
# print("[%d, %d, 3]" % (n, dim_k))

input_r = int(input("請輸入r 當r>3時 可能會有記憶體不足的訊息。 : "))
q = 3
n = int((3**input_r-1)/2)
dim_k = (3**input_r - input_r - 1)/2
print("[n, k, d] = [%d, %d, 3]" % (n, dim_k))

# check bits numbers
r = getR(n)
# data bits numbers
k = n - r
# create a matrix for codeword
c = np.zeros((q ** k, n), int)
# print(c)
# create a q-nary code
for x in range(int(q ** k)):
	temp = x
	for index in range(n):
		k_lastIndex = n - index - r - 1
		c[x][k_lastIndex] = temp % q
		temp /= q
debug_index = 2
# generate check bits
for index, row in enumerate(c):
	if(index == debug_index):
		print(row)
	# iterator find each checkbits
	for checkbits_pos in range(r):
		data_sum = 0
		# get equation
		for data_index in range(k):
			# print(k - 1 - checkbits_pos)
			if(data_index != k - 1 - checkbits_pos ):
				# if(index == debug_index):
				# 	print("data_index =", data_index, " checkbits_pos=", checkbits_pos ," row[", data_index , "] = ", row[data_index] )
				data_sum += row[data_index] 
		# if(index == debug_index):
		# 	print("data_index =", data_index-1, "sum = ", data_sum)
		i_check_bit = (q - (data_sum % q)) % q
		row[k+ checkbits_pos] = i_check_bit
# get k*k IndentifyMatrix
K_I = get_indentify_matrix(r)
print(K_I)
# find the row which in checkbits is a row in I  
H_list = [find_mat_ind_by_row(c, I_row) for I_row in K_I]
print(c)
# print(H_list)
H = np.array([c[index] for index in H_list], dtype=int)
print("H = \n", H)
P = np.array([row[0:k] for row in H], dtype=int)
print("p = \n",P)
print("p.transpose = \n", P.transpose())
G = np.concatenate((get_indentify_matrix(k), (q - P)% 3), axis=0).transpose()
G.astype(int)
print("G = \n", G)
G = np.matrix(G)
H = np.matrix(H)
# print("G * H\n", np.multiply(G, H.transpose()) % q)
# print(np.multiply(G, H.transpose()))
print("G * H\n",G * H.transpose() % q)