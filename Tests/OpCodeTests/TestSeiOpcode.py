from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestSeiOpCode(OpCodeTestBase):
    def test_sei_implied_command_calls_sei_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sei_implied_command, self.target.get_sei_command_executed)
