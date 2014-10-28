from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestClcOpCode(OpCodeTestBase):
    def test_execute_clc_implied_command_calls_clc_method(self):
        self.assert_opcode_execution(OpCodes.clc_implied_command, self.target.get_clc_command_executed)

