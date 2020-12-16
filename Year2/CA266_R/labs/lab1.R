setwd("C:/Users/vince/College/SecondYear/ca266_R")
results <- read.table("C:/Users/vince/College/SecondYear/ca266_R/Results.txt", header = T)
summary(results)

attach(results)
par (mfrow = c(2,2))
hist(arch1, xlab = "Architecture",
     main = "Semester 1", ylim = c(0,35), col="purple")
hist(arch2, xlab = "Architecture",
     main = "Semester 2", ylim = c(0,35), col="yellow")
hist(prog1, xlab = "Programming",
     main = "Semester 1", ylim = c(0,35), col="yellow")
hist(prog2, xlab = "Programming",
     main = "Semester 2", ylim = c(0,35), col="purple")

stem(prog1)
plot(prog1,prog2, xlab = "Programming 1", ylab = "PRogramming 2")
pairs(results[2:5])