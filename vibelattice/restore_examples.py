import os
import shutil
import glob

# Source from the original complete VibeLattice frontend in your scratch folder
src_dir = r"C:\Users\KARSHAK_Tamal\.gemini\antigravity-ide\scratch\vibelattice\third_party\avl\runs"
# Destination in your Desktop repo
dest_dir = r"C:\Users\KARSHAK_Tamal\Desktop\Git\AVL-RJ\vibelattice\vibe_frontend\third_party\avl\runs"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

restored = 0
for ext in ["*.avl", "*.mass"]:
    for file_path in glob.glob(os.path.join(src_dir, ext)):
        filename = os.path.basename(file_path)
        dest_path = os.path.join(dest_dir, filename)
        shutil.copy2(file_path, dest_path)
        restored += 1

print(f"Successfully restored {restored} missing example files (.avl and .mass) into {dest_dir}")
