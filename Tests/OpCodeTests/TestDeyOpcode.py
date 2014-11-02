from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestDeyOpCode(OpCodeTestBase):
    def test_dey_implied_command_calls_dey_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.dey_implied_command, self.target.get_dey_command_executed)
