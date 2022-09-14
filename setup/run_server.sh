echo "Killing any process on port 3000"
fuser -k 3000/tcp
sleep 2
echo "Killing any process on port 5001"
fuser -k 5001/tcp
sleep 2
echo "Starting Backend"
source setup/run_backend.sh
sleep 2
echo "Starting Frontend"
npm install
npm start & disown
