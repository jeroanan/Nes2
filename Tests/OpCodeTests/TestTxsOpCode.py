from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestTxsOpCode(OpCodeTestBase):
    def test_txs_implied_command_calls_txs_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.txs_implied_command, self.target.get_txs_command_executed)
