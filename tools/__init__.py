from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).parent.joinpath('..').resolve()

CACHE_DIR = PROJECT_ROOT_DIR.joinpath('cache')
DOWNLOADS_DIR = CACHE_DIR.joinpath('downloads')
