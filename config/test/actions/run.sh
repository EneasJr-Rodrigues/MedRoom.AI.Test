#!/bin/bash

python setup.py -q develop

# mkdir -p "$PROJECT_DIR/datalake/test"
# gsutil -m rsync -rn gs://datalake_template/* "$PROJECT_DIR/datalake/test"

ENV=test py.test --cov=med.room.* "${@:2}";
exitcode=$?
rm -f .coverage .coverage.*  # cleanup
exit $exitcode
