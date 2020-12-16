###### Monday ########
##1
#a
virus=0
test=0
for(i in c(1:10000)){
  if(runif(1) < 0.15){
    # Has virus
    virus[i] = 1
    if(runif(1) < 0.95){
      # Has virus, positive result
      test[i] = 1
    }
    else{
      # Has virus, negative result
      test[i] = 0
    }
  }
  else{
    # No virus
    virus[i]=0
    if(runif(1) < 0.02){
      test[i]=1
      # No virus, positive result
    }
    else{
      # No virus, negative result
      test[i]=0
    }
  }
}
# the probability of having the virus given a positive test is
sum(test & virus)/sum(test)

#prob getting pos result
sum(test)/10000

# prob 
sum(!test & virus)/sum(!test)

table(virus)
table(test)


###### Thursday ########
#P(H | P1^P2)
#first find prob P(P1^P2)
(0.15*0.95*0.95) + (0.85*0.02*0.02)
#so..
(0.15*0.95*0.95) / ((0.15*0.95*0.95)+(0.85*0.02*0.02))

#P(H | P1^P2)
#find probability of pos and neg..
#..if they have/don't have virus, add them
(0.95*0.05*0.15) / ((0.15*0.95*0.05) + (0.85*0.02*0.98))

### BayesNet Tutorial Sheet #### (Thursday/ week 6 Monday)
#P(H) (i)
(0.8*0.3*0.4) + (0.5*0.7*0.4) + (0.4*0.3*0.6) + (0.1*0.7*0.6)

#P(B) (ii)
(0.35 * 0.7) + (0.65 * 0.1)

#P(H | B) (iii)
(0.7 * 0.35) / 0.31

#P(B ^ E) (iv)
(0.7*0.8*0.35) +(0.1*0.1*0.65)

#P(H|B ^ E) (v)
(0.7*0.8*0.35) / 0.2025

#P(H|B ^ !E) (vi)
#first find P(B ^ !E)
(0.7*0.2*0.35) + (0.1*0.9*0.65)
(0.7*0.2*0.35) / 0.1075

#P(H|S) (vii)
(0.8*0.4) + (0.4*0.6)

#P(E|S) (viii)
(0.56*0.8) + (0.1*(1-0.56))

#P(H|E ^ S) (ix)
(0.3*0.56*0.8) / (0.3*0.492)
