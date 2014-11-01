from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBmiOpCode(OpCodeTestBase):
    def test_execute_bmi_relative_command_calls_bmi_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.bmi_relative_command, self.target.get_bmi_command_executed)
