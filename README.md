# Receipt Processor

A REST API service that processes receipts and calculates points based on specific rules.

## Setup & Running

### Using Docker

1. Build the Docker image:
```bash
cd src
docker build -t receipt-processor .
```

2. Run the container:
```bash
docker run --rm -p 5000:5000 receipt-processor
```

The service will be available at `http://localhost:5000`
```

## API Endpoints

### Process Receipt
- **POST** `/receipts/process`
- Processes a receipt and returns an ID
- Request body: JSON receipt object
- Returns: `{ "id": "uuid-string" }`

### Get Points
- **GET** `/receipts/{id}/points`
- Retrieves points for a processed receipt
- Returns: `{ "points": number }`

## Example Usage

```bash
# Process a receipt
curl -X POST -H "Content-Type: application/json" -d @examples/simple-receipt.json http://localhost:5000/receipts/process

# Get points for a receipt
curl http://localhost:5000/receipts/{id}/points
```

## Error Handling

- 400 Bad Request: Invalid receipt data
- 404 Not Found: Receipt ID not found
