from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestSecOpCode(OpCodeTestBase):
    def test_execute_sec_implied_command_calls_sec_method(self):
        self.assert_opcode_execution(OpCodes.sec_implied_command, self.target.get_sec_command_executed)
