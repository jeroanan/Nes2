from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestAdcOpCode(OpCodeTestBase):
    def test_adc_indirect_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_indirect_x_command, self.target.get_adc_command_executed)

    def test_adc_zero_page_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_zero_page_command, self.target.get_adc_command_executed)

    def test_adc_absolute_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_absolute_command, self.target.get_adc_command_executed)

    def test_adc_immediate_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_immediate_command, self.target.get_adc_command_executed)

    def test_adc_absolute_y_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_absolute_y_command, self.target.get_adc_command_executed)

    def test_adc_absolute_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_absolute_x_command, self.target.get_adc_command_executed)

    def test_adc_indirect_y_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_indirect_y_command, self.target.get_adc_command_executed)

    def test_adc_zero_page_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_zero_page_x_command, self.target.get_adc_command_executed)