# Import the Flask class from the flask module
from flask import Flask, make_response, jsonify, request
import uuid

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

@app.route("/name_search")
def name_search():
    """Find a person in the database.

    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If argument 'q' is missing
        422: If argument 'q' is present but invalid
    """
    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')

    # Check if the query parameter 'q' is missing
    if query is None:
        return {"message": "Query parameter 'q' is missing"}, 400

    # Check if the query parameter is present but invalid (e.g., empty or numeric)
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422

    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            # If a match is found, return the person as a JSON response with a 200 OK status code
            return person, 200

    # If no match is found, return a JSON response with a message indicating the person was not found and a 404 Not Found status code
    return {"message": "Person not found"}, 404

@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

@app.route("/no_content")
def no_content():
    """return 'No content found' with a status of 204
    Returns:
        string: No content found
        status code: 204
    """
    return ("No content found", 204)

@app.route("/exp")
def index_explicit():
    """return 'Hello World' message with a status code of 200

    Returns:
        string: Hello World
        status code: 200
    """
    resp = make_response(jsonify({"message": "Hello World"}))
    resp.status_code = 200
    return resp

@app.route("/count")
def count():
    try:
        # Tente retornar uma resposta JSON com a contagem de itens em 'data'
        # Substitua {insert code to find length of data} por len(data) para obter o comprimento da coleção 'data'
        return {"data count": len(data)}, 200
    except NameError:
        # Se 'data' não estiver definido e gerar um NameError
        # Retorne uma resposta JSON com uma mensagem e um código de status 500 Internal Server Error
        return {"message": "data not defined"}, 500

@app.route("/person/<var_name>")
def find_by_uuid(var_name):
    # Itere pela lista 'data' para procurar uma pessoa com um ID correspondente
    for person in data:
        # Verifique se o campo 'id' da pessoa corresponde ao parâmetro 'var_name'
        if person["id"] == str(var_name):
            # Retorne a pessoa como uma resposta JSON se uma correspondência for encontrada
            return person

    # Retorne uma resposta JSON com uma mensagem e um código de status 404 Not Found se nenhuma pessoa correspondente for encontrada
    return {"message": "Person not found"}, 404

@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    id_str = str(id)
    for person in data:
        if person["id"] == id_str:
            # Remova a pessoa da lista de dados
            data.remove(person)
            # Retorne uma resposta JSON com uma mensagem e código de status HTTP 200 (OK)
            return jsonify({"message": f"Person with ID {id_str} deleted"}), 200
    # Se nenhuma pessoa com o ID fornecido for encontrada, retorne uma resposta JSON com uma mensagem e código de status HTTP 404 (Not Found)
    return jsonify({"message": "Person not found"}), 404

@app.route("/person", methods=['POST'])
def add_by_uuid():
    # Get the JSON data from the incoming request
    new_person = request.get_json()

    # Check if the JSON data is empty or None
    if not new_person:
        # Return a JSON response indicating that the request data is invalid
        # with a status code of 422 (Unprocessable Entity)
        return jsonify({"message": "Parâmetro de entrada inválido"}), 422

    # Proceed with further processing of 'new_person', such as adding it to a database
    # or validating its contents before saving it

    # Gera UUID único
    new_id = str(uuid.uuid4())
    
    # Adiciona ID ao objeto da pessoa
    new_person['id'] = new_id
    
    # Adiciona à lista de dados
    data.append(new_person)

    # Assuming the processing is successful, return a success message with status code 200 (Created)
    return jsonify({"id": new_id}), 200

@app.errorhandler(404)
def api_not_found(error):
    return jsonify({"message": "API not found"}), 404

if __name__ == "__main__":
    app.run()

@app.route("/test500")
def test500():
    raise Exception("Forced exception for testing")

@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500