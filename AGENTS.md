# AI Contribution Guidelines

This repository contains a skeleton of the **Telegram Online Bank** project.
When modifying code, follow these rules:

1. Keep services written in **Python 3.11** using [FastAPI](https://fastapi.tiangolo.com/).
2. Add tests under each service's `tests/` folder when features are implemented.
3. Always run `pytest` in the repository root before committing. Tests may output `no tests ran` when none exist.
4. Update documentation in `docs/` together with code changes.
5. Ensure `scripts/setup.sh` installs any new Python dependencies.
