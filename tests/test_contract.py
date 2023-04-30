from brownie import BasicContract, accounts, config

def test_default_value():
    account = accounts.add(config["account-keys"]["private-key"]) #Accessing the account from the brownie config file
    deploy_contract = BasicContract.deploy({"from":account})
    retrieved_number = deploy_contract.readNumber()
    expected_result = 0
    assert retrieved_number == expected_result

def test_stored_value():
    account = accounts.add(config["account-keys"]["private-key"])
    deploy_contract = BasicContract.deploy({"from":account})
    transaction_receipt = deploy_contract.storeNumber(15,{"from":account})
    transaction_receipt.wait(1)
    retrieved_number = deploy_contract.readNumber()
    expected_result = 15
    assert retrieved_number == expected_result