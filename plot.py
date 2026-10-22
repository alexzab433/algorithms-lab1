import csv
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
def load():
    with open("data/results.csv") as file:
        return list(csv.DictReader(file))
def draw(rows,experiment,xfunc,xlabel,title,filename):
    plt.figure(figsize=(8,5))
    for algo in ["two_pointers","binary","exp","double_binary"]:
        pts=sorted((xfunc(r),float(r["time_sec"])) for r in rows if r["experiment"]==experiment and r["algorithm"]==algo)
        plt.plot([p[0] for p in pts],[p[1] for p in pts],marker="o",label=algo)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(xlabel)
    plt.ylabel("время, с")
    plt.title(title)
    plt.grid(True,which="both",alpha=0.3)
    plt.legend()
    plt.savefig("plots/"+filename,dpi=150,bbox_inches="tight")
    plt.close()
if __name__=="__main__":
    os.makedirs("plots",exist_ok=True)
    rows=load()
    draw(rows,"equal",lambda r:int(r["N"]),"N (M = N)","Массивы одинакового размера","equal_sizes.png")
    draw(rows,"fixed_m",lambda r:int(r["N"]),"N (M = 50)","Фиксированный M = 50, растёт N","fixed_m.png")
    draw(rows,"ratio",lambda r:int(r["N"])/int(r["M"]),"N / M (N = 131072)","Зависимость от соотношения N / M","varying_ratio.png")
