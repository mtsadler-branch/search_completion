echo "Starting Backend"

fuser -k 3000/tcp
sleep 2
fuser -k 5001/tcp
sleep 2
. .venv/bin/activate
sleep 5
python3 backend/main.py & disown
sleep 5
echo "Starting Frontend"
npm start & disown
