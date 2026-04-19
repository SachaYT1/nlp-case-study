from pathlib import Path
from src.data import load_sentences, Sentence, bucket_by_length

FIXTURE = """# sent_id = 1
# text = The cat sat.
1	The	the	DET	DT	_	2	det	_	_
2	cat	cat	NOUN	NN	_	3	nsubj	_	_
3	sat	sit	VERB	VBD	_	0	root	_	_
4	.	.	PUNCT	.	_	3	punct	_	_

"""

def test_load_sentences_parses_basic(tmp_path: Path) -> None:
    p = tmp_path / "t.conllu"
    p.write_text(FIXTURE)
    sents = load_sentences(p)
    assert len(sents) == 1
    s = sents[0]
    assert isinstance(s, Sentence)
    assert s.tokens == ["The", "cat", "sat", "."]
    assert s.heads == [2, 3, 0, 3]
    assert s.deprels == ["det", "nsubj", "root", "punct"]

def test_load_sentences_skips_multiword(tmp_path: Path) -> None:
    fixture = """# sent_id = 1
1-2	don't	_	_	_	_	_	_	_	_
1	do	do	AUX	_	_	2	aux	_	_
2	n't	not	PART	_	_	0	root	_	_

"""
    p = tmp_path / "t.conllu"
    p.write_text(fixture)
    sents = load_sentences(p)
    assert sents[0].tokens == ["do", "n't"]
    assert sents[0].heads == [2, 0]

def test_bucket_by_length() -> None:
    sents = [
        Sentence("1", ["a"]*5, [], [], []),
        Sentence("2", ["a"]*15, [], [], []),
        Sentence("3", ["a"]*30, [], [], []),
        Sentence("4", ["a"]*50, [], [], []),
    ]
    buckets = bucket_by_length(sents)
    assert [len(buckets[k]) for k in ("1-10", "11-20", "21-40", "40+")] == [1, 1, 1, 1]
