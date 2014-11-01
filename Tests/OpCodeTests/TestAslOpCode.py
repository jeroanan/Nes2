from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestAslOpCode(OpCodeTestBase):

    def test_execute_asl_zero_page_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.asl_zero_page_command, self.target.get_asl_command_executed)

    def test_execute_asl_accumulator_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.asl_accumulator_command, self.target.get_asl_command_executed)

    def test_execute_asl_absolute_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.asl_absolute_command, self.target.get_asl_command_executed)

    def test_execute_asl_zero_page_x_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.asl_zero_page_x_command, self.target.get_asl_command_executed)

    def test_execute_asl_absolute_x_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.asl_absolute_x_command, self.target.get_asl_command_executed)
