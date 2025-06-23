import yaml

root_compose = 'docker-compose.yml'

with open(root_compose, 'r') as fp:
  config: dict = yaml.safe_load(fp)

out = ", ".join(config['services'].keys())
print(out)