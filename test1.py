#Starting of blockchain
genesis_block={
    'previous_hash':'',
        'index':0,
        'transaction':[]
}
blockchain=[genesis_block]
open_transactions=[]
owner='Max'
participants={'Max'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

#Function for last_transaction
def lst_transaction():
     if len(blockchain) < 1:
        return None
     return blockchain[-1]
#Function for last_transaction
def add_transaction(recipient,sender=owner,amount=1.0):
    transaction={'sender':sender,
                 'recipient':recipient,
                 'amount':amount
                }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)
    
def mine_block():
    last_block=blockchain[-1]
    hashed_block=hash_block(last_block)
        
    block={
        'previous_hash':'xyz',
        'index':len(blockchain),
        'transaction':open_transactions
          }
    blockchain.append(block)

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
    for(index,block) in enumerate(blockchain):
        if index==0:
            continue
        if block['previous_hash']!=hash_block(blockchain[index-1]):
            return False
        return True
   

waiting_for_input = True

while waiting_for_input:
    print('please choice')
    print('1:Add new transaction')
    print('2:Mine a new block')
    print('3:Output the blockchain block')
    print('4:Output participants')
    print('H:Manipulate the last transaction')
    print('Q:Quit')
    user_choice=get_user_choice()
    
    if user_choice=='1':
        txt_data=get_transaction_value()
        recipient,amount=txt_data
        add_transaction(recipient,amount=amount)
        print(open_transactions)
    elif user_choice=='2':
        mine_block()
    elif user_choice =='3':
        print_blockchain_element()
    elif user_choice=='4':
        print(participants)
    elif user_choice =='Q':
        waiting_for_input = False
    elif user_choice =='H':
        if len(blockchain) >=1:
            blockchain[0] = {
                'previous_hash':'',
                'index':0,
                'transaction':[{'sender':'Chris','recipient':'Max','amount':100.0}]
}
    else:
        print('INPUT INVALID!!!,ENTER THE VALID OPTION')
    #if not verify_chain():
     #  print_blockchain_element()
     #  print('Invalid Blockchain!!!')
     #  break

print('Done!')