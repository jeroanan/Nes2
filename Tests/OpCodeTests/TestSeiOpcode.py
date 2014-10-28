from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestSeiOpCode(OpCodeTestBase):
    def test_sei_implied_command_calls_sei_method(self):
        self.assert_opcode_execution(OpCodes.sei_implied_command, self.target.get_sei_command_executed)
