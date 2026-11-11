"""Allow `python -m rag` as an alias for the CLI."""

from rag.cli import main

raise SystemExit(main())
