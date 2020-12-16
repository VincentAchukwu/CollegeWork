# Monday Sharks
#1a
fishpop = 20
for(i in c(2:300)){
  m=fishpop[i-1]/100
  fishpop[i] = fishpop[i-1] + rpois(1,m)
}
#length(fishpop)
plot(fishpop)

#1b
sharkpop = 100
for(i in c(2:300)){
  m=sharkpop[i-1]/100
  sharkpop[i] = sharkpop[i-1] - rpois(1,m)
}
plot(sharkpop)

#1c
sharkpop = 5
fishpop = 20
for(i in c(2:3000)){
  meanEat = (sharkpop[i-1]*fishpop[i-1])/1000
  neats=rpois(1,meanEat)
  
  mf=fishpop[i-1]/100
  fishpop[i] = fishpop[i-1] + rpois(1,mf) - neats
  if(fishpop[i] <= 0){
    fishpop[i] = 5
  }
  
  ms=sharkpop[i-1]/100
  sharkpop[i] = sharkpop[i-1] - rpois(1,ms) + neats
  if(sharkpop[i] <= 0){
    sharkpop[i] = 5
  }
}
plot(fishpop, ylim=c(0,50))
points(c(1:3000),sharkpop, col="red")

############# Thursday (Normal Dist) Mahalanobis Lab #################
#1
x1 = rnorm(1000, 0, 1.5)
y1 = rnorm(1000, 0, 0.5)
plot(x1,y1, xlim=c(-10,10), ylim=c(-10,10))

#2
x2 = rnorm(1000, -4, 0.5)
y2 = rnorm(1000, 0, 1.5)
points(x2,y2, col="red")

#3
mah21 = x2^2/1.5^2 + y2^2/0.5^2 # all distances in class 2 from class 1
mah22 = (x2+4)^2/0.5^2 + y1^2/1.5^2 # all distances in class 2 from itself
sum(mah22 < mah21)

mah11 = x1^2/1.5^2 + y1^2/0.5^2 # all distances in class 1 from itself
mah12 = (x1+4)^2/0.5^2 + y1^2/1.5^2 # all distances in class 1 from class 2
sum(mah11 < mah12)

#4
for(i in c(-10:10)){
  for (j in c(-10:10)){
    mah1 = i^2/1.5^2 + j^2/0.5^2
    mah2 = (i+4)^2/0.5^2 + j^2/1.5^2
    if(mah1 < mah2){
      points(i, j, col="black")
    }
    else{
      points(i, j, col="red")
    }
  }
}