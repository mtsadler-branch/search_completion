# Create virtual environment, if needed
if [ ! -d ".venv/" ]; then
    echo "Installing virutalenv..."
    python3 -m pip install virtualenv
    echo "Creating .venv/..."
    python3 -m virtualenv .venv/
fi

# Activate virtual environment, if one isn't active
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating Virtual Environment..."
    . .venv/bin/activate
else
    echo -e "Deactivating Virtual Environment: $VIRTUAL_ENV/"
    deactivate
    echo "Activating Virtual Environment..."
    . .venv/bin/activate
fi

# Install PyPi packages (python requirements)
pip3 install -Ir requirements.txt

# Spin up back-end
python3 backend/helpers.py
python3 backend/main.py &

# Test back-end
sleep 3
echo "Running 'curl http://127.0.0.1:7000/prefix/h'"
curl http://127.0.0.1:7000/prefix/h

