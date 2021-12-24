from brownie import FundMe, network, accounts, exceptions
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    deploy_mocks,
)
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    min_entrance_fee = fund_me.getEntranceFee() + 10000
    # Action
    tx = fund_me.fund({"from": account, "value": min_entrance_fee})
    tx.wait(1)
    # Assert
    assert fund_me.addressToAmountFunded(account.address) == min_entrance_fee
    # Action
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    # Assert
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    # assert fund_me.add
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
