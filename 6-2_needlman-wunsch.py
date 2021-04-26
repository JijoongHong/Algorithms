# import module
import numpy as np

# set sequences
# s1 = "TAAGGTCA"
# s2 = "AACAGTTACC"

s1 = "qbcdty"
s2 = "abcdefg"


# create matices
main_matrix = np.zeros(((len(s1) + 1), (len(s2) + 1)))
match_checker_matrix = np.zeros((len(s1), len(s2)))

# set panalties
match = 1
mismatch = -1
gap = -1

# fill the match checker matrix according to match or mismatch
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            match_checker_matrix[i][j] = match
        else:
            match_checker_matrix[i][j] = mismatch

print("/-------------match checker matrix-------------/\n")
print(match_checker_matrix)

# filling up the matrix using Needleman-Wunsch algorithm
# STEP 1 : Initialization
for i in range(len(s1) + 1):
    main_matrix[i][0] = i * gap
for j in range(len(s2) + 1):
    main_matrix[0][j] = j * gap

# STEP 2 : Matrix filling
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        main_matrix[i][j] = max(main_matrix[i-1][j-1]+match_checker_matrix[i-1][j-1],
                                main_matrix[i-1][j]+gap,
                                main_matrix[i][j-1]+gap)

print("/-------------main matrix-------------/\n")
print(main_matrix)

# STEP 3 : Traceback
a1 = ""
a2 = ""
ti = len(s1)
tj = len(s2)

while(ti > 0 and tj >0):
    if (ti > 0 and tj > 0 and main_matrix[ti][tj] == main_matrix[ti-1][tj-1] + match_checker_matrix[ti-1][tj-1]):
        a1 = s1[ti-1] + a1
        a2 = s2[tj-1] + a2
        ti = ti - 1
        tj = tj - 1

    elif (ti > 0 and main_matrix[ti][tj] == main_matrix[ti-1][tj] + gap):
        a1 = s1[ti-1] + a1
        a2 = "-" + a2
        ti = ti - 1
    else :
        a1 = "-" + a1
        a2 = s2[tj-1] + a2
        tj = tj - 1

# Test
print(a1)
print(a2)