#!/usr/bin/env bash
set -eu

BASEDIR=$PWD
for ext in whl tar.gz
do
    package="$PWD/dist/*.$ext"
    test_dir=$(mktemp -d)
    cd $test_dir
        python3 -m venv .venv
            ./.venv/bin/pip install $package
            ./.venv/bin/python3 -c 'import dict_zip; assert dict_zip.dict_zip({}, {}) == {}; print("OK")'
        rm -rf .venv
    cd "$BASEDIR"
    rm -rf $test_dir
done
