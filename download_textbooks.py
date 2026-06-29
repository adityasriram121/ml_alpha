import urllib.request
import sys
import shutil
from pathlib import Path

BOOKS = {
    "islp_textbook.pdf": "https://drive.google.com/uc?export=download&id=1ajFkHO6zjrdGNqhqW1jKBZdiNGh_8YQ1",
    "mml_textbook.pdf": "https://mml-book.github.io/book/mml-book.pdf",
    "esl_textbook.pdf": "https://drive.google.com/uc?export=download&id=1--Wo5Hcl2y_v3DL-tGgcJHRPdtjiVYjS",
    "sutton_barto_rl.pdf": "http://incompleteideas.net/book/RLbook2020.pdf",
}

dest_dir = Path("C:/Users/adisr/OneDrive/Documents/ml/ml_alpha/01_resources/books")
dest_dir.mkdir(parents=True, exist_ok=True)

# User-Agent headers to prevent 403 Forbidden errors
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, url in BOOKS.items():
    dest_path = dest_dir / filename
    if dest_path.exists():
        print(f"{filename} already exists. Skipping.")
        continue
        
    print(f"Downloading {filename} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f"Successfully saved to {dest_path}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}", file=sys.stderr)

print("Textbook download script completed.")
