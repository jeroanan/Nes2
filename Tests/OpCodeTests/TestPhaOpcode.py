from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestPhaOpCode(OpCodeTestBase):
    def test_pha_implied_command_calls_pha_method(self):
        self.assert_opcode_execution(OpCodes.pha_implied_command, self.target.get_pha_command_executed)
