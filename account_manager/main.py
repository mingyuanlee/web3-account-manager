import click
import yaml

from account_manager.eth_account import get_ith_account

@click.group()
def cli():
  with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

  global keyword
  keyword = config['keyword']
  """Account Manager CLI"""
  pass

@click.command()
@click.argument('index', type=int)
def get(index):
  """Get the i-th account based on keyword"""
  account = get_ith_account(keyword, index)
  click.echo(f"Account {str(index)}")
  click.echo(f"Private Key: {account.private_key}")
  click.echo(f"Public Key: {account.public_key}")
  click.echo(f"ETH Address: {account.eth_address}")

# Adding the get command to the cli group
cli.add_command(get)

if __name__ == '__main__':
  cli()