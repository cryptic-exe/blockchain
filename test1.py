#Starting of blockchain
genesis_block={
    'previous_hash':'',
        'index':0,
        'transaction':[]
}
blockchain=[genesis_block]
open_transactions=[]
owner='Max'

#Function for last_transaction
def lst_transaction():
     if len(blockchain) < 1:
        return None
     return blockchain[-1]
#Function for last_transaction
def add_transaction(recipient,sender=owner,amount=1.0):
    transaction={'sender':sender,
                 'recipient':recipient,
                 'amount':amount}
    open_transactions.append(transaction)
    
def mine_block():
    last_block=blockchain[-1]
    hashed_block='-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)
        
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
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
              block_index += 1
              continue
        elif blockchain[block_index][0] == blockchain[block_index-1]:
             is_valid = True
        else:
            is_valid = False
            break

    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index +=1
    return is_valid

waiting_for_input = True

while waiting_for_input:
    print('please choice')
    print('1:Add new transaction')
    print('2:Mine a new block')
    print('3:Output the blockchain block')
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
    elif user_choice =='Q':
        waiting_for_input = False
    elif user_choice =='H':
        if len(blockchain) >=1:
            blockchain[0] = [2]
    else:
        print('INPUT INVALID!!!,ENTER THE VALID OPTION')
    #if not verify_chain():
       #print_blockchain_element()
       #print('Invalid Blockchain!!!')
       #break

print('Done!')  