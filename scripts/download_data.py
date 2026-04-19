"""Download UD-EWT (English) and UD-SynTagRus (Russian) test splits."""
from __future__ import annotations

import urllib.error
import urllib.request
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

FILES = {
    "en_ewt_test.conllu": (
        "https://raw.githubusercontent.com/UniversalDependencies/"
        "UD_English-EWT/r2.13/en_ewt-ud-test.conllu"
    ),
    "ru_syntagrus_test.conllu": (
        "https://raw.githubusercontent.com/UniversalDependencies/"
        "UD_Russian-SynTagRus/r2.13/ru_syntagrus-ud-test.conllu"
    ),
}


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for fname, url in FILES.items():
        dest = DATA_DIR / fname
        if dest.exists():
            print(f"skip {fname} (exists)")
            continue
        print(f"downloading {fname} ...")
        tmp = dest.with_suffix(".tmp")
        try:
            urllib.request.urlretrieve(url, tmp)
        except urllib.error.HTTPError as e:
            tmp.unlink(missing_ok=True)
            raise RuntimeError(f"HTTP {e.code} downloading {url}") from e
        except Exception:
            tmp.unlink(missing_ok=True)
            raise
        tmp.rename(dest)
        print(f"saved {dest}")


if __name__ == "__main__":
    main()
