#!/usr/bin/env bash
set -eu

package=$PWD/dist/*.whl
test_dir=$(mktemp -d)
cd $test_dir
python3 -m venv .venv
./.venv/bin/pip install $package
./.venv/bin/python3 -c 'import dict_zip; assert dict_zip.dict_zip({}, {}) == {}; print("OK")'
rm -rf .venv
rm -rf $test_dir
