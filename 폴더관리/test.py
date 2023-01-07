import requests
if __name__ == "__main__":
    proxy_url = 'https://mycarpage.io/api/v3/proxyapi/'
    data = {
        'key': 'asdjqwejiqponsc',
        'url': "http://carport.kbchachacha.com/public/mycarpage/api/car/search.json",
        'data': {"carNo": "319서6629", "vin": None},
        'headers': {"client_id": "6SuDl1RDz7", "client_secret": "5485G1293He8p6e85Nx6hZ9zh782Mll8onokF3R5",
                    "Content-Type": "application/x-www-form-urlencoded"},
        'method': 'POST',
    }
    car_data = requests.post(proxy_url, data=data)
    print(car_data)