import json
import random
import time

from faker import Faker
from confluent_kafka import SerializingProducer
from datetime import datetime


fake = Faker()
def generateSalesTransaction():
    user = fake.simple_profile()

    return {
        "transactionId": fake.uuid4(),
        "producerId": random.choice(['product1', 'product2', 'product3', 'product4', 'product5', 'product6', 'product7', 'product8']),
        "productName": random.choice(['laptop', 'cellphone', 'tablet', 'watch', 'headphones', 'speakers', 'mouse', 'monitor']),
        "productCategory": random.choice(['electronics', 'fashion', 'grocery', 'music', 'books', 'home', 'beauty', 'sports']),
        'productPrice': round(random.uniform(100, 4000), 2),
        'productQuantity': random.randint(1, 10),
        'productBrand': random.choice(['Apple', 'Samsung', 'Sony', 'Acer', 'OnePlus', 'Google']),
        'currency': random.choice(['USD', 'EUR', 'GBP', 'JPY']),
        'customerId': user['username'],
        'transactionDate': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
        'paymentMethod': random.choice(['creditCard', 'debitCard', 'onlineTransfer'])
    }

def deliveryReport(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic} [{msg.partition}]')
def main():
    topic = 'financialTransactions'
    producer = SerializingProducer({
        'bootstrap.servers': 'localhost:9092'
    })

    curr_time = datetime.now()

    while (datetime.now() - curr_time).seconds < 120:
        try:
            transaction = generateSalesTransaction()
            transaction['totalAmount'] = transaction['productPrice'] * transaction['productQuantity']

            print(transaction)

            producer.produce(topic, key=str(transaction['transactionId']),
                             value=json.dumps(transaction),
                             on_delivery=deliveryReport)
            producer.poll(0)

            # wait 5 seconds before sending the next transaction
            time.sleep(5)
        except BufferError:
            print('Buffer Full: Waiting...')
            time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()