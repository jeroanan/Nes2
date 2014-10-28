from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestLdaOpCode(OpCodeTestBase):

    def test_lda_indirect_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_indirect_x_command, self.target.get_lda_command_executed)

    def test_lda_zero_page_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_zero_page_command, self.target.get_lda_command_executed)

    def test_lda_immediate_command_calls_lda_method(self):
        self.assert_opcode_execution(OpCodes.lda_immediate_command, self.target.get_lda_command_executed)

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





