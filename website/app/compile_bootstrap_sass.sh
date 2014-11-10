#!/usr/bin/env bash

# This is a simple little script which compiles the
# Twitter Bootstrap code from the scss template into the
# CSS in the /static area of the Microbug application.

echo "Compiling SCSS"
sass ./bootstrap_src/sass/_bootstrap.scss:microbug/static/microbug/css/bootstrap.css
