from Chip import OpCodeDefinitions
from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestAdcOpCode(OpCodeTestBase):

    def setUp(self):
        super().setUp()
        self.___adc_indirect_x_command = OpCodeDefinitions.adc_indirect_x_command
        self.__adc_zero_page_command = OpCodeDefinitions.adc_zero_page_command
        self.__adc_absolute_command = OpCodeDefinitions.adc_absolute_command

    def test_adc_indirect_x_command_calls_adc_method(self):
        self.assert_opcode_execution(self.___adc_indirect_x_command, self.target.get_adc_command_executed)

    def test_adc_zero_page_command_calls_adc_method(self):
        self.assert_opcode_execution(self.__adc_zero_page_command, self.target.get_adc_command_executed)

    def test_adc_absolute_command_calls_adc_method(self):
        self.assert_opcode_execution(self.__adc_absolute_command, self.target.get_adc_command_executed)

    def test_adc_immediate_command_performs_add(self):
        self.__one_plus_one()
        self.assertEqual(0x2, self.target.get_accumulator())

    def test_adc_immediate_command_sets_carry_flag_when_there_is_a_carry(self):
        self.__add_two_numbers(0xFF, 0x01)
        self.assert_carry_flag_set()

    def test_adc_immediate_command_clears_carry_flag_when_there_is_no_carry(self):
        self.target.set_carry_flag()
        self.__one_plus_one()
        self.assert_carry_flag_clear()

    def test_adc_immediate_command_does_not_set_overflow_flag_when_sign_bit_does_not_change(self):
        self.__one_plus_one()
        self.assert_overflow_flag_clear()

    def __one_plus_one(self):
        self.__add_two_numbers(0x1, 0x1)

    def test_adc_immediate_command_sets_overflow_flag_when_sign_bit_changes_positive_to_negative(self):
        self.__add_two_numbers(127, 0x1)
        self.assert_overflow_flag_set()

    def test_adc_immediate_command_set_overflow_flag_when_sign_bit_changes_negative_to_positive(self):
        self.__add_two_numbers(-127, -1)
        self.assert_overflow_flag_set()

    def test_adc_immediate_command_sets_zero_flag_when_result_is_zero(self):
        self.__add_two_numbers(-1, 0x1)
        self.assert_zero_flag_set()

    def test_adc_immediate_command_clears_zero_flag_when_result_is_nonzero(self):
        self.__add_two_numbers(-1, 0x1)
        self.__add_two_numbers(0x0, 0x1)
        self.assert_zero_flag_clear()

    def __add_two_numbers(self, x, y):
        self.target.set_accumulator(x)
        self.target.execute(OpCodeDefinitions.adc_immediate_command, y)

    def test_adc_absolute_y_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.adc_absolute_y_command, self.target.get_adc_command_executed)

    def test_adc_absolute_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.adc_absolute_x_command, self.target.get_adc_command_executed)

    def test_adc_indirect_y_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.adc_indirect_y_command, self.target.get_adc_command_executed)

    def test_adc_zero_page_x_command_calls_adc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.adc_zero_page_x_command, self.target.get_adc_command_executed)