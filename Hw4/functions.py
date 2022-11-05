import os
import pandas as pd
import numpy as np
import evo
import random as rnd

tas = pd.read_csv('tas.csv')
sections = pd.read_csv('sections.csv')

def overallocation(sol):
    pen = 0
    for i in range(len(sol)):
        if sol[i].sum() > tas['max_assigned'][i]:
            pen += sol[i].sum()-tas['max_assigned'][i]
    return pen

def conflicts(sol):
    '''1 point if ta assigned to a lab with conflicts'''
    score = 0
    for i in range(len(sol)):
        lst = [j for j in range(len(sol[i])) if sol[i][j] == 1]
        for time in sections["daytime"].unique():
            df1 = sections[sections["daytime"] == time]
            l = [k for k in range(len(df1.index.values)) if df1.index.values[k] in lst]
            if len(l) >= 2:
                score += 1

    return score


def undersupport(sol):
    pen = 0
    tas_sum = sol.sum(axis=0)
    for i in range(0, len(tas_sum)):
        if tas_sum[i] < sections["min_ta"][i]:
            pen += sections["min_ta"][i] - tas_sum[i]
    return pen

def unwilling(sol):
    '''1 point for sections ta unwilling to support'''
    score = 0
    for i in range(len(sol)):
        score += sum([1 for j in range(len(sol[i])) if sol[i][j] == 1
                      and list(tas[str(j)])[i] == 'U'])
    return score


def unpreferred(sol):
    '''1 point for sections ta unprefered to support'''
    score = 0
    for i in range(len(sol)):
        score += sum([1 for j in range(len(sol[i])) if sol[i][j] == 1
                      and list(tas[str(j)])[i] == 'W'])
    return score

def swapper(solutions):
    """ Agent: Swap two random values """
    L = solutions[0]
    i = rnd.randrange(0, len(L))
    j = rnd.randrange(0, len(L))
    L[i], L[j] = L[j], L[i]
    return L

def main():
    test1 = np.loadtxt("test1.csv",
                     delimiter=",", dtype=int)

    E = evo.Environment()

    # register the fitness criteria (objects)
    E.add_fitness_criteria("overallocation", overallocation)
    E.add_fitness_criteria("conflicts", conflicts)
    E.add_fitness_criteria("undersupport", undersupport)
    E.add_fitness_criteria("unwilling", unwilling)
    E.add_fitness_criteria("unpreferred", unpreferred)

    # register all agents
    E.add_agent("swapper", swapper, 1)

    # seed the population with an intial solution
    L = test1
    E.add_solution(L)

    # run the evolver
    E.evolve(50000, dom=100, sync=10000)

    # print result
    print(E)



if __name__ == '__main__':
    main()