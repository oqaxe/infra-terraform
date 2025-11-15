import os
import sys
import click
import logging

from infra_terraform.terraform import Terraform

@click.group()
def main():
    """Terraform infrastructure deployment tool."""
    pass

@main.command()
@click.option('--init', is_flag=True, help='Initialize terraform configuration.')
@click.option('--apply', is_flag=True, help='Apply terraform configuration.')
@click.option('--destroy', is_flag=True, help='Destroy terraform configuration.')
@click.argument('directory', type=click.Path(exists=True))
def terraform(init, apply, destroy, directory):
    """Terraform command wrapper."""
    terraform = Terraform(directory)

    if init:
        terraform.init()
    elif apply:
        terraform.apply()
    elif destroy:
        terraform.destroy()
    else:
        click.echo("No command specified. Use --help for usage.")

if __name__ == '__main__':
    main()