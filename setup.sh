# Create virtual environment, if needed
if [ ! -d ".venv/" ]; then
    echo "Installing virutalenv..."
    python3 -m pip install virtualenv
    echo "Creating .venv/..."
    python3 -m virtualenv .venv/
fi

# Activate virtual environment, if one isn't active
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Starting Virtual Environment..."
    . .venv/bin/activate
else
    echo -e "Using active Virtual Environment: $VIRTUAL_ENV/"
fi

pip3 install -Ir requirements.txt