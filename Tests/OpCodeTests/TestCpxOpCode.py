from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestCpxOpCode(OpCodeTestBase):

        def test_cpx_immediate_command_sets_zero_flag_when_comparison_is_equal(self):
            self.__compare_like_values()
            self.assertEqual(0x01, self.target.get_zero_flag())

        def test_cpx_immediate_command_sets_carry_flag_when_x_register_greater_than_operand(self):
            self.target.set_x_register(0x1)
            self.target.execute(OpCodeDefinitions.cpx_immediate_command, 0x0)
            self.assertEqual(0x01, self.target.get_carry_flag())

        def test_cpx_immediate_command_does_not_set_carry_flag_when_x_register_not_greater_than_operand(self):
            self.__compare_like_values()
            self.assertEqual(0x0, self.target.get_carry_flag())

        def test_cpx_immediate_command_sets_negative_flag_when_x_register_less_than_operand(self):
            self.target.set_x_register(0x0)
            self.target.execute(OpCodeDefinitions.cpx_immediate_command, 0x01)
            self.assertEqual(0x01, self.target.get_negative_flag())

        def test_cpx_immediate_command_does_not_set_negative_flag_when_x_register_not_less_than_operand(self):
            self.__compare_like_values()
            self.assertEqual(0x00, self.target.get_negative_flag())

        def __compare_like_values(self):
            self.target.set_x_register(0x13)
            self.target.execute(OpCodeDefinitions.cpx_immediate_command, 0x13)

        def test_cpx_zero_page_command_calls_cpx_method(self):
            self.assert_opcode_execution(OpCodeDefinitions.cpx_zero_page_command, self.target.get_cpx_command_executed)

        def test_cpx_absolute_command_calls_cpx_method(self):
            self.assert_opcode_execution(OpCodeDefinitions.cpx_absolute_command, self.target.get_cpx_command_executed)
