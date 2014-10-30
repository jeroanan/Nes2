from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestLdxOpCode(OpCodeTestBase):

    def test_ldx_immediate_command_loads_x_register(self):
        self.target.execute(OpCodes.ldx_immediate_command, 0x13)
        self.assertEqual(0x13, self.target.get_x_register())

    def test_ldx_immediate_command_sets_zero_flag_when_result_is_zero(self):
        self.target.execute(OpCodes.ldx_immediate_command, 0x00)
        self.assertEqual(0x01, self.target.get_zero_flag())

    def test_ldx_immediate_command_sets_negative_flag_when_sign_bit_set(self):
        self.target.execute(OpCodes.ldx_immediate_command, 0xFF)
        self.assertEqual(0x01, self.target.get_negative_flag())

    def test_ldx_zero_page_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_zero_page_command, self.target.get_ldx_command_executed)

    def test_ldx_absolute_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_absolute_command, self.target.get_ldx_command_executed)

    def test_ldx_zero_page_y_command_calls_ldx_method(self):
        self.assert_opcode_execution(OpCodes.ldx_zero_page_y_command, self.target.get_ldx_command_executed)

    def test_ldx_absolute_y_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.ldx_absolute_y_command, self.target.get_ldx_command_executed)




