import yaml
import os
import cli.utils.create_root
from cli.utils.input_select import input_select

def add_app (image: str):
  app = {
    image: {
      "build": {
        "context": ".",
        "dockerfile": f'./dockerfiles/{image}/Dockerfile'
      }
    }
  }
  return app

def add_fs_app (folder_name: str, image: str):
  app = {
    folder_name: {
      "build": {
        "context": ".",
        "dockerfile": f'./dockerfiles/{image}/Dockerfile'
      },
      "volumes": [
        f"../{folder_name}:/app",
        "//var/run/docker.sock:/var/run/docker.sock"
      ],
      "entrypoint": [
        "sleep",
        "infinity"
      ]
    }
  }
  return app

def add_container_app (app_name: str, github_url: str, image: str):
  app = {
    app_name: {
      "build": {
        "args": [
          f"GITHUB_URL={github_url}"
        ],
        "context": ".",
        "dockerfile": f'./dockerfiles/{image}/Dockerfile'
      },
      "volumes": [
        "//var/run/docker.sock:/var/run/docker.sock"
      ],
      "entrypoint": [
        "sleep",
        "infinity"
      ]
    }
  }
  return app

root_compose = 'docker-compose.yml'

images = os.listdir('dockerfiles')
image_input = input_select("Select image", images)

app = dict()
if "fs" in image_input:
  folder_name = input("Fill folder name workspace: ")
  app = add_fs_app(folder_name, image_input)

elif "container" in image_input:
  app_name = input('Fill App name: ')
  github_url = input("Fill github repository url: ")
  app = add_container_app(app_name, github_url, image_input)

else:
  app = add_app(image_input)

with open(root_compose, 'r') as fp:
  config: dict = yaml.safe_load(fp)

config['services'] = config['services'] | app
with open(root_compose, 'w') as fp:
  yaml.dump(config, fp)

