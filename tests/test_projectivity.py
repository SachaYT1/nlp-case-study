from src.projectivity import nonprojective_arc_mask, sentence_is_projective


def test_projective_simple():
    # "the dog runs" — heads 1-indexed: [2, 3, 0]
    heads = [2, 3, 0]
    assert nonprojective_arc_mask(heads) == [False, False, False]
    assert sentence_is_projective(heads)


def test_crossing_arcs_detected():
    # Tokens A B C D with crossing arcs: A<-C and B<-D
    # heads: A(head=3), B(head=4), C(head=0), D(head=3)
    heads = [3, 4, 0, 3]
    mask = nonprojective_arc_mask(heads)
    # Arc at token A (1) spans (1,3); token B (pos 2) lies inside and its head=4 is outside
    # Arc at token B (2) spans (2,4); token C (pos 3) lies inside and its head=0 is outside
    assert mask[0] is True
    assert mask[1] is True
    assert not sentence_is_projective(heads)


def test_empty_and_single():
    assert nonprojective_arc_mask([]) == []
    assert nonprojective_arc_mask([0]) == [False]
    assert sentence_is_projective([0])
