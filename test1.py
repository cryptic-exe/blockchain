#Starting of blockchain
from functools import reduce
import hashlib as hl
from collections import OrderedDict
from hash import hash_string_256, hash_block
import json   
MINING_REWARD=10

genesis_block={
    'previous_hash': '',
    'index':0,
    'transactions':[],
    'proof':100
}
blockchain=[genesis_block]
open_transactions=[]
owner='Max'
participants={'Max'}

def load_data():
    with open('Blockchain.txt', mode='r') as f:
        file_content=f.readlines()
        global blockchain
        global open_transactions
        blockchain=json.loads(file_content[0][:-1])
        open_transactions=json.loads(file_content[1])

#load_data()

def save_data():
    with open('Blockchain.txt', mode='w') as f:
        f.write(json.dumps(blockchain))
        f.write('\n')
        f.write(json.dumps(open_transactions))


def valid_proof(transactions, last_hash, proof):
    guess=(str(transactions)+str(last_hash)+str(proof)).encode()
    guess_hash=hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2]=='00'

def proof_of_work():
    last_block=blockchain[-1]
    last_hash=hash_block(last_block)
    proof=0
    while not valid_proof(open_transactions, last_hash, proof):
        proof +=1
    return proof

        
def get_balance(participant):
    tx_sender=[[tx['amount'] for tx in block['transactions'] if tx['sender']==participant] for block in blockchain]
    open_tx_sender=[tx['amount' ] for tx in open_transactions if tx['sender']==participant]
    print(tx_sender)
    tx_sender.append(open_tx_sender)
    amount_sent=reduce(lambda tx_sum, tx_amt: tx_sum+sum(tx_amt[0]) if len(tx_amt)>0 else tx_sum+0, tx_sender, 0)
    tx_recipient=[[tx['amount'] for tx in block['transactions'] if tx['recipient']==participant] for block in blockchain]
    amount_received=reduce(lambda tx_sum, tx_amt: tx_sum+sum(tx_amt[0]) if len(tx_amt)>0 else tx_sum+0, tx_recipient, 0)
    return amount_received - amount_sent

#Function for last_transaction
def lst_transaction():
     if len(blockchain) < 1:
         return None
     return blockchain[-1]

def verify_transaction(transaction):
    sender_balance=get_balance(transaction['sender'])
    return sender_balance>=transaction['amount']

#Function for last_transaction
def add_transaction(recipient,sender=owner,amount=1.0):
    #transaction={'sender':sender,
     #            'recipient':recipient,
      #           'amount':amount
    #}
    transaction=OrderedDict([('sender', sender),('recipient', recipient),('amount', amount)])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False


def mine_block():
    last_block=blockchain[-1]
    hashed_block=hash_block(last_block)
    proof=proof_of_work()
    #reward_transaction={
     #   'sender':'MINING',
      #  'recipient':owner,
       # 'amount':MINING_REWARD
    #}
    reward_transaction=OrderedDict([('sender', 'MINING'),('recipient', owner),('amount', MINING_REWARD)])
    copied_transactions=open_transactions[:] 
    copied_transactions.append(reward_transaction)
    block={
        'previous_hash':'xyz',
        'index':len(blockchain),
        'transactions':copied_transactions,
        'proof':proof
    }
    blockchain.append(block)
    save_data()
    return True

def get_transaction_value():
    txt_recipient=input('enter the recipient of the transaction')
    txt_amount= float(input("enter the transaction amount "))
    return txt_recipient,txt_amount

def get_user_choice():
    return input('your choice ')

def print_blockchain_element():
    for block in blockchain:
        print("outputinggg....")
        print(block)
    else:
        print('_'*20)

#Function for checking the blockchain
def verify_chain():
    """verify the current blockchain and return true if it is valid else false"""
    for(index, block) in enumerate(blockchain):
        if index==0:
            continue
        if block['previous_hash']!=hash_block(blockchain[index-1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False
        return True
   
def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])

waiting_for_input = True

while waiting_for_input:
    print('please choice')
    print('1:Add new transaction')
    print('2:Mine a new block')
    print('3:Output the blockchain block')
    print('4:Output participants')
    print('5:Check transaction validity')
    print('H:Manipulate the last transaction')
    print('Q:Quit')
    user_choice=get_user_choice()
    
    if user_choice=='1':
        txt_data=get_transaction_value()
        recipient,amount=txt_data
        if add_transaction(recipient,amount=amount)!=1:
            print('Added Transaction!')
        else:
            print("Transaction Failed!")
        print(open_transactions)
    elif user_choice=='2':
        if mine_block():
            open_transactions = []
    elif user_choice =='3':
        print_blockchain_element()
    elif user_choice =='4':
        print(participants)
    elif user_choice =='5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are Invalid Transaction')
    elif user_choice =='Q':
        waiting_for_input = False
    elif user_choice =='H':
        if len(blockchain) >=1:
            blockchain[0] = {
                'previous_hash':'',
                'index':0,
                'transactions':[{'sender':'Chris','recipient':'Max','amount':100.0}]
}
    else:
        print('INPUT INVALID!!!,ENTER THE VALID OPTION')
    if verify_chain():
       print_blockchain_element()
       print('Invalid Blockchain!!!')
       break 
       print('Balance of {}: {:6.2f}'.format('Max', get_balance('Max')))
else:
    print('Done!')