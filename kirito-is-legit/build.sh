echo "Preparing Docker..."
docker stop $(docker ps --filter "ancestor=kirito" -q)
docker rm $(docker ps -q -f status=exited)

echo "Building container for 'Kirito is Legit'..."
docker build -t kirito $DIRECTORY

echo "Running the container..."
tmux kill-session -t kirito
docker rm kirito
tmux new-session -s kirito -d "tmux set remain-on-exit on && docker run -it -p 6002:80 --name kirito kirito"

echo "Done."