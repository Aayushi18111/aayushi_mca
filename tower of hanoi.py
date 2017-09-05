def hanoi(n,source,spare,target):
    '''
    objective: move n number of disks from pole 1 to pole 3
    input parameters:
      n,source, spare,target
    '''
    #approach: use recursion

    n>0
    if n==1:
        print('move disk from',source,'to',target)
    else:
        hanoi(n-1,source, target,spare)
        print('move disk from',source,'to',target)
        hanoi(n-1,spare,source,target)

def main():
    n = int(input('Enter the number of disks: '))
    source = 1
    spare = 2
    target = 3
    hanoi(n,source,spare,target)

if __name__=='__main__':
    main()

    
