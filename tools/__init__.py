from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).parents[1]

CACHE_DIR = PROJECT_ROOT_DIR.joinpath('cache')
DOWNLOADS_DIR = CACHE_DIR.joinpath('downloads')
