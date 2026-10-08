import os
import shutil

vibe_root = r"C:\Users\KARSHAK_Tamal\Desktop\Git\AVL-RJ\vibelattice"
vibe_frontend = os.path.join(vibe_root, "vibe_frontend")

if os.path.exists(vibe_frontend):
    for item in os.listdir(vibe_frontend):
        src = os.path.join(vibe_frontend, item)
        dst = os.path.join(vibe_root, item)
        if os.path.exists(dst):
            if os.path.isdir(dst):
                shutil.rmtree(dst)
            else:
                os.remove(dst)
        shutil.move(src, dst)
    
    # Remove the empty vibe_frontend folder
    os.rmdir(vibe_frontend)
    print("Successfully moved frontend files to the root of vibelattice.")
else:
    print("vibe_frontend folder already removed or doesn't exist.")

# Ensure we bring over the missing .avl and .mass files from scratch
src_runs = r"C:\Users\KARSHAK_Tamal\.gemini\antigravity-ide\scratch\vibelattice\third_party\avl\runs"
dest_runs = os.path.join(vibe_root, "third_party", "avl", "runs")

if os.path.exists(src_runs) and os.path.exists(dest_runs):
    import glob
    for ext in ["*.avl", "*.mass"]:
        for file_path in glob.glob(os.path.join(src_runs, ext)):
            filename = os.path.basename(file_path)
            dest_path = os.path.join(dest_runs, filename)
            shutil.copy2(file_path, dest_path)
    print("Successfully restored example files to third_party/avl/runs.")
