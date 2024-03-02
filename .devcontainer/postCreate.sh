set -eux

sudo chown -R "$(id -u):$(id -g)" /home/vscode/.cache/pypoetry
poetry install
