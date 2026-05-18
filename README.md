# EvoSchedule 3.0

A Flask-based API for generating optimized timetables using a genetic algorithm (GA) with Firebase integration.

## Features

- **Genetic Algorithm Scheduler**: Optimizes course-to-room, lecturer, and timeslot assignments
- **Firebase Firestore Integration**: Manages courses, lecturers, rooms, departments, and generated timetables
- **Nonblocking GA Execution**: Background job processing prevents API freezing during long computations
- **RESTful API**: JSON endpoints for data management and timetable generation
- **Production-Ready**: Configured for deployment on Render with Gunicorn

## Project Structure

```
.
├── app.py                      # Flask application and API routes
├── wsgi.py                     # WSGI entry point for Gunicorn
├── gunicorn_config.py          # Gunicorn server configuration
├── render.yaml                 # Render deployment configuration
├── requirements.txt            # Python dependencies
├── key.json                    # Firebase service account (local only, git-ignored)
├── algorithm/                  # Legacy GA implementation
├── scheduler/                  # Active GA scheduler
│   ├── ga_run.py              # Main GA execution logic
│   ├── ga_background.py       # Background job worker for nonblocking runs
│   ├── ga_init_pop.py         # Population initialization
│   ├── fitness.py             # Fitness evaluation
│   ├── selection.py           # Selection operators
│   ├── crossover.py           # Crossover operators
│   ├── mutation.py            # Mutation operators
│   ├── repair.py              # Constraint repair
│   ├── timetable_builder.py   # Timetable decoding
│   └── models.py              # Data models
├── data_mgt/                  # Data management utilities
│   ├── data_loader.py         # Firestore data loading
│   └── codec.py               # Data encoding/decoding
└── utils/                     # Utility functions
    ├── models.py              # Shared models
    ├── helper.py              # Helper functions
    ├── timeslots.py           # Timeslot utilities
    └── ...
```

## Setup

### Prerequisites

- Python 3.8+
- Pip or Conda
- Firebase project with service account credentials

### Local Development

1. **Clone and enter the directory**
   ```bash
   cd EvoSchedule3.0
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   source env/Scripts/activate  # Windows
   # or
   source env/bin/activate      # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Firebase credentials**
   ```bash
   cp .env.example .env
   # Edit .env and add your FIREBASE_SERVICE_ACCOUNT_JSON
   # OR place key.json in project root
   ```

5. **Run with Flask (dev only)**
   ```bash
   python app.py
   ```
   or with Gunicorn:
   ```bash
   gunicorn --config gunicorn_config.py wsgi:app
   ```

## API Endpoints

### Data Management

- `GET /departments` - List all departments
- `POST /save_departments` - Create/update departments
- `GET /courses` - List all courses
- `POST /save_courses` - Create/update courses
- `GET /lecturers` - List all lecturers
- `POST /save_lecturers` - Create/update lecturers
- `GET /rooms` - List all rooms
- `POST /save_rooms` - Create/update rooms
- `GET /assignments` - Get lecturer-to-course assignments
- `POST /save_assignments` - Store assignments
- `GET /global_settings` - Get global GA settings
- `POST /global_settings` - Update global settings
- `POST /levels` - Store level data for departments

### Timetable Generation

- `POST /run_ga` - Start a nonblocking GA job
  - Returns: `{ "job_id": "<uuid>", "status_url": "/run_ga_status/<uuid>" }`
  - Status: `202 Accepted`

- `GET /run_ga_status/<job_id>` - Poll job status
  - Returns: Job metadata including `status`, `fitness`, `run_id`, `duration`

- `GET /get_timetable/<run_id>` - Fetch completed timetable entries

### Health Check

- `GET /` - Health check endpoint

## Configuration

### Gunicorn (`gunicorn_config.py`)

- **Binding**: `0.0.0.0:{PORT}` (respects `PORT` env var for Render)
- **Workers**: 2
- **Threads**: 2
- **Timeout**: 120s
- **Logging**: stdout and stderr

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `FIREBASE_SERVICE_ACCOUNT_JSON` | On Render | JSON service account credentials |
| `PORT` | Optional | Server port (default: 8000) |

## Deployment on Render

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Render Web Service**
   - Connect your GitHub repo
   - Choose Python 3.11+
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn --config gunicorn_config.py wsgi:app`

3. **Set Environment Variables**
   - Add `FIREBASE_SERVICE_ACCOUNT_JSON` as a secret
   - Paste the full Firebase service account JSON

4. **Deploy**
   - Render auto-deploys on push to `main`

## Usage Example

### 1. Load Data
```bash
curl -X POST http://localhost:8000/save_courses \
  -H "Content-Type: application/json" \
  -d '[{"id": "CS101", "name": "Intro to CS", ...}]'
```

### 2. Start GA Job
```bash
curl -X POST http://localhost:8000/run_ga
# Response: { "job_id": "abc123...", "status_url": "/run_ga_status/abc123..." }
```

### 3. Poll Status
```bash
curl http://localhost:8000/run_ga_status/abc123...
# Response: { "status": "running", "job_id": "abc123..." }
# When complete: { "status": "completed", "fitness": 0.95, "run_id": "2026-05-18..." }
```

### 4. Fetch Timetable
```bash
curl http://localhost:8000/get_timetable/2026-05-18...
# Response: Array of timetable entries
```

## Genetic Algorithm Details

- **Population Size**: 200 chromosomes
- **Max Generations**: 500
- **Stagnation Limit**: 80 generations without improvement
- **Fitness Function**: Evaluates room capacity, lecturer workload, time-of-day preferences
- **Operators**: Selection, crossover, mutation, repair (constraint-based)

## Security Notes

- **Firebase Credentials**: Never commit `key.json` or raw service account JSON
- **Environment Variables**: Use Render's secure secret management
- **CORS**: Enabled for all routes (configure as needed)

## Contributing

1. Create a feature branch
2. Make changes
3. Test locally
4. Push and create a PR

## License

Proprietary - EvoSchedule 3.0
