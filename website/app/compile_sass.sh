#!/usr/bin/env bash

# This is a simple little script which compiles the
# SASS files for the application into CSS in the right place.

echo "Compiling Bootstrap"
sass ./sass_src/_bootstrap.scss:microbug/static/microbug/css/bootstrap.css

echo "Compiling Font Awesome"
sass ./sass_src/font-awesome.scss:microbug/static/microbug/css/font-awesome.css

echo "All sass compiled"
