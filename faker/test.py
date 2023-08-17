from faker import Faker
import pandas as pd
import numpy as np

fake = Faker()
tranDate = []
custName = []
cardNum = []
zipCode = []
tranAmount = []
for i in range(10):
    print(fake.date_time_between_dates("-1d", "now"))
for _ in range(10):
    print(fake.name())
for _ in range(10):
    print(fake.credit_card_number())
for _ in range(10):
    print(fake.zipcode())

df = pd.DataFrame(
    zip(tranDate, custName, cardNum, zipCode, tranAmount),
    columns=["tranDate", "custName", "cardNum", "zipCode", "tranAmount"],
)
