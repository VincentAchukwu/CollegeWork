#1
prod(26:21) / (26 ** 6)

#2
prod(26:21) / prod(6:1)

#how to generate random 6 letter passwords
sample(letters, 6, replace=F)

#3
x=0
for (i in c(1:10000)){
  x[i] = sample(c("H","T"), 1, replace = T)
}
table(x)

#4
prod(60:56) / prod(100:96)

#5
l=0
for (i in c(1:10000)){
  s = sample(c(rep("f",60), rep("m",40)), 5, replace = F)
  l[i] = sum(s=="f")
}
table(l)
boxplot(l, col="purple")
hist(l, breaks=5, col="turquoise")

###################################
#past paper q1 b-e
#b
(choose(15,5) + choose(10,5) + choose(5,5)) / choose(30,5)

#c
(choose(15,2) * choose(15,3)) / choose(30,5)

#d

s=sample(c(rep("r",15),rep("g",10),rep("b",5)), 5, replace=F)
#cant' remember how he got table laid out...
