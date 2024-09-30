echo "Starting pipeline"
python3 src/pipeline.py

echo "Starting Flask server"
flask run --host=46.17.100.206 --port=5000 # don't forget to change to 0.0.0.0 for running locally and chmod +x entrypoint.sh in bash
