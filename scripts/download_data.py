"""Download UD-EWT (English) and UD-SynTagRus (Russian) test splits."""
from pathlib import Path
import urllib.request

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
    DATA_DIR.mkdir(exist_ok=True)
    for fname, url in FILES.items():
        dest = DATA_DIR / fname
        if dest.exists():
            print(f"skip {fname} (exists)")
            continue
        print(f"downloading {fname} ...")
        urllib.request.urlretrieve(url, dest)
        print(f"saved {dest}")


if __name__ == "__main__":
    main()
