import random
import pytest
from alg import two_pointers,binary,exp,double_binary
ALGOS=[two_pointers,binary,exp,double_binary]
def reference(a,b):
    return bool(set(a)&set(b))
@pytest.mark.parametrize("f",ALGOS)
@pytest.mark.parametrize("a,b,expected",[
    ([1,2,3],[3,4,5],True),
    ([2,4,6],[3,5,7],False),
    ([],[],False),
    ([],[1],False),
    ([1],[],False),
    ([1],[1],True),
    ([1,5],[5,9],True),
    ([1,5],[1,9],True),
    ([1,1,2],[3,3],False),
])
def test_examples(f,a,b,expected):
    assert f(a,b)==expected
@pytest.mark.parametrize("f",ALGOS)
def test_random(f):
    rng=random.Random(42)
    for _ in range(5000):
        a=sorted(rng.randint(0,60) for _ in range(rng.randint(0,30)))
        b=sorted(rng.randint(0,60) for _ in range(rng.randint(0,30)))
        assert f(a,b)==reference(a,b),(a,b)
