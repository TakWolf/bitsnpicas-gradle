import shutil
from zipfile import ZipFile

from loguru import logger

from tools import project_root_dir, downloads_dir
from tools.utils import download_util


def _update_javas():
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

    for module_name in ('bitsnpicas', 'keyedit', 'mapedit', 'unicode'):
        src_root_dir = project_root_dir.joinpath(module_name, 'src', 'main', 'java', 'com', 'kreative', module_name)
        if src_root_dir.exists():
            shutil.rmtree(src_root_dir)
        src_root_dir.parent.mkdir(parents=True, exist_ok=True)
        source_unzip_dir.joinpath('main', 'java', 'BitsNPicas', 'src', 'com', 'kreative', module_name).rename(src_root_dir)
        logger.info("Update src: '{}'", src_root_dir)

    if source_unzip_dir.exists():
        shutil.rmtree(source_unzip_dir)


def _format_javas():
    for module_name in ('bitsnpicas', 'keyedit', 'mapedit', 'unicode'):
        src_root_dir = project_root_dir.joinpath(module_name, 'src', 'main', 'java', 'com', 'kreative', module_name)
        for file_dir, _, file_names in src_root_dir.walk():
            for file_name in file_names:
                if not file_name.endswith('.java'):
                    continue
                file_path = file_dir.joinpath(file_name)

                lines = []
                for line in file_path.read_text('utf-8').splitlines():
                    line = line.replace('\t', '    ').rstrip()
                    lines.append(line)
                lines.append('')
                text = '\n'.join(lines)

                file_path.write_text(text, 'utf-8')
                logger.info("Format: '{}'", file_path)


def _fix_resources():
    for module_name in ('bitsnpicas', 'keyedit', 'mapedit', 'unicode'):
        resources_root_dir = project_root_dir.joinpath(module_name, 'src', 'main', 'resources')
        if resources_root_dir.exists():
            shutil.rmtree(resources_root_dir)

        src_root_dir = project_root_dir.joinpath(module_name, 'src', 'main', 'java', 'com', 'kreative', module_name)
        for file_dir, _, file_names in src_root_dir.walk():
            for file_name in file_names:
                if file_name.endswith('.java'):
                    continue
                file_from_path = file_dir.joinpath(file_name)
                file_to_path = resources_root_dir.joinpath(file_from_path.relative_to(src_root_dir))
                file_to_path.parent.mkdir(parents=True, exist_ok=True)
                file_from_path.rename(file_to_path)
                logger.info("Move: '{}' -> '{}'", file_from_path, file_to_path)


def main():
    _update_javas()
    _format_javas()
    _fix_resources()


if __name__ == '__main__':
    main()
