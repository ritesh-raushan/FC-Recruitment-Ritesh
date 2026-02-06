# Blog Posts API

A REST API built with FastAPI for managing blog posts. Uses PostgreSQL for data storage and runs entirely in Docker containers.

## What it does

Basic CRUD operations for blog posts:
- Create new posts
- Retrieve all posts
- Update existing posts
- Delete posts

Each post has a title, content, author name, and timestamp.

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic for validation
- Docker & Docker Compose

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- That's it

### Running the application

1. Clone the repository
2. Create a `.env` file in the root directory:

```env
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
```

3. Start everything:

```bash
docker compose up -d
```

This starts three containers:
- PostgreSQL database
- FastAPI application
- Adminer (database management UI)

### Access points

- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Adminer: http://localhost:8080

## API Endpoints

### Create a post
```
POST /posts/
```
Body:
```json
{
  "title": "Post title",
  "content": "Post content here",
  "author": "Author name"
}
```

### Get all posts
```
GET /posts/
```

### Update a post
```
PUT /posts/{id}
```
Body (all fields optional):
```json
{
  "title": "Updated title",
  "content": "Updated content",
  "author": "Updated author"
}
```

### Delete a post
```
DELETE /posts/{id}
```

## Development

The application automatically reloads when you change code files. Just edit and save.

To view logs:
```bash
docker compose logs -f app
```

To stop everything:
```bash
docker compose down
```

## Project Structure

```
.
├── app/
│   ├── config.py       # Environment configuration
│   ├── database.py     # Database connection
│   ├── main.py         # Application entry point
│   ├── models.py       # SQLAlchemy models
│   ├── routers.py      # API endpoints
│   └── schemas.py      # Pydantic schemas
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Database

PostgreSQL with a single `posts` table. Schema is automatically created on startup.

To access the database directly through Adminer:
1. Go to http://localhost:8080
2. Use credentials from your `.env` file
3. Server: `db`