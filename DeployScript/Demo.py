import requests

if __name__ == "__main__":
    try:
        url = "https://www.techcronus.com/staging/db-script/ems.sql"
        filename = "ems.sql"  # Adjust filename as needed
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"File '{filename}' downloaded successfully!")
    except requests.exceptions.RequestException as err:
        print(f"Error downloading file: {err}")

#         # db_config = {
#         #     'host': "ems-db.cbew84swqjs6.eu-north-1.rds.amazonaws.com",
#         #     'user': "root",
#         #     'password': "mK3CuqT8oKBsgmop5eap",
#         #     'database': 'Demo',
#         #     'port': 3306 
#         # }
#         db_config = {
#             'host': "ems-production-db.cbew84swqjs6.eu-north-1.rds.amazonaws.com",
#             'user': "root",
#             'password': "5iluHue8j9D5Nk1W6Y36",
#             'database': 'Demo',
#             'port': 3306 
#         }