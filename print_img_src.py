import subprocess
from pathlib import Path

import click
import pyperclip

# Usage: python3 print_img_src.py --country=Taoyuan
from PIL import Image


def get_untracked_files():
    # Get the list of untracked files using git
    result = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard"],
        capture_output=True,
        text=True,
    )
    # Split the output by lines to get each untracked file
    untracked_files = result.stdout.splitlines()
    return set(untracked_files)


@click.command()
@click.option("--country")
def print_img_src(country: str):
    untracked_files = get_untracked_files()
    path = Path(f"assets/media/{country}").resolve()
    if not path.exists():
        print(f"path:{path} is wrong")
    html_ouput = ""
    for filepath in sorted(
        path.glob("*"), key=lambda x: "_".join(str(x).split("_")[2:])
    ):
        name = str(filepath).split("blog/")[1]
        if (
            any(
                ext in filepath.suffix.lower()
                for ext in [".jpg", ".jpeg", ".png", ".tiff", ".heic"]
            )
            and name in untracked_files
        ):
            img = Image.open(name)
            html_line = f'<img src="{name}" width="{img.width}" height="{img.height}" loading="lazy"/>'
            html_ouput += html_line + "\n"
    print(html_ouput)
    pyperclip.copy(html_ouput)


if __name__ == "__main__":
    print_img_src()
