echo "Startiing Backend"

fuser -k 3000/tcp
fuser -k 5000/tcp
source setup/run_backend.sh
sleep 5
echo "Starting Frontend"
npm start & disown
