from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestInxOpCode(OpCodeTestBase):

    def test_inx_implied_command_calls_inx_method(self):
        self.assert_opcode_execution(OpCodes.inx_implied_command, self.target.get_inx_command_executed)
