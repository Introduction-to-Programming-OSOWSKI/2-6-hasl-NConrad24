#WRITE YOUR CODE IN THIS FILE
def hasL(w):
    numl=0
    for i in range(0, len(w)):
        if w[i] == "l":
            numl=numl+1
    if numl >=1:
        return True
    else:
        return False