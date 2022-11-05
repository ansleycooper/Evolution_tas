import numpy as np
from evo import Environment
import pandas as pd
import pytest
import functions

tas = pd.read_csv("tas.csv")
sections = pd.read_csv("sections.csv")

@pytest.fixture()
def cases():
    t1 = np.array((pd.read_csv("test1.csv", header=None)))
    t2 = np.array((pd.read_csv("test1.csv", header=None)))
    t3 = np.array((pd.read_csv("test1.csv", header=None)))
    print(t1)
    return t1, t2, t3

def test_overallocation():
    t1 = np.array((pd.read_csv("test1.csv", header=None)))
    t2 = np.array((pd.read_csv("test2.csv", header=None)))
    t3 = np.array((pd.read_csv("test3.csv", header=None)))
    assert functions.overallocation(t1) == 37, "incorrect allocation for test one"
    assert functions.overallocation(t2) == 41, "incorrect allocation for test two"
    assert functions.overallocation(t3) == 23, "incorrect allocation for test three"

def test_conflicts():
    t1 = np.array((pd.read_csv("test1.csv", header=None)))
    t2 = np.array((pd.read_csv("test2.csv", header=None)))
    t3 = np.array((pd.read_csv("test3.csv", header=None)))
    assert functions.conflicts(t1) == 8, "incorrect conflicts for test one"
    assert functions.conflicts(t2) == 5, "incorrect conflicts for test two"
    assert functions.conflicts(t3) == 2, "incorrect conflicts for test three"

def test_undersupport():
    t1 = np.array((pd.read_csv("test1.csv", header=None)))
    t2 = np.array((pd.read_csv("test2.csv", header=None)))
    t3 = np.array((pd.read_csv("test3.csv", header=None)))
    assert functions.undersupport(t1) == 1, "incorrect conflicts for test one"
    assert functions.undersupport(t2) == 0, "incorrect conflicts for test two"
    assert functions.undersupport(t3) == 7, "incorrect conflicts for test three"

def test_unwilling():
    t1 = np.array((pd.read_csv("test1.csv", header=None)))
    t2 = np.array((pd.read_csv("test2.csv", header=None)))
    t3 = np.array((pd.read_csv("test3.csv", header=None)))
    assert functions.unwilling(t1) == 53, "incorrect unwilling for test one"
    assert functions.unwilling(t2) == 58, "incorrect unwilling for test two"
    assert functions.unwilling(t3) == 43, "incorrect unwilling for test three"

def test_unpreferred():
    t1 = np.array((pd.read_csv("test1.csv", header=None)))
    t2 = np.array((pd.read_csv("test2.csv", header=None)))
    t3 = np.array((pd.read_csv("test3.csv", header=None)))
    assert functions.unpreferred(t1) == 15, "incorrect unpreferred for test one"
    assert functions.unpreferred(t2) == 19, "incorrect unpreferred for test two"
    assert functions.unpreferred(t3) == 10, "incorrect unpreferred for test three"

def main():
    pass

if __name__ == main():
    main()