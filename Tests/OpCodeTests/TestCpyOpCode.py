from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestCpyOpCode(OpCodeTestBase):

    def test_cpy_immediate_command_sets_zero_flag_when_comparison_is_equal(self):
        self.target.execute(OpCodes.cpy_immediate_command, 0x0)
        self.assertEqual(0x01, self.target.get_zero_flag())

    def test_cpy_immediate_command_does_not_set_zero_flag_when_comparison_is_unequal(self):
        self.target.execute(OpCodes.cpy_immediate_command, 0x1)
        self.assertEqual(0x00, self.target.get_zero_flag())

    def test_cpy_immediate_command_sets_carry_flag_when_y_register_greater_than_operand(self):
        self.target.set_y_register(0x1)
        self.target.execute(OpCodes.cpy_immediate_command, 0x0)
        self.assertEqual(0x01, self.target.get_carry_flag())

    def test_cpy_immediate_command_sets_negative_flag_when_register_less_than_operand(self):
        self.target.execute(OpCodes.cpy_immediate_command, 0x1)
        self.assertEqual(0x1, self.target.get_negative_flag())

    def test_cpy_zero_page_command_calls_cpy_method(self):
        self.assert_opcode_execution(OpCodes.cpy_zero_page_command, self.target.get_cpy_command_executed)

    def test_cpy_absolute_command_calls_cpy_method(self):
        self.assert_opcode_execution(OpCodes.cpy_absolute_command, self.target.get_cpy_command_executed)


