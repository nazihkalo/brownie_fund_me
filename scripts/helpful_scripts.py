from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3
import os

DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_MAINNET_ENVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_MAINNET_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"Active network is {network.show_active()}")
    print("Deploying Mocks...")
    # Check length of MockV3Aggregator contract, if empty then deploy else use latest deployed
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            STARTING_PRICE,
            {"from": get_account()},  # Web3.toWei(STARTING_PRICE, "ether")
        )
    print("Mocks Deployed!")
