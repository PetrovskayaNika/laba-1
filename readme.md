#  Проект: Flask + Nginx + Docker Compose

## 📌 Описание проекта
Этот проект запускает веб-приложение Flask, распределяя нагрузку через Nginx.  
Flask-приложение развернуто в **трёх контейнерах** (`app1`, `app2`, `app3`), а `nginx` выполняет балансировку нагрузки.

---

## 🏠 Структура проекта

```
/папка_проекта
├── docker-compose.yml   # Конфигурация Docker Compose
├── Dockerfile           # Описание сборки контейнера Flask
├── nginx.conf           # Конфигурация Nginx (балансировка)
├── app/
│   ├── app.py           # Код Flask-приложения
```

---

## 🚀 Как запустить проект?

### 2️⃣ **Построй и запусти контейнеры**
```sh
docker-compose up -d --build
```
- `-d` → Запуск в фоновом режиме
- `--build` → Пересборка контейнеров

### 3️⃣ **Проверка работы**
После запуска контейнеров проверь работоспособность:

- **Главная страница**  
  ```
  http://localhost:6080/
  ```
- **Запрос `/api/v1/contact` (балансировка между `app1`, `app2`, `app3`)**
  ```sh
  curl http://localhost:6080/api/v1/contact
  ```
- **Запрос `/api/v1/group` (всегда идёт в `app1`)**
  ```sh
  curl http://localhost:6080/api/v1/group
  ```

---

📌 **Что делает Nginx?**
- `/api/v1/contact` — распределяет запросы между **трёмя Flask-серверами**.
- `/api/v1/group` — отправляет все запросы **в `app1`**.

📌 **Что делает Dockerfile?**
- Берёт **Python 3.9** как базовый образ.
- Копирует код из папки `app/` в контейнер.
- Устанавливает зависимости (`Flask`, `requests`).
- Запускает приложение (`app.py`).

---

## 🔄 Как перезапустить проект?

### Остановить контейнеры
```sh
docker-compose down
```

### Пересобрать и перезапустить контейнеры
```sh
docker-compose up -d --build
```

---

## 📌 Вывод
- **Flask** работает в трёх контейнерах.
- **Nginx** балансирует нагрузку между контейнерами.
- **Порт 6080** используется для внешнего подключения.
- **Запуск** в один шаг: `docker-compose up -d --build`.


#   l a b a - 1  
 #   l a b a - 1  
 #   l a b a - 1  
 #   l a b a - 1  
 #   l a b a - 1  
 