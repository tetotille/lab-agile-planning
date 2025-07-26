import requests

def test_increment_and_get_counter():
    # Incrementar el contador en 2
    response = requests.post("http://127.0.0.1:8000/increment", params={"amount": 2})
    assert response.status_code == 200
    assert response.json()["counter"] == 2

    # Obtener el valor actual del contador
    response = requests.get("http://127.0.0.1:8000/counter")
    assert response.status_code == 200
    assert response.json()["counter"] == 2

if __name__ == "__main__":
    test_increment_and_get_counter()
    print("Prueba pasada: el contador es 2 después de incrementar en 2.")
