if [ -z "$@" ]; then
  echo Dev environments cli
  echo - add  - add dev environment 
  echo - rm   - remove dev environment 
  echo - list - view dev environments
else
  python3 -m cli.$@
fi