import requests
import time

# mark_data = {"nickname": "hzumaeta","controlPoint": 1}
# resp = requests.post('http://localhost:3000/api/marks', data=mark_data)


def main():
    # Define la URL del recurso REST
    url = "https://example.com/api/v1/users"
    mark_data = {"nickname": "hzumaeta","controlPoint": 1}

    # Itera 5 veces
    for i in range(5):
        # Realiza la llamada a HTTP REST
        response = requests.post('http://localhost:3000/api/marks', data=mark_data)

        # Imprime la respuesta
        print(response.text)

        time.sleep(10)

if __name__ == "__main__":
    main()
