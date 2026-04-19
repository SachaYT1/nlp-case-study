"""Speed + memory measurement helpers."""
from __future__ import annotations

import time
import tracemalloc
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class ThroughputResult:
    n_sentences: int
    n_tokens: int
    seconds: float
    sentences_per_sec: float
    tokens_per_sec: float


def measure_throughput(
    fn: Callable[[list[list[str]]], object],
    batches: list[list[list[str]]],
    warmup: int = 5,
) -> ThroughputResult:
    """Run fn on each batch, skipping the first warmup batches for timing."""
    for b in batches[:warmup]:
        fn(b)
    measured = batches[warmup:]
    n_sent = sum(len(b) for b in measured)
    n_tok = sum(len(s) for b in measured for s in b)
    t0 = time.perf_counter()
    for b in measured:
        fn(b)
    elapsed = time.perf_counter() - t0
    return ThroughputResult(
        n_sentences=n_sent,
        n_tokens=n_tok,
        seconds=elapsed,
        sentences_per_sec=n_sent / elapsed if elapsed else 0.0,
        tokens_per_sec=n_tok / elapsed if elapsed else 0.0,
    )


def measure_peak_memory(fn: Callable[[], object]) -> int:
    """Return peak bytes allocated during fn()."""
    tracemalloc.start()
    try:
        fn()
        _, peak = tracemalloc.get_traced_memory()
        return peak
    finally:
        tracemalloc.stop()
