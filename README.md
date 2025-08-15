# Flask Multi-Build Container Application

A production-ready Flask web application with multi-stage Docker builds, PostgreSQL database, and modular architecture using Flask Blueprints.

## 🏗️ Architecture

This application follows Flask best practices with:
- **Modular structure** using Flask Blueprints
- **Multi-stage Docker builds** for optimized production images
- **PostgreSQL database** with SQLAlchemy ORM
- **Environment-based configuration** for different deployment stages
- **WTForms** for secure form handling

## 📁 Project Structure

```
MultibuildContainer/
├── app/                    # Main application package
│   ├── __init__.py        # Application factory
│   ├── main/              # Main blueprint
│   │   ├── __init__.py    # Blueprint initialization
│   │   ├── routes.py      # Route handlers
│   │   └── forms.py       # WTForms classes
│   ├── models/            # Database models
│   │   ├── __init__.py    # Models package
│   │   └── user.py        # User model
│   ├── static/            # CSS, JS, images
│   └── templates/         # Jinja2 templates
│       └── base.html      # Base template
├── docs/                  # Documentation
├── config.py             # Configuration classes
├── requirements.txt      # Python dependencies
├── Dockerfile           # Multi-stage Docker build
├── docker-compose.yml   # Container orchestration
├── .env.example         # Environment variables template
└── .dockerignore        # Docker ignore file
```

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.11+ (for local development)

### 1. Clone and Setup
```bash
git clone <your-repo-url>
cd MultibuildContainer
cp .env.example .env
# Edit .env with your configuration
```

### 2. Run with Docker Compose
```bash
docker-compose up --build
```

The application will be available at `http://localhost:5000`

### 3. Local Development
```bash
pip install -r requirements.txt
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

## 🐳 Docker Multi-Stage Build

The Dockerfile uses a two-stage build process:

1. **Builder Stage**: Installs and compiles dependencies
2. **Production Stage**: Creates lightweight final image with only runtime requirements

This approach reduces image size and improves security by excluding build tools from the final image.

## 🗄️ Database

The application uses PostgreSQL in production with SQLAlchemy ORM:

- **Development**: SQLite (default)
- **Production**: PostgreSQL via Docker Compose

### Database Migration
```bash
# Initialize database
flask db init

# Create migration
flask db migrate -m "Initial migration"

# Apply migration
flask db upgrade
```

## ⚙️ Configuration

Configuration is managed through environment variables and config classes:

- `DevelopmentConfig`: Debug enabled, SQLite database
- `ProductionConfig`: Debug disabled, PostgreSQL database
- `TestingConfig`: Testing environment with in-memory database

## 🔐 Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
SECRET_KEY=your-secret-key-here
SQLALCHEMY_DATABASE_URI=postgresql://user:pass@localhost/dbname
FLASK_ENV=development
FLASK_DEBUG=True
```

## 📊 Available Routes

- `/` - Home page
- `/hello` - Form demonstration with name input

## 🧪 Testing

```bash
# Run tests
python -m pytest

# Run with coverage
python -m pytest --cov=app
```

## 🚢 Deployment

### Docker Production
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Manual Deployment
1. Set environment variables for production
2. Run database migrations
3. Start with a WSGI server (Gunicorn recommended)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔧 Development Notes

- Uses Flask Blueprints for modular organization
- WTForms for secure form handling with CSRF protection
- SQLAlchemy for database operations
- Multi-stage Docker builds for production optimization
- Environment-based configuration management

## 📚 Documentation

Additional documentation can be found in the `docs/` directory:
- Architecture overview
- Deployment guide
- Usage examples
