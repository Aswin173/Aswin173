import math
def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom


x=int(input("Enter a number"))
mean=int(input("Enter mean"))
sd=int(input("Enter sd"))
normpdf(x,mean,sd)

