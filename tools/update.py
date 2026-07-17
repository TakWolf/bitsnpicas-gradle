import shutil
from zipfile import ZipFile

from loguru import logger

from tools import project_root_dir, downloads_dir
from tools.utils import download_util


def _update_java_src():
    sha = '6d1e7d96f0ad3f253d961e52922a2b15b95f853d'

    source_file_path = downloads_dir.joinpath(f'bitsnpicas-{sha}.zip')
    if not source_file_path.exists():
        asset_url = f'https://github.com/kreativekorp/bitsnpicas/archive/{sha}.zip'
        logger.info("Start download: '{}'", asset_url)
        downloads_dir.mkdir(parents=True, exist_ok=True)
        download_util.download_file(asset_url, source_file_path)
    else:
        logger.info("Already downloaded: '{}'", source_file_path)

    source_unzip_dir = downloads_dir.joinpath(f'bitsnpicas-{sha}')
    if source_unzip_dir.exists():
        shutil.rmtree(source_unzip_dir)
    with ZipFile(source_file_path) as file:
        file.extractall(downloads_dir)
    logger.info("Unzip: '{}'", source_unzip_dir)

    src_root_dir = project_root_dir.joinpath('bitsnpicas', 'src', 'main', 'java')
    if src_root_dir.exists():
        shutil.rmtree(src_root_dir)
    source_unzip_dir.joinpath('main', 'java', 'BitsNPicas', 'src').rename(src_root_dir)

    if source_unzip_dir.exists():
        shutil.rmtree(source_unzip_dir)
    logger.info("Update src: '{}'", src_root_dir)


def main():
    _update_java_src()


if __name__ == '__main__':
    main()
