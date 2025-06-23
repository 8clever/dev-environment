import yaml
from cli.utils.input_select import input_select

root_compose = 'docker-compose.yml'

with open(root_compose, 'r') as fp:
  config: dict = yaml.safe_load(fp)

rm_input = input_select('Select app for remove. Warning: this action is undone!', config['services'].keys())
del config['services'][rm_input]

with open(root_compose, 'w') as fp:
  yaml.safe_dump(config, fp)