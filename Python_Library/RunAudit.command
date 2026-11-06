#!/bin/zsh
# Double-click this file to run the collector without typing a quoted file path.
audit_script_dir="$(cd -- "$(dirname -- "$0")" && pwd)"
exec /usr/local/bin/python3 -u "$audit_script_dir/audit_files.py" "$@"
