from solution import SolParse
import os

solutionlist = []

for sol in os.listdir("./solutions"):
    if os.path.exists(f"./solutions/{sol}/solution") and sol != "example":
        psol = SolParse(f"./solutions/{sol}/solution")

        solutionlist.append(psol)

for _, sol in enumerate(solutionlist):

    print('[',_,']',sol.getFormatted())

res = input("Num for issue, or e to exit:\n")

try: 
    int(res)
except:
    quit()

solutionlist[int(res)].exec()
