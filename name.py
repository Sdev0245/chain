def all_participant():
    print participants	
def get_all_transaction(participant):
    tx_sender= [ [block['amount'] for block in blocks['transaction'] if block['sender'] == participant] for blocks in blockchain]
    print tx_sender
    total_send = 0 
    print tx_sender
    for tx in tx_sender:
        if len(tx) >0:
            total_send = total_send+tx[0]
    tx_received= [ [block['amount'] for block in blocks['transaction'] if block['recepient'] == participant] for blocks in blockchain]
    total_received = 0 
    for tx in tx_received:
        if len(tx) >0:
            total_received = total_received+tx[0]
    print total_received-total_send 


while True:
    print 'Enter your choice'
    print '1. adding the value to blockchain'
    print '2. printing the blockchain'
    print '3.to mine'
    print "h to manpulate blockchain"
    print 'q. to quit the application'
    print 'p. to print blockchain'
    print '4. to print all participants'
    print '5. to print transaction'
    user_choice = get_user_choice()
    if user_choice == 1:
        recepient,amount = get_input()
        add_value('Deven',recepient=recepient,amount=amount)
    elif user_choice == 2:
        print blockchain
    elif user_choice == 'q':
        break
    
    elif user_choice == 3:
    	mine()
    elif user_choice == 4:
        all_participant()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'p':
    	print blockchain
    elif user_choice == 5:
        get_all_transaction('Deven')
    else:
    	print "enter a valid response"

    if not verify_blockchain():
    	print "Not a valid blockchain"
    	break

print 'successfully quit the application'


