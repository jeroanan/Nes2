from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestTayOpCode(OpCodeTestBase):
    def test_tay_implied_command_calls_tay_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.tay_implied_command, self.target.get_tay_command_executed)
