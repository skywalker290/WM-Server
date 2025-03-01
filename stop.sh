cd ~/WM-Meter/
git pull

PID=$(lsof -t -i:5006)

# If the PID exists, kill the process
if [ -n "$PID" ]; then
    echo "Stopping Gunicorn server with PID: $PID"
    kill -9 $PID
    echo "Gunicorn server stopped"
else
    echo "No Gunicorn process found on port 5006"
fi