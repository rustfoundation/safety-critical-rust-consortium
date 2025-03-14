#!/usr/bin/env -S uv run
# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

import os
from builder import build_cli

build_cli.main(os.path.abspath(os.path.dirname(__file__)))
