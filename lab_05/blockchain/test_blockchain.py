from blockchain import Blockchain


my_blockchain = Blockchain()


# my_blockchain.add_transaction('Alice', 'Bob', 10)
# my_blockchain.add_transaction('Bob', 'Charlie', 5)
# my_blockchain.add_transaction('Charlie', 'Alice', 3)


sender_1 = input("Enter sender of transaction 1: ")
recipient_1 = input("Enter recipient of transaction 1: ")
amount_1 = float(input("Enter amount for transaction 1: "))
my_blockchain.add_transaction(sender_1, recipient_1, amount_1)

sender_2 = input("Enter sender of transaction 2: ")
recipient_2 = input("Enter recipient of transaction 2: ")
amount_2 = float(input("Enter amount for transaction 2: "))
my_blockchain.add_transaction(sender_2, recipient_2, amount_2)

sender_3 = input("Enter sender of transaction 3: ")
recipient_3 = input("Enter recipient of transaction 3: ")
amount_3 = float(input("Enter amount for transaction 3: "))
my_blockchain.add_transaction(sender_3, recipient_3, amount_3)


previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("----------------------------")


print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
