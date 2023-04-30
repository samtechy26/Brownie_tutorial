from brownie import BasicContract, accounts


def main():
    #fetch the account
    account = accounts.load("brownie-starter") # Accessing the account by loading the account directly.
    #Deploy contract
    deploy_contract = BasicContract.deploy({"from":account})
    