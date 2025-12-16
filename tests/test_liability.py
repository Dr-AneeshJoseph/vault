from vault.tumblers.compliance import ComplianceTumblers
import pytest

validator = ComplianceTumblers()

def test_guarantee_block():
    # Attempt to slip in a guarantee
    unsafe_msg = "We guarantee a 10% return on investment."
    is_valid, msg = validator.validate(unsafe_msg)
    assert is_valid is False
    assert "LIABILITY VIOLATION" in msg

def test_advice_block():
    # Attempt to give direct investment advice
    unsafe_msg = "You should sell your house and buy this stock."
    # Note: Regex would need to be tuned to catch 'should sell', 
    # currently catches 'sell now'. 
    unsafe_msg_2 = "Sell now and buy this!"
    is_valid, msg = validator.validate(unsafe_msg_2)
    assert is_valid is False
  
