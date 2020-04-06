import os
import csv
from collections import defaultdict

import click


def get_fh(name: str, fields: list, path: str) -> csv.DictWriter:
    of = open(os.path.join(path, f"{name.replace(' ', '_')}.csv"), "a")
    writer = csv.DictWriter(of, fieldnames=fields)
    writer.writeheader()
    return writer


@click.command()
@click.argument("input_file", type=click.File())
@click.argument("column_name")
@click.option(
    "--out-path",
    type=click.Path(exists=True, file_okay=False, writable=True),
    help="Path to write output files",
)
def main(input_file, column_name, out_path):
    if not out_path:
        out_path = os.path.dirname(input_file.name)
    infile_read = csv.DictReader(input_file)
    if column_name not in infile_read.fieldnames:
        click.secho("ERROR: Invalid Column Name", fg="bright_red")
        return
    file_handlers = {}
    stats = defaultdict(int)
    for line in infile_read:
        split_value = line.get(column_name)
        if split_value not in file_handlers:
            file_handlers.update(
                {
                    split_value: get_fh(
                        name=split_value, fields=infile_read.fieldnames, path=out_path
                    )
                }
            )
        file_handlers[split_value].writerow(line)
        stats[split_value] += 1

    click.secho("Split completed", fg="green")
    for k, v in stats.items():
        click.secho(f"{k} file: {v} records", fg="magenta")
    click.secho(f"Total Count = {sum(stats.values())}", bold=True, fg="blue")
