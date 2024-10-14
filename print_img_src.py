from pathlib import Path

import click
import pyperclip

# Usage: python3 print_img_src.py --country=Taoyuan
from PIL import Image


@click.command()
@click.option("--country")
def print_img_src(country: str):
    path = Path(f"assets/media/{country}").resolve()
    if not path.exists():
        print(f"path:{path} is wrong")
    html_ouput = ""
    for filepath in sorted(
        path.glob("*"), key=lambda x: "_".join(str(x).split("_")[2:])
    ):
        if any(ext in str(filepath).lower() for ext in ["jpg", "jpeg", "png"]):
            img = Image.open(filepath)
            name = str(filepath).split("blog/")[1]
            html_line = f'<img src="{name}" width="{img.width}" height="{img.height}" loading="lazy"/>'
            html_ouput += html_line + "\n"
    print(html_ouput)
    pyperclip.copy(html_ouput)


if __name__ == "__main__":
    print_img_src()
