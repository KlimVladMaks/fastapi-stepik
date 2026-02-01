# Заметки

## Работа с venv

```
# Создание venv
python3 -m venv .venv

# Активация venv
source .venv/bin/activate

# Деактивация venv
deactivate
```

## Установка Python-пакетов

Список всех установленных Python-пакетов нужно хранить в `requirements.txt`.

```
# Установка всех Python-пакетов из requirements.txt
pip install -r requirements.txt

# Запись всех установленных Python-пакетов в requirements.txt
pip freeze -> requirements.txt
```

## Запуск приложения

Если файл называется `main.py` и содержит `app = FastAPI()`, то запуск FastAPI происходит следующей командой:

```
uvicorn main:app --reload
```

Если файл находится по пути `folder_1/folder_2/main.py`, то для запуска FastAPI можно поместить в папки `folder_1` и `folder_2` пустые файлы `__init__.py` (т.е. `folder_1/__init__.py` и `folder_1/folder_2/__init__.py`), чтобы папки воспринимались как Python-пакеты. Далее можно выполнить следующую команду:

```
uvicorn folder_1.folder_2.main:app --reload
```

Также можно просто перейти в нужную папку с помощью `cd` и запустить FastAPI стандартным образом:

```
cd folder_1/folder_2
uvicorn main:app --reload
```
