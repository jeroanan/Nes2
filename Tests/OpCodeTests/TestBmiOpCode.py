from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBmiOpCode(OpCodeTestBase):
    def test_execute_bmi_relative_command_calls_bmi_method(self):
        self.assert_opcode_execution(OpCodes.bmi_relative_command, self.target.get_bmi_command_executed)
