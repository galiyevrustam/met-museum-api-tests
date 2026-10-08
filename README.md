# Тесты для API Музея Метрополитен

Автоматизированные тесты для [Metropolitan Museum of Art Collection API](https://metmuseum.github.io),
написанные на Python с использованием **Pytest** и **Pydantic v2**.

## Что покрыто тестами

- `GET /objects/{objectID}` — получение объекта по ID, валидация схемы,
  проверка 404 для несуществующих ID, консистентность дат создания.
- `GET /objects` — массовое получение ID объектов, фильтрация по отделу.
- `GET /v1.1/search` — поиск по ключевому слову, все документированные
  фильтры, пагинация (`offset` / `limit`), потолок в 10 000 результатов,
  консистентность `total` между страницами.
- `GET /search` (устаревший v1) — одна проверка, что эндпоинт ещё жив
  (будет отключён 1 октября 2026).
- `GET /departments` — структура ответа, уникальные положительные ID.

## Требования

- Python 3.10+
- Зависимости из `requirements.txt`

## Установка

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate

pip install -r requirements.txt
