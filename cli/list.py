import yaml

root_compose = 'docker-compose.yml'

with open(root_compose, 'r') as fp:
  config: dict = yaml.safe_load(fp)

print('Docker compose services list:')
for service in config['services'].keys():
  print(f" - {service}")