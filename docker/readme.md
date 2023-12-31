 1. `docker run`:
   - Параметри:
     - `-d` (або `--detach`): Запускає контейнер у фоновому режимі.
     - `-p` (або `--publish`): Вказує порти, що будуть мапитися між контейнером і хост-системою.
     - `-e` (або `--env`): Встановлює змінні середовища для контейнера.
     - `-v` (або `--volume`): Цей параметр дозволяє монтувати об'єм або директорію з хост-системи до контейнера. Наприклад, -v /host/directory:/container/directory мапує директорію з хост-системи на директорію в контейнері.
     - `--name`: Цей параметр дозволяє надати ім'я контейнеру. Ви можете вказати власне ім'я для легшого визначення контейнера.
   - Пояснення: Команда `docker run` використовується для створення та запуску нового контейнера на основі Docker-образу. Параметри дозволяють налаштовувати різні аспекти контейнера, такі як мережеві порти, змінні середовища та інше.

2. `docker build`:
   - Параметри:
     - `-t` (або `--tag`): Вказує тег (ім'я та версію) образу, який буде створено.
     - `-f` (або `--file`): Вказує ім'я Dockerfile для побудови образу.
   - Пояснення: Ця команда використовується для створення Docker-образу на основі Dockerfile, який містить інструкції для побудови образу.

3. `docker images`:
   - Параметри: відсутні.
   - Пояснення: Ця команда виводить список всіх Docker-образів, які знаходяться на вашій системі.

4. `docker ps`:
   - Параметри:
     - `-a` (або `--all`): Виводить всі контейнери, включаючи припинені.
   - Пояснення: Команда `docker ps` виводить список активних контейнерів, які виконуються в даний момент.

5. `docker stop`:
   - Параметри: вказується ідентифікатор або ім'я контейнера, який потрібно зупинити.
   - Пояснення: Використовується для зупинки виконання контейнера.

6. `docker start`:
   - Параметри: вказується ідентифікатор або ім'я контейнера, який потрібно запустити.
   - Пояснення: Команда дозволяє відновити виконання зупиненого контейнера.

7. `docker exec`:
   - Параметри:
     - `-it` (або `--interactive` та `--tty`): Забезпечує інтерактивний доступ до контейнера.
   - Пояснення: Використовується для виконання команд всередині контейнера.

8. `docker pull`:
   - Параметри: вказується ім'я та версія образу для завантаження.
   - Пояснення: Команда завантажує Docker-образ з реєстру образів (наприклад, Docker Hub) на вашу систему.

9. `docker rmi`:
   - Параметри: вказується ім'я або ідентифікатор образу для видалення.
   - Пояснення: Команда видаляє Docker-образ з вашоєї системи.

10. `docker rm`:
    - Параметри: вказується ідентифікатор або ім'я контейнера для видалення.
    - Пояснення: Використовується для видалення контейнера з системи.