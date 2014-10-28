from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestCmpOpCode(OpCodeTestBase):
    def test_cmp_indirect_x_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_indirect_x_command, self.target.get_cmp_command_executed)

    def test_cmp_zero_page_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_zero_page_command, self.target.get_cmp_command_executed)

    def test_cmp_immediate_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_immediate_command, self.target.get_cmp_command_executed)

    def test_cmp_absolute_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_absolute_command, self.target.get_cmp_command_executed)

    def test_cmp_indirect_y_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_indirect_y_command, self.target.get_cmp_command_executed)

    def test_cmp_zero_page_x_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_zero_page_x_command, self.target.get_cmp_command_executed)

    def test_cmp_absolute_y_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_absolute_y_command, self.target.get_cmp_command_executed)

    def test_cmp_absolute_x_command_calls_cmp_method(self):
        self.assert_opcode_execution(OpCodes.cmp_absolute_x_command, self.target.get_cmp_command_executed)

