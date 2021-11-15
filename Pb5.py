def l100kmtompg(liters):
    litrii_100km = (3.78541178 / 1.609344) * 100
    mpg = litrii_100km/liters
    return mpg



def mpgtol100km(miles):
    litrii_100km = (3.78541178 / 1.609344) * 100
    mpg = litrii_100km/miles
    return mpg


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))