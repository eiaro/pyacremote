"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mpyacremote` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``pyacremote.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``pyacremote.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import sys
import click
from discover import Discover

@click.group(invoke_without_command=True)
@click.version_option()
@click.pass_context
def cli(ctx):
  pass

@cli.command()
@click.option('--ttl', default=100, help="Time to wait for results", type=int)
def discover(ttl):
  """Discover ACRemote devices on the current network"""
  d = Discover()
  found_devices = d.run(ttl)

  for dev in found_devices:
    click.echo("Found ACRemote at %s" % dev._address)

@cli.command()
@click.argument('host', nargs=1)
@click.option('--json', default=True, help="Return the result as JSON", type=bool)
@click.pass_context
def get(ctx, host, json):
  """Get ACState from an ACRemote device"""
  
  return

@cli.command()
def set():
  """Apply the state to an ACRemote device"""
  return
  

if __name__ == "__main__":
  cli()
