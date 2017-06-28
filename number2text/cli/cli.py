"""Define the top-level cli command."""
import click
from pbr import version

from number2text import conversion

# Retrieve the project version from PBR.
try:
    version_info = version.VersionInfo('processor-cli')
    __version__ = version_info.release_string()
except AttributeError:
    __version__ = None


@click.group()
@click.version_option(version=__version__)
@click.option(
    '--log-level',
    '-l',
    default='NOTSET',
    type=click.Choice(['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']),
    help='defines the log level',
    show_default=True)
@click.pass_context
def cli(ctx, log_level):
    """Manage CLI commands."""
    ctx.obj = {**ctx.params}


@click.command()
@click.argument('number', type=click.INT)
def convert(number):
    click.echo(conversion.convert(number))


cli.add_command(convert)
