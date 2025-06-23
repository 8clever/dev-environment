# Dev Environments [Beta]
Create **docker-compose.yml** file with dev environments

Supported environments:
- **foundry anvil** - dev node for working with foundry
- **foundry container** - foundry dev environment
- **node container** - node.js dev environmen
- **node fs** - node.js dev environment
- **python fs** - python dev environment

**[name] container** - it is mean that you will developing in docker container directly usualy for front-end web interfaces that required **hot reloading**

**[name] fs** - it is mean that you will developing in custom folder in your hard drive usualy for services which does not require hot reloading

Requirements:
- **Docker Engine**
- **Dev Containers [VSCode extension]**

For usage copy this repository to your hard drive and then use CLI or manually create **docker-compose.yml**. For refference use **docker-compose.example.yml**. 
Then just up your environment ```docker compose up [env] -d``` and attach **vscode** to container

##  CLI [Windows]
For use cli run `./exec/bin/main.exe` and follow prompt suggestions

Commands:
- **add** - add dev enviroment
- **list** - list dev environments in your compose file
- **rm** - remove dev environment from your compose file

## Access to Private Repositories

Drop `.ssh` folder with private keys to root folder, this folder will directly copied to container and container will fully access private repositories or hostings

## Support

If you have any questions or you have feature suggestion feel free to write issue

## Future Updates
- GUI
- Portable Version