import os

import click


@click.command
@click.argument("input_file", type=click.File())
@click.option(
    "--out-path", type=click.Path(exists=True, file_okay=False, writable=True), help=""
)
def main():
    pass
