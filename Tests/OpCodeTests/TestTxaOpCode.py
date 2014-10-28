from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestTxaOpCode(OpCodeTestBase):
    def test_txa_implied_command_calls_txa_method(self):
        self.assert_opcode_execution(OpCodes.txa_implied_command, self.target.get_txa_command_executed)
