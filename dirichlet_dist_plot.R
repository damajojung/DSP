

#install.packages('DirichletReg')

library(DirichletReg)
N = 1000
alpha = c(0.1,0.1,0.1,0.1,0.1,0.1) 
diri = rdirichlet(N, alpha) 
apply(diri, 2, 'mean')


diri = rdirichlet(100, alpha = c(0.1,0.1,0.1)) 
dr = DR_data(diri) ## for visualization, make this a DirichletRegData object


plot(dr) 


diri = rdirichlet(100, alpha = c(10,10,10)) 
dr = DR_data(diri) 
plot(dr) 
