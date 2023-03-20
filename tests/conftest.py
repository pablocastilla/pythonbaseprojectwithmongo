from pathlib import Path
import os
import sys

main_folder = Path(__file__).parent.parent
sys.path.insert(0, str(main_folder))
sys.path.insert(0, str(main_folder / "src"))
sys.path.insert(0, str(main_folder / "tests"))
os.chdir(main_folder / "src")
