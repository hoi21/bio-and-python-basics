import sys
import random
sys.path.insert(0, "src")

from Bio.Align import PairwiseAligner
from align import needleman_wunsch


def biopython_score(a, b):
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 1
    aligner.mismatch_score = -1
    aligner.open_gap_score = -1
    aligner.extend_gap_score = -1
    return aligner.score(a, b)


def test_known_example():
    # TODO: assert your score equals biopython_score for one pair
    score = needleman_wunsch("GCATGCG", "GATTACA")[0]
    assert score == biopython_score("GCATGCG", "GATTACA")

def test_random_sequences():
    # TODO: loop over random DNA pairs and compare scores
    random.seed(0)
    for _ in range(50):
        a = "".join(random.choices("ACGT", k=random.randint(5, 40)))
        b = "".join(random.choices("ACGT", k=random.randint(5, 40)))
        assert needleman_wunsch(a, b)[0] == biopython_score(a, b), (a, b)

def test_hand_checked():
    assert needleman_wunsch("A", "A")[0] == 1
    assert needleman_wunsch("A", "T")[0] == -1
    assert needleman_wunsch("GA", "GA")[0] == 2
    assert needleman_wunsch("A", "")[0] == -1