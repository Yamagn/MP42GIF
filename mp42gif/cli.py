"""Console script for mp42gif."""
import sys
import click
import mp42gif.mp42gif as mp42gif


@click.command()
@click.argument('video_path')
@click.argument('dir_path')
@click.argument('basename')
@click.option('--ext', '-e', default='jpg')
@click.option('--quality', '-q', default="high")
@click.option('--crop', '-c', default='none')
def main(video_path, dir_path, basename, quality, ext, crop):
    mp42gif.mp4togif(str(video_path), str(dir_path), str(basename), str(quality), str(crop), str(ext))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
