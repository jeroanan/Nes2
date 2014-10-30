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

    def __one_plus_one(self):
        self.target.set_accumulator(0x01)
        self.target.execute(OpCodes.adc_immediate_command, 0x01)

    def test_adc_immediate_command_performs_add(self):
        self.__one_plus_one()

        expected_value = 0x01 + 0x01
        actual_value = self.target.get_accumulator()

        self.assertEqual(expected_value, actual_value)

    def test_adc_immediate_command_sets_carry_flag_when_there_is_a_carry(self):
        self.target.set_accumulator(0xFF)
        self.target.execute(OpCodes.adc_immediate_command, 0x01)

        expected_value = 0x1
        actual_value = self.target.get_carry_flag()

        self.assertEqual(expected_value, actual_value)

    def test_adc_immediate_command_clears_carry_flag_when_there_is_no_carry(self):
        self.target.set_carry_flag()
        self.__one_plus_one()

        expected_value = 0x0
        actual_value = self.target.get_carry_flag()

        self.assertEqual(expected_value, actual_value)

    def test_adc_immediate_command_does_not_set_overflow_flag_when_sign_bit_changes(self):
        self.__one_plus_one()

        expected_value = 0x0
        actual_value = self.target.get_overflow_flag()

        self.assertEqual(expected_value, actual_value)

    def test_adc_immediate_command_sets_overflow_flag_when_sign_bit_changes(self):
        self.target.set_accumulator(127)
        self.target.execute(OpCodes.adc_immediate_command, 0x01)

        expected_value = 0x01
        actual_value = self.target.get_overflow_flag()

        self.assertEqual(expected_value, actual_value)

    def test_adc_immediate_command_sets_zero_flag_when_result_is_zero(self):
        self.target.set_accumulator(-1)
        self.target.execute(OpCodes.adc_immediate_command, 0x01)

        expected_value = 0x1
        actual_value = self.target.get_zero_flag()

        self.assertEqual(expected_value, actual_value)

    def test_adc_immediate_command_clears_zero_flag_when_result_is_nonzero(self):
        self.target.set_accumulator(-1)
        self.target.execute(OpCodes.adc_immediate_command, 0x1)
        self.target.execute(OpCodes.adc_immediate_command, 0x1)

        self.assertEqual(0x0, self.target.get_zero_flag())

    def test_adc_absolute_y_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_absolute_y_command, self.target.get_adc_command_executed)

    def test_adc_absolute_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_absolute_x_command, self.target.get_adc_command_executed)

    def test_adc_indirect_y_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_indirect_y_command, self.target.get_adc_command_executed)

    def test_adc_zero_page_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodes.adc_zero_page_x_command, self.target.get_adc_command_executed)