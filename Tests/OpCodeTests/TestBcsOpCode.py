from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBcsOpCode(OpCodeTestBase):
    def test_bcs_relative_command_calls_bcs_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.bcs_relative_command, self.target.get_bcs_command_executed)
