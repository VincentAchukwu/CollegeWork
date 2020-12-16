# Hypergeometric Distribution Lab Monday
#1a
# with replacement
sample(c(rep(0,15), rep(1,5)), 5, replace=T)
# without replacement
sample(c(rep(0,15), rep(1,5)), 5, replace=F)

#1b&c
#with replacement (replace=T)
x = 0
for(i in c(1:10000)){
  x[i] = sum(sample(c(rep(0,15), rep(1,5)), 5, replace=T))
}
table(x)
plot(c(0:5), table(x))
points(c(0:5), dbinom(c(0:5), 5, 0.25)*10000, col="red")

# without replacement (replace=F)
y = 0
for(i in c(1:10000)){
  y[i] = sum(sample(c(rep(0,15), rep(1,5)), 5, replace=F))
}
table(y)
#plot(c(0:5), table(y))
points(c(0:5), dhyper(c(0:5), 5, 15, 5) * 10000, col="turquoise")

#1d
#done above with points ^^^
# with replacement
#dbinom(c(0:5), 5, prob=5/20)

#without replacement
#dhyper(c(0:5), 5, 15, 5)
