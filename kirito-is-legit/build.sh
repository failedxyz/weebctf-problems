docker stop $(docker ps --filter "ancestor=kirito" -q)
docker rm $(docker ps -q -f status=exited)
docker build -t kirito $DIRECTORY
tmux kill-session -t kirito
docker rm kirito
tmux new-session -s kirito -d "docker run -it -p 6002:80 --name kirito kirito"