import requests
url = "https://archival-rpc.mainnet.near.org"
import csv

def extract_chunk_values(response):
    chunks = response['result']['chunks']
    chunk_values = []
    for chunk in chunks:
        chunk_values.append(chunk['chunk_hash'])
    return chunk_values

# function to return a list of chunks in a specific block
def get_chunks_from_block(block_id):
  url = "https://archival-rpc.mainnet.near.org"
  payload = {
   "jsonrpc": "2.0",
   "id": "dontcare",
   "method": "block",
   "params": {
     "block_id": block_id
   }
  }
  response = requests.post(url, json=payload)
  return extract_chunk_values(response.json())


#print(response.json())
chunks = get_chunks_from_block(91226650)
print(chunks)
# function to get data of any chunk based on its hash/id
# you can get a list of chunk hashes of any block using get_chunks_from_block()
def get_chunk(chunk_hash):
  payload = {
    "jsonrpc": "2.0",
    "id": "dontcare",
    "method": "chunk",
    "params": {
        "chunk_id": chunk_hash
      }
  }
  response = requests.post(url, json=payload)
  return response.json()


current_chunk = get_chunk(chunks[0])
print(current_chunk)

# function to extract transaction(s) from a given chunk response

def extract_transfer_transactions(response):
    transactions = response["result"]["receipts"]
    transfer_transactions = []

    for transaction in transactions:
        action = transaction["receipt"]["Action"]
        if "Transfer" in action["actions"][0]:
            transfer = action["actions"][0]["Transfer"]
            #print(transaction.keys())
            sender = transaction["receipt"]["Action"]["signer_id"]
            receiver = transaction["receiver_id"]
            amount = transfer["deposit"]
            block_id = response["result"]["header"]["height_created"]
            #print(response["result"]["header"])
            transfer_transactions.append({"sender": sender,
                                          "receiver": receiver,
                                          "amount": int(amount)/10**24,
                                          "block_id": block_id
                                          })

    return transfer_transactions[0]

row = extract_transfer_transactions(current_chunk)
print(row)

'''
# MAKE SURE THIS PART OF CODE IS COMMENTED BEFORE RUNNING TO AVOID DATA LOSS
# INITIALIZE the csv file
# This will reset the file to a blank state.

with open('transactions.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['sender', 'receiver', 'amount', 'block_id'])'''

# Function to append a transaction as a row to csv file.

def append_to_csv(transaction):
    headers = ['sender', 'receiver', 'amount', 'block_id']
    with open('transactions.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerow(transaction)

#append_to_csv(row)

# time to put all this into a loop
# one iteration of the loop makes 2 api calls.
# the limit for api calls is 600 per minute.
# I will limit the loop to 480 calls a minute for being on a safer side

import time


up_blocks_limit = 91271647
low_blocks_limit = up_blocks_limit - 50000    #for 5k blocks.


for b_id in range(low_blocks_limit,up_blocks_limit):
  time.sleep(0.25) #to limit api calls to 8/sec
  chunks = get_chunks_from_block(b_id)
  for chunk in chunks:
    current_chunk = get_chunk(chunk)
    try:
      row = extract_transfer_transactions(current_chunk)
      print(row)
      append_to_csv(row)
    except:
      print("skipped")
      continue
