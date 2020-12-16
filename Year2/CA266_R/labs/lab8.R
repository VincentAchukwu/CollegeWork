#Thursday lab (Binomial Dist) 2019 Q2a
#i
db = dbinom(x=c(0:6), prob=0.5, size=6)
#ii
4/6
#iii
((4/6)*(db[5])) / 0.5
#iv
1/10 # ?assuming the question means P(first exp has 6 heads given 10th has 6 heads..)

#v
1 - pbinom(4,6,prob=0.5) # or just the sum of last 2 from 1st q.
#vi
#mean
heads = c(0:6)
m = sum(db * heads)
# or np (trials * prob success)
m = 6*0.5

#variance
v = sum((heads-m)^2 * db)
# or n*p*(1-p)
v = 6 * 0.5 * 0.5