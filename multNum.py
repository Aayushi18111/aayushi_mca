def inc(n):
    '''
    objective: increase the input number by one
    '''
    return n+1

def pred(a,base=0):
    '''
    approach: find predecessor using recursion
    '''
    if inc(base) == a:
        return base
    else:
        return pred(a,inc(base))

def multNum(a, b):
    '''
    objective: to multiply two user input numbers
    '''
    #approach: recursively use function of predecessor to muliply recursively
    if a == 0:
       return 0
    elif a == 1:
       return b
    else:
       return b + multNum(pred(a,base=0), b)

def main():
    '''
    objective: to multiply two user input numbers
    '''
    #approach: recursively use multNum function

    a=int(input('Enter first number: '))
    b=int(input('Enter second number: '))
    print('Multiple of',a, 'and',b, '=', multNum(a,b))
      

if __name__=='__main__':
    main()
