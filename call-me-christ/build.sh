DIRECTORY=/home/weebctf/weebctf-problems/call-me-christ
# set -e

echo "Preparing Docker..."
docker stop $(docker ps --filter "ancestor=christ" -q)
docker rm $(docker ps -q -f status=exited)

echo "Building container for 'Call Me Christ' from $DIRECTORY..."
docker build -t christ $DIRECTORY

echo "Running the container..."
tmux kill-session -t christ
docker rm christ
tmux new-session -s christ -d "tmux set remain-on-exit on && docker run -it -p 6003:80 --name christ christ"

echo "Done."