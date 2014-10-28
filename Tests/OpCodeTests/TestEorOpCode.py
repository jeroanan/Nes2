from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestEorOpCode(OpCodeTestBase):

    def test_eor_indirect_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_indirect_x_command, self.target.get_eor_command_executed)

    def test_eor_zero_page_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_zero_page_command, self.target.get_eor_command_executed)

    def test_eor_immediate_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_immediate_command, self.target.get_eor_command_executed)

    def test_eor_absolute_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_absolute_command, self.target.get_eor_command_executed)

    def test_eor_indirect_y_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_indirect_y_command, self.target.get_eor_command_executed)

    def test_eor_zero_page_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_zero_page_x_command, self.target.get_eor_command_executed)

    def test_eor_absolute_y_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_absolute_y_command, self.target.get_eor_command_executed)

    def test_eor_absolute_x_command_calls_eor_method(self):
        self.assert_opcode_execution(OpCodes.eor_absolute_x_command, self.target.get_eor_command_executed)