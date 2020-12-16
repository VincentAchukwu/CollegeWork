####### 2018 1b #######MONDAY
#i
#P(A=15)
.1+.15+.1

#P(District=Centre)
.1+.15+.05+.05

#P(Age=15 | District=Centre)
0.15/0.35

#P(Age=15 & District=Centre)
0.15

#P(Age=15 or District=Centre)
(0.35+0.35)-0.15

#ii
#mean
m = (0.3*14)+(0.35*15)+(0.15*16)+(0.2*17)

#variance
v = (0.3*(14-m)^2) + (0.35*(15-m)^2) + (0.15*(16-m)^2) + (0.2*(17-m)^2)

######## THURSDAY --> Monday week 8 #########
#Geometric distribution WAITING TIMES
#2a
sample(c(0,1), 60, prob=c(0.9,0.1), replace=T)

#2b&c
x=0
for(i in c(1:10000)){
  s = sample(c(0,1), 60, prob=c(0.9,0.1), replace=T)
  j=1
  while(s[j]==0 & j<=60){
    j = j + 1
  }
  x[i] = j
}
#length(x)
table(x)
plot(table(x), col="turquoise")
points(c(1:61),dgeom(c(0:60),0.1)*10000)

#d
x=0
for(i in c(1:10000)){
  s = sample(c(0,1),60,prob=c(0.9,0.1),replace=T)
  x[i] = sum(s)
}
plot(table(x),col="red")
dbinom(x=c(0:17), prob=0.1,size=60)
points(c(0:17), dbinom(x=c(0:17), prob=0.1,size=60) *10000)

###### Queue Simulation ######
#1
q1=0
q1[1]=0

q2=0
q2[1]=0

for(i in c(2:10000)){
  a = sample(c(0,1),60,prob=c(58/60,2/60),replace=T)
  d1 = sample(c(0,1),60,prob=c(59/60,1/60),replace=T)
  d2 = sample(c(0,1),60,prob=c(59/60,1/60),replace=T)

  if(q1[i-1] <= q2[i-1]){
    q1[i] = q1[i-1] + sum(a) - sum(d1)
    q2[i] = q2[i-1] - sum(d2)
  }
  else{
    q1[i] = q1[i-1] - sum(d1)
    q2[i] = q2[i-1] + sum(a) - sum(d2)
  }

}
plot(q1)
points(c(1:10000), q2,col="turquoise")