from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestLdyOpCode(OpCodeTestBase):

    def test_ldy_immediate_command_loads_y_register(self):
        self.target.execute(OpCodes.ldy_immediate_command, 0x13)
        self.assertEqual(0x13, self.target.get_y_register())

    def test_ldy_immediate_command_sets_z_flag_when_result_zero(self):
        self.target.execute(OpCodes.ldy_immediate_command, 0x0)
        self.assertEqual(0x1, self.target.get_zero_flag())

    def test_ldy_immediate_command_does_not_set_z_flag_when_result_nonzero(self):
        self.target.execute(OpCodes.ldy_immediate_command, 0x13)
        self.assertEqual(0x0, self.target.get_zero_flag())

    def test_ldy_immediate_command_clears_z_flag_when_result_nonzero(self):
        self.target.execute(OpCodes.ldy_immediate_command, 0x0)
        self.target.execute(OpCodes.ldy_immediate_command, 0x13)
        self.assertEqual(0x0, self.target.get_zero_flag())

    def test_ldy_immediate_command_sets_negative_flag_when_result_negative(self):
        self.target.execute(OpCodes.ldy_immediate_command, 0xFF)
        self.assertEqual(0x1, self.target.get_negative_flag())

    def test_ldy_immediate_command_clears_negative_flag_when_result_nonnegative(self):
        self.target.execute(OpCodes.ldy_immediate_command, 0xFF)
        self.target.execute(OpCodes.ldy_immediate_command, 0x01)
        self.assertEqual(0x0, self.target.get_negative_flag())

    def test_ldy_zero_page_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_zero_page_command, self.target.get_ldy_command_executed)

    def test_ldy_absolute_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_absolute_command, self.target.get_ldy_command_executed)

    def test_ldy_zero_page_x_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_zero_page_x_command, self.target.get_ldy_command_executed)

    def test_ldy_absolute_x_command_calls_ldy_method(self):
        self.assert_opcode_execution(OpCodes.ldy_absolute_x_command, self.target.get_ldy_command_executed)



