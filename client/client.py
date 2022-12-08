import csv
from pathlib import Path
import requests

script_location = Path(__file__).absolute().parent

def get_user_data():
    users = []
    with open(script_location / 'generated_data/users.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter = ' ')
        headings = next(reader)

        return [row[:] for row in reader]
    

def get_users_transactions(users):
    with open(script_location / 'generated_data/transactions.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter = ' ')
        headings = next(reader)
        reader_list = list(reader)

        transactions_per_user = []
        users_consumptions = []
        for _ in users[:100]:
            transactions_per_user.extend(row for row in reader_list if _[0].split(',')[0] == row[0].split(',')[1])
            users_consumptions.append(get_total_value_transactions_user(transactions_per_user, _))
        return users_consumptions


def get_total_value_transactions_user(transactions, user):
    with open(script_location / 'generated_data/gas_stations.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter = ' ')
        headings = next(reader)
        reader_list = list(reader)

        total_amount_paid = float()
        total_liters = int()

        for _ in transactions:
            for row in reader_list:
                if _[0].split(',')[2] == row[0].split(',')[0]:
                    total_amount_paid += int(_[0].split(',')[3]) * float(row[0].split(',')[1])
                    total_liters += int(_[0].split(',')[3])
        return f"{_[0].split(',')[1]}, {str(total_liters)}, {str(total_amount_paid)}, {user[0].split(',')[1]}"


#Function to send predictions(Predictions not implemented)
def send_prediction():
    json_prediction={
            "project_name": "raizen_gasoline",
            "table_name": "fraud",
            "outlier": "1 0.3"
        }
    res = requests.post('http://api:8000/api/create_outlier/', json=json_prediction, timeout=5)
    print(f"Status code {res.status_code} para dos dados: {json_prediction}")


if __name__ == '__main__':
    print('Init client')

    users = get_user_data()
    total_transaction = get_users_transactions(users)
    print(f"Total value from first 500 users: \n {total_transaction}")
    send_prediction()


