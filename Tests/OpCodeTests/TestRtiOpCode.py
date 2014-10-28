from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestRtiOpCode(OpCodeTestBase):
    def test_execute_rti_implied_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.rti_implied_command, self.target.get_rti_command_executed)
