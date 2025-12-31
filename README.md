# Szybkie Wyzwania (Quick Challenges)

A competitive programming platform for solving coding challenges in multiple programming languages. Built with Django REST Framework and Docker.

## Features

- **206 Coding Problems** - Wide variety of algorithmic challenges across different difficulty levels
- **Multi-Language Support** - Solve problems in Python, JavaScript, C#, or C++
- **Real-time Code Execution** - Secure sandboxed code execution using Docker containers
- **User Profiles & Progress Tracking** - Track your solved problems, submissions, and statistics
- **Experience Points & Leveling** - Earn XP and level up as you solve more problems
- **Leaderboard System** - Compete with other developers on the global leaderboard
- **Comprehensive Testing** - Each problem includes multiple test cases (visible and hidden)
- **RESTful API** - Full-featured API for integration and custom clients

## Tech Stack

### Backend
- **Django 4.2.7** - Web framework
- **Django REST Framework 3.14** - API framework
- **PostgreSQL 15** - Primary database
- **Redis 7** - Caching and message broker
- **Celery** - Asynchronous task queue for code execution
- **Docker SDK** - Secure code execution in isolated containers

### Authentication & Security
- **JWT (Simple JWT)** - Token-based authentication
- **RestrictedPython** - Code security and sandboxing
- **CORS Headers** - Cross-origin resource sharing

### Deployment
- **Docker & Docker Compose** - Containerization
- **Gunicorn** - WSGI HTTP server
- **Nginx-ready** - Production-ready setup

## Project Structure

```
szybkie-wyzwania/
├── apps/
│   ├── accounts/         # User authentication and profiles
│   ├── problems/         # Problem management and tags
│   ├── submissions/      # Code submission handling
│   ├── judge/           # Code execution and evaluation
│   └── leaderboard/     # Rankings and statistics
├── szybkie_wyzwania_project/  # Django project settings
├── templates/           # HTML templates
├── static/             # Static files (CSS, JS)
├── media/              # User-uploaded files
├── all_problems.py     # Problem data deployment script
├── docker-compose.yml  # Docker services configuration
├── Dockerfile          # Docker image definition
└── requirements.txt    # Python dependencies
```

## Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/szybkie-wyzwania.git
   cd szybkie-wyzwania
   ```

2. **Build and start Docker containers**
   ```bash
   docker-compose up -d --build
   ```

3. **Load problem data**
   ```bash
   docker exec szybkie-wyzwania-web-1 python all_problems.py
   ```

4. **Create a superuser (optional)**
   ```bash
   docker exec -it szybkie-wyzwania-web-1 python manage.py createsuperuser
   ```

5. **Access the application**
   - API: http://localhost:8000/api/
   - Admin Panel: http://localhost:8000/admin/

### Default Admin Credentials

If you loaded problems using `all_problems.py`, a default admin user is created:
- **Username:** admin
- **Password:** admin123

⚠️ **Change this password in production!**

## API Endpoints

### Authentication
```
POST   /api/auth/register/          # Register new user
POST   /api/auth/login/             # Login and get JWT tokens
POST   /api/auth/token/refresh/     # Refresh access token
GET    /api/auth/user/              # Get current user profile
PUT    /api/auth/user/update/       # Update user profile
POST   /api/auth/change-password/   # Change password
```

### Problems
```
GET    /api/problems/               # List all problems
GET    /api/problems/{id}/          # Get problem details
GET    /api/problems/tags/          # List all tags
GET    /api/problems/by-difficulty/ # Filter by difficulty
```

### Submissions
```
POST   /api/submissions/submit/     # Submit code for evaluation
GET    /api/submissions/             # List user submissions
GET    /api/submissions/{id}/       # Get submission details
GET    /api/submissions/stats/      # Get submission statistics
```

### Leaderboard
```
GET    /api/leaderboard/            # Get global rankings
GET    /api/leaderboard/top/        # Get top users
```

## Problem Difficulty Levels

- **Easy (80 problems)** - 10-30 points each
- **Medium (90 problems)** - 40-80 points each
- **Hard (36 problems)** - 100-160 points each

**Total:** 206 problems worth 11,580 points

## Development

### Running tests
```bash
docker exec szybkie-wyzwania-web-1 pytest
```

### View logs
```bash
# Web application logs
docker logs szybkie-wyzwania-web-1

# Celery worker logs
docker logs szybkie-wyzwania-celery-1

# Database logs
docker logs szybkie-wyzwania-db-1
```

### Access Django shell
```bash
docker exec -it szybkie-wyzwania-web-1 python manage.py shell
```

### Database migrations
```bash
docker exec szybkie-wyzwania-web-1 python manage.py makemigrations
docker exec szybkie-wyzwania-web-1 python manage.py migrate
```

## Docker Services

The application runs in 5 Docker containers:

1. **web** - Django application (port 8000)
2. **db** - PostgreSQL database (port 5432)
3. **redis** - Redis cache and message broker (port 6379)
4. **celery** - Celery worker for async tasks
5. **celery-beat** - Celery scheduler for periodic tasks

## Environment Variables

Create a `.env` file for production (see `.env.example`):

```env
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@db:5432/dbname
REDIS_URL=redis://redis:6379/0
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Code Execution Security

The platform uses multiple security layers for safe code execution:

1. **Docker Isolation** - Each submission runs in an isolated container
2. **Resource Limits** - CPU, memory, and time constraints
3. **RestrictedPython** - Python code sandboxing
4. **Network Isolation** - No external network access during execution
5. **Automatic Cleanup** - Containers are destroyed after execution

## Performance Features

- **Redis Caching** - Frequently accessed data cached
- **Database Indexing** - Optimized queries with strategic indexes
- **Celery Workers** - Asynchronous code execution prevents blocking
- **Connection Pooling** - Efficient database connection management

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or contributions, please open an issue on GitHub.

## Acknowledgments

- Inspired by platforms like LeetCode, HackerRank, and Codeforces
- Built with the Django and Python communities' excellent tools and libraries
