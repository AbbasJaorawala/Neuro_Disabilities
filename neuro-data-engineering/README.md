# Neuro Data Engineering Project

This project implements a data engineering pipeline for collecting, processing, and analyzing neurological behavioral data. It follows modern data engineering practices to handle real-time behavioral metrics and generate actionable insights.

## Data Engineering Architecture

### Data Collection Layer
- Real-time behavioral data collection
- Screen time monitoring
- Focus metrics tracking
- Application usage patterns
- Data validation and sanitization

### Data Pipeline
```
Raw Data → Landing Zone → Processing → Feature Store → Analytics
```
- **Landing Zone**: Raw events in JSON/Parquet format
- **Processing Layer**: Data cleaning, transformation, and feature engineering
- **Feature Store**: Pre-computed behavioral features
- **Analytics Layer**: ML models and dashboards

### Technical Stack
- **Storage**: SQLite (local) / PostgreSQL (production), Parquet files (raw data)
- **Processing**: Pandas for batch processing
- **API**: FastAPI for real-time ingestion
- **Orchestration**: Apache Airflow (planned)
- **Dashboard**: Dash + Plotly

## Project Structure

```
src/
├── collectors/          # Data collection services
│   └── start_collection.py
├── api/                 # REST API
│   ├── routes/
│   │   └── data_ingestion.py
│   └── server.py
├── pipelines/           # Data processing pipelines
│   └── ingest_pipeline.py
├── ml/                  # ML models & features
│   └── features/
│       └── behavioral_features.py
├── warehouse/           # Data warehouse schemas
│   └── init_db.py
├── processing/          # Data processing (existing)
│   └── process_data.py
├── analysis/            # Data analysis (existing)
│   └── analyze_data.py
└── utils/               # Utility helpers
    └── helpers.py

data/
├── landing/             # Raw data landing zone
├── processed/           # Cleaned and transformed data
├── features/            # Computed feature sets
└── models/              # Trained ML models

config/
├── collectors_config.yaml

notebooks/
└── exploratory_analysis.ipynb

tests/
├── unit/
└── integration/
```

## Data Engineering Workflows

### 1. Data Ingestion Pipeline
```
Daily Collection → Validation → Landing Zone
Schedule: Every 60 seconds (configurable)
```

### 2. Feature Engineering Pipeline
```
Raw Data → Cleaning → Feature Computation → Feature Store
Schedule: Hourly
```

### 3. Analytics Pipeline
```
Features → ML Models → Insights → Dashboard
Schedule: Daily
```

## Setup Instructions (PowerShell / Windows)

1. Install dependencies:
```powershell
pip install -r requirements.txt
```

2. Initialize the database (SQLite default):
```powershell
python src/warehouse/init_db.py
```

3. Start the API server:
```powershell
uvicorn src.api.server:app --reload --port 8000
```

4. Start the sample collector (in another terminal):
```powershell
python src/collectors/start_collection.py
```

5. Process landing files to parquet (in another terminal):
```powershell
python -c "from src.pipelines.ingest_pipeline import ingest_landing_files; ingest_landing_files()"
```

6. Test API ingest endpoint:
```powershell
$body = @{
    user_id = "user_456"
    timestamp = (Get-Date).ToUniversalTime().ToString("o")
    event_type = "app_focus"
    duration = 15
    metadata = @{}
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/ingest" -Method POST -Body $body -ContentType "application/json"
```

## API Endpoints

- `GET /health` — Health check
- `POST /api/ingest` — Ingest behavioral event

### Example Ingest Request

```json
{
  "user_id": "user_123",
  "timestamp": "2025-11-10T10:30:00Z",
  "event_type": "screen_on",
  "duration": 12.5,
  "metadata": {}
}
```

## Data Collection

Raw events are collected via:
1. **Collectors**: `src/collectors/start_collection.py` — periodic sampling
2. **API**: `POST /api/ingest` — real-time ingestion

All events land in `data/landing/` as CSV files.

## Processing Pipeline

Run the ingest pipeline to convert CSV → Parquet:

```powershell
python -c "from src.pipelines.ingest_pipeline import ingest_landing_files; ingest_landing_files()"
```

Processed files move to `data/processed/`.

## Feature Engineering

Compute behavioral features:

```python
from src.ml.features.behavioral_features import compute_session_features
import pandas as pd

df = pd.read_parquet("data/processed/event_1234567890.parquet")
features = compute_session_features(df)
print(features)
```

## Monitoring & Maintenance

- API health: `http://localhost:8000/health`
- Database: `data/neuro.db` (SQLite)
- Logs: `app.log`

## Data Governance

- Data retention: 90 days for raw data
- Encryption: AES-256 for sensitive data (future)
- Access control: Role-based access (future)
- Compliance: GDPR, HIPAA guidelines

## Next Steps

- [ ] Add unit tests for collectors, pipelines, features
- [ ] Add Airflow DAG for orchestration
- [ ] Build Dash dashboard
- [ ] Implement model training for condition detection
- [ ] Add data quality checks
- [ ] Set up GitHub Actions CI/CD

## Contributing

1. Create a feature branch: `git checkout -b feat/your-feature`
2. Commit changes: `git commit -m "feat: your message"`
3. Push and open a PR: `git push -u origin feat/your-feature`