echo "Startiing Backend"

fuser -k 3000/tcp
fuser -k 5000/tcp
. .venv/bin/activate
python3 backend/main.py & disown
sleep 5
echo "Starting Frontend"
npm start & disown
