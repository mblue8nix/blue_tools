from multiprocessing import cpu_count
import pandas as pd
from faker import Faker
import argparse
import sys
from tqdm import tqdm

# This script generates data in json, csv or parquet format
# mblue Feb 2023

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', nargs='*', dest="data_file", help='name for the file -e user_data.parquet')
parser.add_argument('--records','-r', nargs='*', dest="num_records", type=str, help='Enter the amount of records like 100 = 100 rows of data')
parser.add_argument('--format', dest="format_name", type=str, help="Specify the format of the output")
args = (parser.parse_args())

# arg conditions 
if args.data_file:
    FNAME = ''.join(args.data_file)
else:
    # Setting default value
    FNAME = "fake_user_data"

if args.num_records:
    REC = ''.join(args.num_records)
else:
    REC = 100

# limited error handling
# *TODO: Better handling   
if args.format_name is None:
    print("Needs 'csv, json or parquet' format argument:\n\
    Usage is: python3 data_generator --name mytestdata --records 1000 --format parquet")
    sys.exit()

if args.format_name:
    FORMAT = ''.join(args.format_name)
    print("\nCreating file", FNAME + '.' + FORMAT + " with", '\'' + REC +  '\'', 'rows: \n')

# Create an instance of Faker
fake = Faker('en-US')
CPU_CORES = cpu_count() -1 
# Create a pandas DataFrame
df = pd.DataFrame(columns=['Email_Id', 'Name', 'Game_Id','Device', 'Phone_Number','Address', \
    'City', 'Year', 'Time', 'Link', 'Money_Spent' ])

# To create email addresses
first_name = fake.first_name()
last_name = fake.last_name()

# Generate Fake Data

REC = int(REC)
x = int(REC/CPU_CORES)
for _ in tqdm(range(int(x))):

    first_name = fake.first_name()
    last_name = fake.last_name()
    game_id = fake.random_int()

    df = pd.concat([df, pd.DataFrame({
        'Email_Id': f"{first_name}.{last_name}@{fake.domain_name()}",
        'Name': first_name + " " +last_name,
        'Game_Id': game_id,
        'Device': fake.ios_platform_token(),
        'Phone_Number' : fake.phone_number(),
        'Address' : fake.address(),
        'City': fake.city(),
        'Year':fake.year(),
        'Time': fake.time(),
        'Link': fake.url(),
        'Money_Spent': fake.random_int(min=5, max=1000) 
    }, index=[0])], ignore_index=True)

def head_it():
    h1 = df.head(3)
    print("\nSample Data:\n", h1.to_string(index=False),"\n")

#Global message 
def Message():

    MESSAGE = f"\nCreated file: " + FNAME + "\nWith " + str(REC) + " rows\n"
    print(MESSAGE)

# Write to CSV
if args.format_name == "csv":
    head_it()
    FNAME = FNAME + ".csv"
    df.to_csv(FNAME, index=False)
    head_it()
    Message()
    sys.exit()

# Write to Parquet
if args.format_name == "parquet":
    FNAME = FNAME + ".parquet"
    df.to_parquet(FNAME)
    head_it()
    Message()
    sys.exit()

# Write to Json
if args.format_name == "json":
    FNAME = FNAME + ".json"
    df.to_json(FNAME, orient='records')
    head_it()
    Message()
    sys.exit()

else:
    print("Format not supported must be either 'csv, json or parquet' format.")
