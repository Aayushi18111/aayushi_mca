def inc(n):
    '''
    objective: increase the input number by one
    '''
    return n+1

def sumInc(n, m):
    '''
    approach: use recursion to add the numbers
    '''

    if m == 0:
        return n
    else:
        return sumInc(inc(n),m-1) 

