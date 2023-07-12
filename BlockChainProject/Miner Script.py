#BlockChain Project Miner Code
# Members: Arturo Silva, Janvier Uwase

import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from urllib.parse import urlparse
import sys
print(sys.version)


def hash_256(string):
    return hashlib.sha256(string).hexdigest()

#use a dict like tutorial? might be easier to store in text files for later use
blockExample = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}



class Blockchain:
    def __init__(self):
        self.blocks = []
        self.nodes = set() #p2p nodes for blockchain
        self.current_transactions = []

        self.add_block(self.create_block(0, time(), [], 100, '1'))
    def add_block(self, new_block):
        self.blocks.append(new_block)
        self.current_transactions = []
    def add_transaction(self, transaction):
        self.current_transactions.append(transaction)

    def valid_chain(self, chain):
        #same code from tutorial
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False
            last_block = block
            current_index += 1
        return True
    
    def resolve_chain_conflicts(self):
        #similar code from tutorial
        nodes = self.nodes
        new_chain = None
        max_length = len(self.blocks)
        for node in nodes:
            response = request.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        if new_chain:
            self.blocks = new_chain
            return True
        return False
    
    def register_node(self, address):
        #same code from tutorial
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    @property
    def last_block(self):
        return self.blocks[-1]
    @property
    def length(self):
        return len(self.blocks)
    
    #static methods for potential separate use outside of object
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hash_256(block_string)

    @staticmethod
    def create_block(index, timestamp, transactions, proof, prev_hash):
        block = {'index': index, 
                 'timestamp': timestamp, 
                 'transactions': transactions, 
                 'proof': proof, 
                 'previous_hash': prev_hash}
        return block
    
    @staticmethod
    def create_transaction(sender, recipient, amount):
        transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
        return transaction
    
    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hash_256(guess)
        return guess_hash[:4] == "0000"
    
    @staticmethod
    def proof_of_work(last_block):
        last_proof = last_block['proof']
        last_hash = Blockchain.hash(last_block)
        proof = 0
        while Blockchain.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1
        return proof

#using flask for the networking
app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


@app.get('/mine')
def mine():
    transactions = []
    last_block = blockchain.last_block
    proof = Blockchain.proof_of_work(last_block)
    #mining reward
    blockchain.add_transaction(Blockchain.create_transaction("0", node_identifier, 1))
    prev_hash = Blockchain.hash(last_block)
    block = Blockchain.create_block(blockchain.length, time(),transactions, proof,prev_hash)
    blockchain.add_block(block)
    response = {
        'message': "New Block Created",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/new_transactions', methods=['POST'])
def get_transactions():
    values = request.get_json()
    if len(blockchain.current_transactions) >= 10:
        response = {'message': 'block full of transactions'}
        return jsonify(response)
    index = blockchain.create_transaction(values['sender'],values['recipient'],values['amount'])
    blockchain.add_transaction(index)
    response = {'message': f'Transaction added to block {index}'}
    return jsonify(response)

@app.route('/nodes_register', methods=['POST'])
def register_nodes():
    #need to manually register nodes in the network
    values = request.get_json()
    nodes = values.get('nodes')
    for node in nodes:
        blockchain.register_node(node)
    response = {'message': 'new nodes added', 'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201

@app.get('/chain_resolve')
def chain_resolve():
    replaced = blockchain.resolve_chain_conflicts()
    if replaced:
        response = { 'message': 'Our chain was replaced', 'new_chain': blockchain.blocks}
    else:
        response = { 'message': 'Our chain is correct', 'chain': blockchain.blocks}
    return jsonify(response), 200

@app.get('/chain')
def full_chain():
    response = {
        'chain': blockchain.blocks,
        'length': len(blockchain.blocks),
    }
    return jsonify(response), 200

def mine_loop():
    #possible auto mining loop that takes in transactions until full then mines the block
    num = 0
    while num < 100:
        while len(blockchain.current_transactions) < 10:
            get_transactions()
        mine()
        num += 1

def main():
    print("Program Finished!")

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)

    main()
