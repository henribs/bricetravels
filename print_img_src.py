from pathlib import Path

import click


@click.command()
@click.option("--country")
def print_img_src(country: str):
    path = Path(f"assets/media/{country}").resolve()
    if not path.exists():
        print(f"path:{path} is wrong")
    for file in sorted(path.glob("*"), key=lambda x: "_".join(str(x).split("_")[2:])):
        name = str(file).split("blog/")[1]
        print(f'<img src="{name}" />')


if __name__ == "__main__":
    print_img_src()
