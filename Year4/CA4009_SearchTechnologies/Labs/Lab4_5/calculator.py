import math

# terms for calculating ow(i)
ti = ["compani", "industri", "secret", "war", "countri"]

# number of documents term t(i) occurs in
ni = [158337, 199735, 12441, 40885, 229732]

# total number of documents in the collection archive
N = 500000

# total number of known relevant documents in the collection archive
R = 5

# number of known relevant documents term t(i) occurs in
ri = [4, 5, 3, 1, 5]

# now we calculate rw(i)
for i in range(len(ti)):
    eqn = ((ri[i] + 0.5) * (N - ni[i] - R + ri[i] + 0.5)) / ((ni[i] - ri[i] + 0.5) * (R - ri[i] + 0.5))
    rwi = math.log(eqn)
    owi = ri[i] * rwi
    print("{}: rw(i) = {}, owi = {}".format(ti[i], str(rwi), str(owi)))
