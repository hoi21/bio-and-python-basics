import sys
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
    pass


def test_random_sequences():
    # TODO: loop over random DNA pairs and compare scores
    pass