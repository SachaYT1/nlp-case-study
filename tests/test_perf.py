import time
from src.perf import measure_throughput, measure_peak_memory


def test_measure_throughput_reports_tokens_per_sec() -> None:
    def fn(batch):
        time.sleep(0.001 * len(batch))
        return batch

    batches = [[["a", "b", "c"]]] * 10  # 10 batches, each with 1 sentence of 3 tokens
    m = measure_throughput(fn, batches, warmup=2)
    assert m.sentences_per_sec > 0
    assert m.tokens_per_sec > 0
    assert m.n_sentences == 8
    assert m.n_tokens == 24


def test_measure_peak_memory_captures_allocation() -> None:
    def fn():
        return [0] * 100_000

    peak = measure_peak_memory(fn)
    assert peak > 0
