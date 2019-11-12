#Starting of blockchain
blockchain=[]

#Function for last_transaction
def lst_transaction():
     if len(blockchain) < 1:
        return None
     return blockchain[-1]
#Function for last_transaction
def add_transaction(transaction_amount,last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction,transaction_amount])

def get_transaction_value():
    return float(input("enter the transaction amount "))

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
    print('2:Output the blockchain block')
    print('H:Manipulate the last transaction')
    print('Q:Quit')
    user_choice=get_user_choice()
    
    if user_choice=='1':
        txt_amount=get_transaction_value()
        add_transaction(txt_amount,lst_transaction())
    elif user_choice =='2':
        print_blockchain_element()
    elif user_choice =='Q':
        waiting_for_input = False
    elif user_choice =='H':
        if len(blockchain) >=1:
            blockchain[0] = [2]
    else:
        print('INPUT INVALID!!!,ENTER THE VALID OPTION')
    if not verify_chain():
        print_blockchain_element()
        print('Invalid Blockchain!!!')
        break

print('Done!')


dsfadf

sadf
sfds