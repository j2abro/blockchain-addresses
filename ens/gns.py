'''
    Extract ENS info from Dune and add to BlockPing

    1) Get Dune data, save to CSV in this directory: in.csv
        -- 1286014 --> All contracts
        SELECT
          name,
          owner,
          evt_tx_hash,
          evt_block_time
        FROM
          ethereumnameservice."view_registrations" -- WHERE contract_address != '\x283af0b28c62c092c9727f1ee09c02ca627eb7f5' -- main contract
        LIMIT
          100

    2) Run this script and create a second file to input into BlockPing

    TO DO: Determine how to write this data: IF the owner and addr are different. Need to write two records:
        A lookup of one, must reveal the other.
'''
import json
from web3 import Web3
from ens import ENS
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

INFURA_URL = os.getenv('INFURA_URL')

# Input CSV From Dune
df = pd.read_csv ('in.csv') # print(df.columns.values) # ['name' 'owner' 'evt_tx_hash' 'evt_block_time']

w3 = Web3(Web3.HTTPProvider(INFURA_URL))
ns = ENS.fromWeb3(w3)

connected = w3.isConnected()
print('connected:', connected)

# Read in each row. Use 'owner' to also get the mapped_address which may be different.
# TODO also get 'responsible party' - So there are potentially 3 names associate with each address.
# https://eips.ethereum.org/EIPS/eip-137
for index, row in df.iterrows():
    name            = row['name']
    owner           = row['owner'].replace('\\x', '0x', 1) # convert Dune \x with 0x
    evt_tx_hash     = row['evt_tx_hash'].replace('\\x', '0x', 1)
    evt_block_time  = row['evt_block_time']
    print('-------------------------------')
    print(name, owner, evt_tx_hash, evt_block_time)
    resolved_address = ns.address(name + '.eth')
    owner_address = ns.owner(name + '.eth')
    resolver_address = ns.resolver(name + '.eth').address
    print('-------')
    print('addr :    ', resolved_address)
    print('owner:    ', owner_address)
    # print('resolver: ', resolver_address) # This is resolver address which we need if we are querying something else

    # domain = ns.name('0x5B2063246F2191f18F2675ceDB8b28102e957458') # print(domain)

# Another approach to get owner directly from contract on chain
# ABI for Ethereum Name Service contract: ENS
ens_json = '''
{ "abi":[{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"resolver","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"label","type":"bytes32"},{"name":"owner","type":"address"}],"name":"setSubnodeOwner","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"ttl","type":"uint64"}],"name":"setTTL","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"ttl","outputs":[{"name":"","type":"uint64"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"resolver","type":"address"}],"name":"setResolver","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"owner","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"owner","type":"address"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":true,"name":"label","type":"bytes32"},{"indexed":false,"name":"owner","type":"address"}],"name":"NewOwner","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"resolver","type":"address"}],"name":"NewResolver","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"ttl","type":"uint64"}],"name":"NewTTL","type":"event"}]
}
'''
# ens_abi = json.loads(ens_json)
# 0x314159265dD8dbb310642f98f50C066173C1259b - ENS
# 0x283Af0B28c62C092C9727F1Ee09c02CA627EB7F5 - ETHRegistrarController
# ens_contract_addr = '0x314159265dd8dbb310642f98f50c066173c1259b'
# ens_contract = w3.eth.contract(Web3.toChecksumAddress(ens_contract_addr), abi=ens_abi['abi'])
# node = '0xc29d8fae38799363df59ca667807dded37958ea619c3ef57e05f5dfeba483944'
# owner = ens_contract.functions.owner(node).call()
# print('owner:', owner)
