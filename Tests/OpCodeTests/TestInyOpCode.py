from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestInyOpCode(OpCodeTestBase):
    def test_iny_implied_command_calls_iny_method(self):
        self.assert_opcode_execution(OpCodes.iny_implied_command, self.target.get_iny_command_executed)
