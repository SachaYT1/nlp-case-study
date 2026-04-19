import pytest
from src.parsers import SpacyParser, StanzaParser, ParseResult

TOKENS_EN = ["The", "cat", "sat", "on", "the", "mat", "."]


@pytest.mark.slow
def test_spacy_parses_english_pretokenized() -> None:
    p = SpacyParser("en_core_web_trf")
    result = p.parse([TOKENS_EN])
    assert isinstance(result[0], ParseResult)
    assert len(result[0].heads) == len(TOKENS_EN)
    assert len(result[0].deprels) == len(TOKENS_EN)
    assert 0 in result[0].heads  # root must exist


@pytest.mark.slow
def test_stanza_parses_english_pretokenized() -> None:
    p = StanzaParser("en")
    result = p.parse([TOKENS_EN])
    assert len(result[0].heads) == len(TOKENS_EN)
    assert 0 in result[0].heads
