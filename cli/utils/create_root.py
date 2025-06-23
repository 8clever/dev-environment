import yaml

file = 'docker-compose.yml'

root = {
  "version": "3.9",
  "services": {}
}

try:
  with open(file) as fp:
    config = yaml.safe_load(fp)
except:
  with open(file, 'w') as fp:
    yaml.safe_dump(root, fp)