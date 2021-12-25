import shutil
import json
from pathlib import Path
from src.data import DATA_DIR
from src.utils.io import read_json
from loguru import logger

class OrgnizeFiles:
    """
    This class is used to orgnize files in directory by
    moving files into directories based on extension
    """
    def __init__(self, directory):
        self.directory = Path(directory)
        if not self.directory.exists():
            raise FileNotFoundError(f'{self.dirctory} does not exist')
        ext_dirs = read_json(DATA_DIR / 'extensions.json')
        self.extension_dest = {}
        for dir_name, ext_list in ext_dirs.items():
            for ext in ext_list:
                self.extensions_dest[ext] = dir_name
        print(self.extensions_des)


    def __call__(self):
        """Organizing files in directory by moving them
        to sub directories based on extension.
        """
        logger.info(f"Orgnizing files in {self.directory}...")
        file_extensions = []
        for file_path in self.directory.iterdir():

            # ignore direction
            if file_path.is_dir():
                continue

            # ignore hidden files
            if file_path.name.startswith('.'):
                continue

            # move files
            if file_path.suffix not in self.extensions_dest:
                DEST_DIR = self.directory / 'Other'
            else:
                DEST_DIR = self.directory / self.extendions_dest[file_path.suffix]
            DEST_DIR.mkdir(exist_ok = True)
            logger.info(f'moving{file_path} to {DEST_DIR}...')
            shutil.move(str(file_path), str(DEST_DIR))


if __name__ == '__main__':
    org_files = OrgnizeFiles('mnt/c/Users/Elham/Downloads')
    org_files = ()
    logger.info('Done!')

