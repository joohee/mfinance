import sys
import os
from pathlib import Path
parent_dir = Path(__file__).parent
print(parent_dir)
sys.path.insert(0, str(parent_dir)+'/packages')
