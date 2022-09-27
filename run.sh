set -e

export PYTHONDONTWRITEBYTECODE=1

if [ ! -d "./gunicorn/venv" ]
then
  echo "Run ansible-playbook setup.yaml to build gunicorn"
  echo "Sample usage: ./run.sh --workers=2 experiment1:app"
fi

./gunicorn/venv/bin/gunicorn "$@"
