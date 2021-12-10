import numpy


def make_fail_table(pattern, character_dict):


    M = len(pattern)
R = len(character_dict)
dfa = numpy.zeros([R, M], int)
dfa[character_dict.get(pattern[0])][0] = 1
X = 0
for j in range(1, M):
    for c in range(0, R):
        dfa[c][j] = int(dfa[c][X])
        dfa[character_dict.get(pattern[j])][j] = j + 1
        X = int(dfa[character_dict.get(pattern[j])][X])
return dfa


def KMP_Search(text, pattern, character_dict):


# You need to modify the code below to search to index M-N
# and return a list of all matches found, not just the first match
dfa = make_fail_table(pattern, character_dict)
N = len(text)
M = len(pattern)
i = 0
for j in range(0, N):
    while j < M and i < N:
    j = dfa[character_dict.get(text[i])][j]
i += 1
if (j == M):
    print("Matches found at index:" + str(i - M))
else:
return N
# Driver code
text = 'GCATTAGCAGATTACATAGGAGAGAAGGATCCATACAGACAGACGTATATGGATCCAACATGCATAGCATAAGAGTTAAGATAGCAAGCAGGATCCAAGCATCAGCATAGCA'
pattern = 'GGATCC'
character_dict = {'G': 0, 'A': 1, 'T': 2, 'C': 3}
match = KMP_Search(text, pattern, character_dict)
print(match)
