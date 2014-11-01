from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestNopOpCode(OpCodeTestBase):

    def test_nop_implied_command_calls_nop_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.nop_implied_command, self.target.get_nop_command_executed)
