from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestLdaOpCode(OpCodeTestBase):

    def test_lda_indirect_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_indirect_x_command, self.target.get_lda_command_executed)

    def test_lda_zero_page_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_zero_page_command, self.target.get_lda_command_executed)

    def test_lda_immediate_command_loads_accumulator(self):
        self.target.execute(OpCodes.lda_immediate_command, 0x13)
        self.assertEqual(0x13, self.target.get_accumulator())

    def test_lda_immediate_command_sets_zero_flag_when_result_is_zero(self):
        self.target.execute(OpCodes.lda_immediate_command, 0x00)
        self.assertEqual(0x01, self.target.get_zero_flag())

    def test_lda_immediate_command_sets_negative_flag_when_sign_bit_is_set(self):
        self.target.execute(OpCodes.lda_immediate_command, 0xFF)
        self.assertEqual(0x01, self.target.get_negative_flag())

    def test_lda_immediate_command_clears_negative_flag_when_sign_bit_is_not_set(self):
        self.target.execute(OpCodes.lda_immediate_command, 0xFF)
        self.target.execute(OpCodes.lda_immediate_command, 0x01)
        self.assertEqual(0x00, self.target.get_negative_flag())

    def test_lda_absolute_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_absolute_command, self.target.get_lda_command_executed)

    def test_lda_indirect_y_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_indirect_y_command, self.target.get_lda_command_executed)

    def test_lda_zero_page_x_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_zero_page_x_command, self.target.get_lda_command_executed)

    def test_lda_absolute_y_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_absolute_y_command, self.target.get_lda_command_executed)

    def test_lda_absolute_x_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_absolute_x_command, self.target.get_lda_command_executed)





