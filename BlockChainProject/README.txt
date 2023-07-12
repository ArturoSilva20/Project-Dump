## Basic BlockChain program
Members:
- Arturo Silva
- Janvier Uwase

based on https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

Similar to the code from above it uses flask to handle some of the program's networking 

it uses cURL to communicate with our local instance of the blockchain or someone else's across the network.

Mining currently mines only one block at a time due to the dependence of cURL


## How to run
1. make sure to have flask and pipenv installed
2. run the server pipenv
	$pipenv run python "Miner Script.py"
	Optional port setting
	$pipenv run python "Miner Script.py" -p <prefered port>
3. in a seperate terminal use cURL to interact with it

cURL commands available with the program
```
$curl http://localhost:5000/mine
```
```
$curl http://localhost:5000/chain_resolve
```
```
$curl http://localhost:5000/chain
```
```
$curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "<your address>",
 "recipient": "<recipient address>",
 "amount": 5
}' "http://localhost:5000/new_transaction"
```
```
$curl -X POST -H "Content-Type: application/json" -d '{
 "nodes": [<node_ip>...]
}' "http://localhost:5000/nodes_register"
```