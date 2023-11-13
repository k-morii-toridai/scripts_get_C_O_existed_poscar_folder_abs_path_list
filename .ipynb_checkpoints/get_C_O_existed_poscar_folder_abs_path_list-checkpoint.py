import os
from pathlib import Path
import numpy as np


# load
C_O_existed_poscar_abs_path_list_loaded = np.load("C_O_existed_poscar_abs_path_list.npy", allow_pickle=True)
print(f"len(C_O_existed_poscar_abs_path_list_loaded): {len(C_O_existed_poscar_abs_path_list_loaded)}")

# make C_O_existed_poscar_folder_abs_path_list
C_O_existed_poscar_folder_abs_path_list = [Path(os.path.split(POSCAR_path)[0] )for POSCAR_path in C_O_existed_poscar_abs_path_list_loaded]

# save 
np.save("C_O_existed_poscar_folder_abs_path_list.npy", C_O_existed_poscar_folder_abs_path_list)
