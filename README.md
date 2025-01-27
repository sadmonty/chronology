
# Сhronology

Простое веб-приложение на Flask для сохранения текстовых записей с временными метками в заданном часовом поясе.

## Функциональность
- Сохранение текстовых записей через веб-форму.
- Автоматическая установка временной метки.
- Хранение данных в SQLite.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/sadmonty/chronology.git
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите приложение:
   ```bash
   python app.py
   ```

4. Откройте браузер и перейдите по адресу:
   ```
   http://127.0.0.1:7000
   ```

## Структура проекта
```
.
├── app.py             # Основной файл приложения
├── database.db        # SQLite база данных
├── templates/
│   └── index.html     # HTML-шаблон для интерфейса
├── static/            # Статические файлы (CSS, изображения и т.д.)
├── venv/              # Виртуальное окружение
└── requirements.txt   # Список зависимостей
```

## Будущие доработки
- Отображение сохраненных записей на главной странице.
- Добавление CSS для улучшения интерфейса.
- Реализация функций редактирования и удаления записей.
