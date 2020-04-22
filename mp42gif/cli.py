"""Console script for mp42gif."""
import sys
import click


@click.command()
@click.option
def main(args=None):
    """Console script for mp42gif."""
    click.echo("Replace this message by putting your code into "
               "mp42gif.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
