
from genetics import Genetics

target = "to be or not to be that is the question"
alphabet = "abcdefghijklmnopqrstuvwxyz "

def calcFitness(genalg):
    genalg.fitnesses = []
    for c in genalg.population:
        s = ""
        f = 0
        for g in c:
            s += alphabet[g]
        for i in range(len(target)):
            if s[i] == target[i]:
                f += 1
        genalg.fitnesses.append(f * f)


if __name__ == "__main__":

    genalg = Genetics(1000, len(target), 0, 26)
    while True:
        calcFitness(genalg)
        f, c = max(zip(genalg.fitnesses, genalg.population))
        print("{:02d}".format(f), end=" ")
        for g in c:
            print(alphabet[g], end="")
        if f == len(target) * len(target):
            print()
            break
        else:
            print(end="\r", flush=True)
        genalg.repopulate()
    print(genalg.generation, "generations")
        
