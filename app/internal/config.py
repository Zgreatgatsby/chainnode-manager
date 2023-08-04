import os
from pathlib import Path

# should be fixed with config located in app.internal
ROOT_DIR = Path(__file__).absolute().parent.parent.parent
STATIC_FILE_DIR = os.environ.get('STATIC_FILE_DIR', 'static')
