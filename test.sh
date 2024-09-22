rm core/store.sqlite3

set -e

export FLASK_APP=core/server.py

if [ ! -d "core/migrations" ]; then
  flask db init -d core/migrations/
fi

flask db upgrade -d core/migrations/

pytest -vvv --cov --cov-report=html:html_report -s tests/