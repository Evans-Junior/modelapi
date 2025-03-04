# Health Assistant API

This API provides predictive health diagnostics using a deep learning model.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API:
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
   ```

## Endpoints

- `GET /` - Home route
- `POST /health/get_advice/` - Get health advice from the model

## Example Request

```bash
curl -X 'POST' 'http://127.0.0.1:8000/health/get_advice/' -H 'Content-Type: application/json' -d '{"sensor_data": {"temperature": 98.6, "oxygen": 95}, "symptoms": "shortness of breath"}'
```

## Swagger UI

- Open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
