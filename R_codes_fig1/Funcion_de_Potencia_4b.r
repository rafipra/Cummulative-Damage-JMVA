#Función de Potencia 4
n<-10
sigma<-.5 
delta<-seq(0,4,0.01)
pdelta<-1-pchisq(9.487729,4,ncp=sigma*(delta-2)^2*n)
pdelta2<-1-pchisq(9.487729,4,ncp=2*n*sigma*(delta-2)^2)
plot(delta,pdelta,ylim=c(0,1),type="l",lty=1,col=1,
main="Fourth profile of the power function",xlab="theta 1",ylab="power of the test")
lines(delta,pdelta2,col=1,lty=8)
legend(.0, .2, c("n=10", "n=20"), 
col = c(1, 1), lty = c(1,8))