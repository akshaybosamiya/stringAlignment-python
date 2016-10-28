#N, M = map(int,input().split()) # N must be odd and M must be equal to N*3
N=21
M=63
for i in range(1,N,2): 
    print((".$."*i).center(M,' ')) #Enter Code Here
print(" H A P P Y ~ D H A N T E R A S ".center(M,':'))