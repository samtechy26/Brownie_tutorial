from brownie import BasicContract, accounts

def test_default_value():
    account = accounts[0]
    deploy_contract = BasicContract.deploy({"from":account})
    retrieved_number = deploy_contract.readNumber()
    expected_result = 0
    assert retrieved_number == expected_result

def test_stored_value():
    account = accounts.load[0]
    deploy_contract = BasicContract.deploy({"from":account})
    transaction_receipt = deploy_contract.storeNumber(15,{"from":account})
    transaction_receipt.wait(1)
    retrieved_number = deploy_contract.readNumber()
    expected_result = 15
    assert retrieved_number == expected_result