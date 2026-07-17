from pathlib import Path

project_root_dir = Path(__file__).parent.joinpath('..').resolve()

cache_dir = project_root_dir.joinpath('cache')
downloads_dir = cache_dir.joinpath('downloads')
