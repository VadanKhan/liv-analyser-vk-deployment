# config.py
import os
import sys
from pathlib import Path

# ------------------------------------------------------------------------------------------------ #
#                                        PATH CONFIGURATIONS                                       #
# ------------------------------------------------------------------------------------------------ #

CURRENT_DIR = Path(os.getcwd())
ROOT_DIR = CURRENT_DIR  # Adjust this if needed
sys.path.append(str(ROOT_DIR))

SUBARU_DECODER = "QC WAFER_LAYOUT 24Dec.csv"
HALO_DECODER = "HALO_DECODER_NE-rev1_1 logic_coords_annotated.csv"

MONITORED_PATH = Path("D:/result/")

GTX_RESULTS_PATH = ROOT_DIR / "results_gtx"
LEVEE_RESULTS_PATH = ROOT_DIR / "results_dats"

INI_NAME = "PROBEINF.ini"
INI_LOCATION = Path("N:/XFER/") / INI_NAME

LEVEE_FOLDER = ROOT_DIR / "levee_folder"
LEVEE_EXE_PATH = ROOT_DIR / "levee_folder/LIVDisp.exe"

LOG_NAME = "detection_log.txt"
LOG_PATH = ROOT_DIR / LOG_NAME

VERSION = 1.1
