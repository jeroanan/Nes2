from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestNopOpCode(OpCodeTestBase):

    def test_nop_implied_command_calls_nop_method(self):
        self.assert_opcode_execution(OpCodes.nop_implied_command, self.target.get_nop_command_executed)
