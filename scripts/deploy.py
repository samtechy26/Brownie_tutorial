from brownie import BasicContract, accounts


def main():
    #fetch the account
    account = accounts.load("my_sepolia")
    #Deploy contract
    deploy_contract = BasicContract.deploy({"from":account})
    # invoke the store function on the contract to store a number
    transaction_receipt = deploy_contract.storeNumber(15, {"from":account})
    #Wait for the transaction confirmation
    transaction_receipt.wait(1)
   # Read the stored number
    retrieved_number = deploy_contract.readNumber()
    #Print the stored number
    print(f"the stored number: {retrieved_number}")