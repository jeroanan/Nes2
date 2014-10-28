from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestPlpOpCode(OpCodeTestBase):
    def test_execute_plp_implied_command_calls_plp_method(self):
        self.assert_opcode_execution(OpCodes.plp_implied_command, self.target.get_plp_command_executed)
