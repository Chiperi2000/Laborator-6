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
    
isItATriangle(0 , 1, 0)