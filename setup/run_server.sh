echo "Startiing Backend"
source setup/run_backend.sh > logs.txt 2>&1 & disown
sleep 5
echo "Starting Frontend"
npm start > logs.txt 2>&1 & disown
