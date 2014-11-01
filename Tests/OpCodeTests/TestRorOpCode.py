from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestRorOpCode(OpCodeTestBase):
    def test_ror_zero_page_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ror_zero_page_command, self.target.get_ror_command_executed)

    def test_ror_accumulator_command_calls_ror_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ror_accumulator_command, self.target.get_ror_command_executed)

    def test_ror_absolute_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ror_absolute_command, self.target.get_ror_command_executed)

    def test_ror_zero_page_x_command_calls_ror_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ror_zero_page_x_command, self.target.get_ror_command_executed)

    def test_ror_absolute_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.ror_absolute_x_command, self.target.get_ror_command_executed)

