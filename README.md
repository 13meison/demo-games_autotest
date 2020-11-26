### Развертывание test-окружения

- Установить `python` версии 3.4 или выше

- установить poetry в качестве проектного пакетного менеджера:

  ```bash
  pip install --user poetry
  poetry config virtualenvs.in-project true
  ```

- перейти в проект с тестами

- установить все зависимости:

  ```bash
  poetry install
  ```

  Актуальные зависимости можно посмотреть в файле pyproject.toml
  Окружение настроено, можно запускать тесты.
  Ставим chromedriver.exe (для хрома) или geckodriver.exe (для firefox), драйвер должен соответсвовать установленой версии браузера chrome или firefox.
  Для хрома:

```bash
poetry run pytest tests --splinter-webdriver chrome --splinter-webdriver-executable chromedriver.exe
```

ИЛИ
Для firefox

```bash
poetry run pytest tests --splinter-webdriver chrome --splinter-webdriver-executable geckodriver.exe
```



### Создание нового проекта

- Установить `python` версии 3.4 или выше
- установить poetry в качестве проектного пакетного менеджера:

  ```bash
  pip install --user poetry
  poetry config virtualenvs.in-project true
    ```

- создаем проект `poetry new <название проекта>`
- переходим в папку с проектом
- устанавливаем зависимости для тестов: `poetry install pytest-splinter`

### Установка pytest-reporter для создания html отчетов
    '''bash
    poetry add pytest-reporter-html1
    '''
Для записи отчета использовать команду:

    '''bash
    poetry run pytest --template=html1/index.html --report=report.html name_test.py

    '''
