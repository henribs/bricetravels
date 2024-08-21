from pathlib import Path

import click

# Usage: python3 print_img_src.py --country=Taoyuan
from PIL import Image


@click.command()
@click.option("--country")
def print_img_src(country: str):
    path = Path(f"assets/media/{country}").resolve()
    if not path.exists():
        print(f"path:{path} is wrong")
    for filepath in sorted(
        path.glob("*"), key=lambda x: "_".join(str(x).split("_")[2:])
    ):
        if any(ext in str(filepath).lower() for ext in ["jpg", "jpeg", "png"]):
            img = Image.open(filepath)
            name = str(filepath).split("blog/")[1]
            print(f'<img src="{name}" width="{img.width}" height="{img.height}" />')


if __name__ == "__main__":
    print_img_src()
