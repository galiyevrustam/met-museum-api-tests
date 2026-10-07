# Met Museum API Tests

Automated tests for the [Metropolitan Museum of Art Collection API](https://metmuseum.github.io)
built with Python, Pytest and Pydantic v2.

## What is covered

- `GET /objects/{objectID}` — valid & invalid ids, schema validation.
- `GET /objects` — bulk enumeration and department filtering.
- `GET /v1.1/search` — keyword search, filters, pagination (offset/limit).
- `GET /search` (deprecated v1) — still works until 2026-10-01.
- `GET /departments` — list shape, unique positive ids.
## Install

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt