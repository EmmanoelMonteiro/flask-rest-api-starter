# flask-rest-api-starter
Structure of a Basic API with Flask

Complete RESTful API for people record management with CRUD operations, advanced search, and robust error handling.

## Main Features

- ✅ **Full CRUD operations** for people management
- 🔍 **Advanced search** by name with parameter validation
- 🆔 **Automatic UUID generation** for new records
- ⚠️ **Detailed error handling** with semantic HTTP codes
- 📦 **Consistent JSON serialization** across all responses
- 🛡️ **Strict validation** of inputs and parameters
- 📚 **Clear documentation** on each endpoint

## Implemented Endpoints

| Method | Endpoint | Description |
|--------|-------------------------|-------------------------------------------|
| GET | `/` | Simple health check |
| GET | `/data` | Dataset information |
| GET | `/count` | Record count |
| GET | `/name_search?q=<name>` | Search for people by first name |
| GET | `/person/<uuid>` | Retrieve person by UUID |
| POST | `/person` | Create new person with generated UUID |
| DELETE | `/person/<uuid>` | Remove person by UUID |

## How to Run

```bash
# Install dependencies
pip install flask

# Run application
python app.py

Error Handling
The API returns appropriate status codes with informative messages:

|Code | Description |
|--------|-------------------------------------------------|
| 400 | Bad Request: Invalid parameters |
| 404 | Not Found: Resource not found |
| 422 | Unprocessable Entity: Invalid input data |
| 500 | Internal Server Error: Unexpected server errors |
