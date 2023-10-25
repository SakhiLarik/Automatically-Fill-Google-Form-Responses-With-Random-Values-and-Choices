import pandas as pd
import math
import random

names_dataset = pd.read_csv("./names.csv");
newDataset = names_dataset
names = newDataset['name']

department = ['IT','BBA','English','Economics','Microbiology','Statics','Physics','Chemistry']
batch = [2022,2020,2021,2023]
email = 'example@gmail.com'

i = 0
for name in names:
    roll = math.floor(random.randint(1,100))
    newDataset['email'][i] = email
    newDataset['roll'][i] = math.floor(roll)
    newDataset['batch'][i] = math.floor(random.choice(batch))
    newDataset['department'][i] = random.choice(department)

    i = i+1
    
newDataset.to_csv('dataset.csv', index=False)

