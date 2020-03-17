def FindingCommonResist():
    
    b = input("0 for parallel, 1 for continious: ")
    if (b == "1"):
       print(continious())
    elif(b == "0"):
        print(Parallel())
    else:
        print ("select 0 or 1")
        FindingCommonResist()
    
def continious():
    sum = 0
    b = []
    s = int(input("# of resistors: ")) 
    b = [int(s) for s in input().split()]
    
    for i in range(len(b)):
        sum+=b[i]

    return(sum)

def Parallel():
    sum = 0
  
    s = input("# of resistors: ") 
    b = [int(s) for s in input().split()]
    
    for i in range(len(b)):
        sum += 1/b[i]
        r = 1/sum
    
    return(r)
            

FindingCommonResist()
