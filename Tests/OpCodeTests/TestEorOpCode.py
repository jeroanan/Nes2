from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestEorOpCode(OpCodeTestBase):

    def test_eor_indirect_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.eor_indirect_x_command, self.target.get_eor_command_executed)

    def test_eor_zero_page_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.eor_zero_page_command, self.target.get_eor_command_executed)

    def test_eor_immediate_command_does_exclusive_or(self):
        self.target.set_accumulator(0x13)
        self.target.execute(OpCodeDefinitions.eor_immediate_command, 0x37)

        expected_value = 0x13 ^ 0x37
        actual_value = self.target.get_accumulator()

        self.assertEqual(expected_value, actual_value)

    def test_eor_absolute_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.eor_absolute_command, self.target.get_eor_command_executed)

    def test_eor_indirect_y_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.eor_indirect_y_command, self.target.get_eor_command_executed)

    def test_eor_zero_page_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.eor_zero_page_x_command, self.target.get_eor_command_executed)

    def test_eor_absolute_y_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.eor_absolute_y_command, self.target.get_eor_command_executed)

    def test_eor_absolute_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.eor_absolute_x_command, self.target.get_eor_command_executed)