import sys
import os
from pathlib import Path
parent_dir = os.path.dirname(os.path.abspath(str(Path(__file__).parent)))
sys.path.insert(0, str(parent_dir))
print("{0} parent_dir: {1}".format(__file__, parent_dir))
