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

def mult(a, b):
   if a == 0:
      return 0
   elif a == 1:
      return b
   else:
      return b + mult((pred(a,inc(base)), b)

def main():
    '''
    '''
    a=int(input('Enter first number: ')
    b=int(input('Enter first number: ')	
    print('Multiple of',a, 'and',b, '=', mult(a,b))
      

if __name__=='__main__':
    main()
