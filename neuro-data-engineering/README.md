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
- **Storage**: PostgreSQL (metrics), Parquet files (raw data)
- **Processing**: Apache Spark / Pandas for batch processing
- **Streaming**: Kafka for real-time events
- **Orchestration**: Apache Airflow
- **Monitoring**: Prometheus + Grafana

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
```python
Daily Collection → Validation → Landing Zone
Schedule: Every 5 minutes
```

### 2. Feature Engineering Pipeline
```python
Raw Data → Cleaning → Feature Computation → Feature Store
Schedule: Hourly
```

### 3. Analytics Pipeline
```python
Features → ML Models → Insights → Dashboard
Schedule: Daily
```

## Setup Instructions

1. Set up the data infrastructure:
```bash
docker-compose up -d postgres kafka
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python src/warehouse/init_db.py
```

4. Start the collectors:
```bash
python src/collectors/start_collection.py
```

## Monitoring & Maintenance

- Pipeline health checks: `localhost:9090`
- Data quality metrics: `localhost:3000`
- Job logs: `localhost:8080`

## Data Governance

- Data retention: 90 days for raw data
- Encryption: AES-256 for sensitive data
- Access control: Role-based access
- Compliance: GDPR, HIPAA guidelines

// ...existing code...