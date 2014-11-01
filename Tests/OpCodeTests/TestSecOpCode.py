from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestSecOpCode(OpCodeTestBase):
    def test_execute_sec_implied_command_calls_sec_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sec_implied_command, self.target.get_sec_command_executed)
