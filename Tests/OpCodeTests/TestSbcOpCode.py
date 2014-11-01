from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestSbcOpCode(OpCodeTestBase):
    def test_sbc_indirect_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_indirect_x_command, self.target.get_sbc_command_executed)

    def test_sbc_zero_page_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_zero_page_command, self.target.get_sbc_command_executed)

    def test_sbc_immediate_command_performs_subtraction(self):
        self.__two_minus_one()
        self.assertEqual(0x1, self.target.get_accumulator())

    def test_sbc_immediate_command_sets_carry_flag_when_there_is_a_borrow(self):
        self.__one_minus_two()
        self.assert_carry_flag_set()

    def test_sbc_immediate_command_clears_carry_flag_when_there_is_no_borrow(self):
        self.__one_minus_two()
        self.__two_minus_one()
        self.assert_carry_flag_clear()

    def __two_minus_one(self):
        self.__subtract_two_numbers(0x02, 0x01)

    def test_sbc_immediate_command_sets_overflow_flag_when_sign_bit_changes_minus_to_positive(self):
        self.__subtract_two_numbers(-127, 1)
        self.assert_overflow_flag_set()

    def test_sbc_immediate_command_does_not_set_overflow_flag_when_sign_bit_does_not_change(self):
        self.__one_minus_two()
        self.assert_overflow_flag_clear()

    def test_sbc_immediate_command_clears_overflow_flag_when_sign_bit_does_not_change(self):
        self.__subtract_two_numbers(-127, 1)
        self.__one_minus_two()
        self.assert_overflow_flag_clear()

    def __one_minus_two(self):
        self.__subtract_two_numbers(0x1, 0x2)

    def test_sbc_immediate_command_sets_overflow_flag_when_sign_bit_changes_positive_to_minus(self):
        self.__subtract_two_numbers(127, -1)
        self.assert_overflow_flag_set()

    def test_sbc_immediate_command_sets_zero_flag_when_result_is_zero(self):
        self.__subtract_two_numbers(0x1, 0x1)
        self.assert_zero_flag_set()

    def __subtract_two_numbers(self, x, y):
        self.target.set_accumulator(x)
        self.target.execute(OpCodes.sbc_immediate_command, y)

    def test_sbc_absolute_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_absolute_command, self.target.get_sbc_command_executed)

    def test_sbc_indirect_y_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_indirect_y_command, self.target.get_sbc_command_executed)

    def test_sbc_zero_page_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_zero_page_x_command, self.target.get_sbc_command_executed)

    def test_sbc_absolute_y_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_absolute_y_command, self.target.get_sbc_command_executed)

    def test_sbc_absolute_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodes.sbc_absolute_x_command, self.target.get_sbc_command_executed)
