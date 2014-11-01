from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestCmpOpCode(OpCodeTestBase):
    def test_cmp_indirect_x_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.cmp_indirect_x_command, self.target.get_cmp_command_executed)

    def test_cmp_zero_page_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.cmp_zero_page_command, self.target.get_cmp_command_executed)

    def test_cmp_immediate_command_sets_zero_flag_when_comparison_is_equal(self):
        self.target.set_accumulator(0x13)
        self.target.execute(OpCodeDefinitions.cmp_immediate_command, 0x13)
        self.assertEqual(0x1, self.target.get_zero_flag())

    def test_cmp_immediate_command_sets_carry_flag_when_accumulator_greater_than_operand(self):
        self.target.set_accumulator(0x37)
        self.target.execute(OpCodeDefinitions.cmp_immediate_command, 0x13)
        self.assertEqual(0x1, self.target.get_carry_flag())

    def test_cmp_immediate_command_sets_negative_flag_when_accumulator_less_than_operand(self):
        self.target.set_accumulator(0x13)
        self.target.execute(OpCodeDefinitions.cmp_immediate_command, 0x37)
        self.assertEqual(0x1, self.target.get_negative_flag())

    def test_cmp_immediate_command_does_not_set_negative_flag_when_accumulator_not_less_than_operand(self):
        self.target.set_accumulator(0x1)
        self.target.execute(OpCodeDefinitions.cmp_immediate_command, 0x0)
        self.assertEqual(0x0, self.target.get_negative_flag())

    def test_cmp_absolute_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.cmp_absolute_command, self.target.get_cmp_command_executed)

    def test_cmp_indirect_y_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.cmp_indirect_y_command, self.target.get_cmp_command_executed)

    def test_cmp_zero_page_x_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.cmp_zero_page_x_command, self.target.get_cmp_command_executed)

    def test_cmp_absolute_y_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.cmp_absolute_y_command, self.target.get_cmp_command_executed)

    def test_cmp_absolute_x_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.cmp_absolute_x_command, self.target.get_cmp_command_executed)

