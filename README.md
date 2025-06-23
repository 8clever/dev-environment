# Dev Environments
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

##  CLI
For use cli run `./exec/bin.sh` and follow prompts suggestions

Requirements:
- **Python3**

Commands:
- **add** - add dev enviroment
- **list** - list dev environments in your compose file
- **rm** - remove dev environment from your compose file