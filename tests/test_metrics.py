import pytest
from src.metrics import uas, las, Gold, Prediction


def _g(heads, deprels):
    return Gold(heads=heads, deprels=deprels)


def _p(heads, deprels):
    return Prediction(heads=heads, deprels=deprels)


def test_uas_perfect() -> None:
    assert uas([_p([2, 0], ["nsubj", "root"])], [_g([2, 0], ["nsubj", "root"])]) == 1.0


def test_uas_half() -> None:
    assert uas([_p([2, 1], ["nsubj", "root"])], [_g([2, 0], ["nsubj", "root"])]) == 0.5


def test_las_label_mismatch_counts_wrong() -> None:
    pred = [_p([2, 0], ["obj", "root"])]
    gold = [_g([2, 0], ["nsubj", "root"])]
    assert uas(pred, gold) == 1.0
    assert las(pred, gold) == 0.5


def test_excludes_punct_by_default() -> None:
    gold = [Gold(heads=[2, 0, 2], deprels=["nsubj", "root", "punct"])]
    pred = [Prediction(heads=[2, 0, 1], deprels=["nsubj", "root", "punct"])]
    assert uas(pred, gold, exclude_punct=False) == pytest.approx(2 / 3)
    assert uas(pred, gold, exclude_punct=True) == 1.0
