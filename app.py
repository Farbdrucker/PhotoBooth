import os

from flask import Flask, render_template

from typer import Typer
from rich import print as rprint

print = rprint

cli_app = Typer()
app = Flask("PhotoBooth")
image_directory = 'static/images/'  # Replace with the actual directory path


def get_newest_image():
    # Get the list of files in the directory
    files = os.listdir(image_directory)

    # Filter out non-image files
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.PNG', '.jpeg', '.gif'))]
    print(f"total number of files: [red]{len(files)}[/red]")

    # Sort the image files by modification time
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(image_directory, x)))


    if image_files:
        newest_image = image_files[-1]
        
        print(f"newest image: {newest_image}")
        return {"image": newest_image, "counts": len(image_files)}
    else:
        return None


@app.route('/')
def index():
    result = get_newest_image()
    return render_template('index.html', image=result['image'])


@app.route('/image')
def image():
    return get_newest_image()


@cli_app.command()
def create_website(host: str = '0.0.0.0', port: int =5000 ):
    app.run(host=host, port=port)

if __name__ == '__main__':
    cli_app()


