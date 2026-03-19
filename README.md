### Hexlet tests and linter status:
[![Actions Status](https://github.com/DenisShutov/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DenisShutov/python-project-83/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DenisShutov_python-project-83&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DenisShutov_python-project-83)

### Page analyzer
[Project Reference](https://python-project-83-ncw2.onrender.com)

**Page Analyzer** is an educational project from Hexlet that analyzes SEO metrics of web pages.  
The service checks headers, meta tags, and HTTP response codes.

> ⚠️ **Note**: The service is hosted on [Render.com](https://render.com) with a **temporary database**.  
> The data may be reset periodically. Hurry up to try it! 🏃‍♂️

### Local setup
```bash
# 1. Clone the repository
git clone https://github.com/DenisShutov/python-project-83.git
# 2. Move to the repository
cd python-project-83

# 3. Install dependencies
make install

# 4. Create .env and setup SECRET_KEY and DATABASE_URL 
touch .env
# Open .env and add:
# SECRET_KEY=your_secret_key
# DATABASE_URL=postgresql://user:password@localhost:5432/db_name

# 5. Initialize the database
psql -d <your_database_name> -f database.sql
# 6. Run in dev mode
make dev
```