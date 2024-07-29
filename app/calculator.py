import click

from app.model import Calculator


@click.group()
@click.pass_context
def calc(ctx: click.Context):
    """A single calculator"""
    ctx.obj = {"calculator_object": Calculator()}