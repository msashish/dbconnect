#!/usr/bin/env bash

rm reports/unittest.txt
rm -R reports/coverage
rm reports/coverage.xml
python3.6 -m coverage run --include='application/*' --branch -m unittest discover -b -v 2> >(tee -a reports/unittest.txt >&2)
UNITTEST_RESULT=$?
python3.6 -m coverage html --directory reports/coverage
python3.6 -m coverage xml -o reports/coverage.xml
python3.6 -m coverage report
exit $UNITTEST_RESULT
