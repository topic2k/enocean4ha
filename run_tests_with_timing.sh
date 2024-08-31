#!/bin/sh
WITH_TIMINGS=1 python -m nose2  -s . --quiet --log-level 100 --with-coverage
