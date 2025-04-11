# VehicleMonitorService

This is a vehicle monitoring service built with FastAPI and PostgreSQL. The project leverages asynchronous database interactions using SQLAlchemy, Alembic for migrations, and Docker for environment setup.

## Set Up

Follow the steps below to set up the project:

### 0. Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/paulmusquaro/VehicleMonitorService.git
cd VehicleMonitorService
```

### 1. Create a virtual environment with Poetry:

```bash
poetry shell
```

### 2. Install dependencies using Poetry:

```bash
poetry install
```

### 3. Start the database with Docker:

```bash
docker-compose --env-file ./src/conf/.env.development up --force-recreate
```

### 4. Apply database migrations using Alembic:

```bash
alembic upgrade head
```

### 5. Start the FastAPI server:

```bash
python main.py
```

The application will be running at `http://127.0.0.1:8000/docs`.

---

## Configuration

In the `src` folder, inside the `conf` directory, you need to create a `.env.development` file with the following content:

```bash
ENV_APP=development
DB_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/postgres
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

---

## Possible Improvements

Here are some suggestions for future improvements:

1. **Switch `id` field type to UUID**:
   - Currently, the `id` field in the models is a string. It could be changed to UUID for better uniqueness and scalability, as UUIDs are generally more robust in distributed systems.

2. **Write unit tests with pytest**:
   - Unit tests using `pytest` should be implemented for various parts of the application to ensure proper functionality and to prevent future bugs. This includes testing the routes, services, and database interactions.

3. **Add better error handling and logging**:
   - Improve error handling across the application and ensure that all exceptions are logged properly for easier debugging and tracking of issues in production environments.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
