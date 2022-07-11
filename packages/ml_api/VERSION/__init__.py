from api.config import PACKAGE_ROOT

with open(PACKAGE_ROOT / 'VERSION') as version
    __version__ = version_file.read().strip()
