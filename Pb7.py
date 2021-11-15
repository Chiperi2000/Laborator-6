def isItATriangle(latura1 , latura2, latura3):
    if latura1 > 0 and latura2 > 0 and latura3 > 0:
        if latura1 + latura2 >= latura3:
            print("Poate fi triunghi!")
        elif latura1 + latura3 >= latura2:
            print("Poate fi triunghi!")
        elif latura2 + latura3 >= latura1:
            print("Poate fi triunghi!")
        else:
            print("Nu poate fi triunghi")
    else:
        print("Nu poate fi triunghi")
    
def dreptunghic(latura1 , latura2, latura3):
    if latura1 > latura2:
        ipotenuza = latura1
        c1 = latura2
        c2 = latura3
        ipotenuza_c = ipotenuza ** 2 == c1 ** 2 + c2 ** 2
        if ipotenuza == True:
            print("Triunghi dreptunghic")
        else:
            print("Nu este triunghi dreptunghic")
    if latura2 > latura3:
        ipotenuza = latura2
        c1 = latura1
        c2 = latura3
        ipotenuza_c = ipotenuza ** 2 == c1 ** 2 + c2 ** 2
        if ipotenuza_c == True:
            print("Triunghi dreptunghic")
        else:
            print("Nu este triunghi dreptunghic")
    if latura3 > latura1:
        ipotenuza = latura3
        c1 = latura1
        c2 = latura2
        ipotenuza_c = ipotenuza ** 2 == c1 ** 2 + c2 ** 2
        if ipotenuza_c == True:
            print("Triunghi dreptunghic")
        else:
            print("Nu este triunghi dreptunghic")
    if latura1 == latura2 == latura3:
        print("Triunghi dreptunghic isoscel")


isItATriangle(1 ,1 , 1)
dreptunghic(1 ,1 , 1)