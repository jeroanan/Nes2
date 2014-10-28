from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestClvOpCode(OpCodeTestBase):
    def test_clv_implied_command_calls_clv_method(self):
        self.assert_opcode_execution(OpCodes.clv_implied_command, self.target.get_clv_command_executed)
