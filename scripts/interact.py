from brownie import BasicContract, accounts

def main():
    contract_instance = BasicContract[-1] #Accessing the latest deployment instance
    account = accounts.load("brownie-starter") # load the stored account that we used to deploy the contract
    # invoke the store function on the contract to store a number
    transaction_receipt = contract_instance.storeNumber(20, {"from":account})
    #Wait for the transaction confirmation
    transaction_receipt.wait(1)
   # Read the stored number
    retrieved_number = contract_instance.readNumber()
    #Print the stored number
    print(f"the stored number: {retrieved_number}")
