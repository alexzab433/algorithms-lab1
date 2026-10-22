import csv
import os
import time
from alg import two_pointers,binary,exp,double_binary
ALGOS={"two_pointers":two_pointers,"binary":binary,"exp":exp,"double_binary":double_binary}
def make_worst(m,n):
    a=[2*(i*n//m)+1 for i in range(m)]
    b=[2*i for i in range(n)]
    return a,b
def measure(f,a,b,repeats):
    best=float("inf")
    for _ in range(repeats):
        t=time.perf_counter()
        r=f(a,b)
        best=min(best,time.perf_counter()-t)
        assert r==False
    return best
def run(name,pairs,writer):
    for m,n in pairs:
        a,b=make_worst(m,n)
        repeats=5 if n<=10000 else 3
        for algo,f in ALGOS.items():
            writer.writerow([name,algo,m,n,measure(f,a,b,repeats)])
        print(name,"M =",m,"N =",n,flush=True)
equal=[(2**k,2**k) for k in range(7,19)]
fixed_m=[(50,2**k) for k in range(6,21)]
ratio=[(2**17//2**k,2**17) for k in range(0,13)]
if __name__=="__main__":
    os.makedirs("data",exist_ok=True)
    with open("data/results.csv","w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["experiment","algorithm","M","N","time_sec"])
        run("equal",equal,writer)
        run("fixed_m",fixed_m,writer)
        run("ratio",ratio,writer)
