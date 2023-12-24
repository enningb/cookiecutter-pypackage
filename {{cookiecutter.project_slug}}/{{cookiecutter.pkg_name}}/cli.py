"""Console script for {{cookiecutter.pkg_name}}."""

{% if cookiecutter.command_line_interface|lower == 'click' -%}
import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("{{ cookiecutter.project_slug }}")
    click.echo("=" * len("{{ cookiecutter.project_slug }}"))
    click.echo("{{ cookiecutter.project_short_description }}")


if __name__ == "__main__":
    main()  # pragma: no cover

{% elif cookiecutter.command_line_interface|lower == 'typer' -%}
import typer
from {{ cookiecutter.pkg_name }} import CONFIG_FILE

app = typer.Typer(
    name="{{ cookiecutter.pkg_name }}",
    help="{{ cookiecutter.project_short_description }}",
)

@app.callback()
def callback():
    """
    {{ cookiecutter.project_short_description }}
    """

# create commandline tool with code like below:
@app.command()
def example_command():
    typer.echo(
        f"This will print the config file path: {CONFIG_FILE} "
    )


{%- endif %}