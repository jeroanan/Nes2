from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestOraOpCode(OpCodeTestBase):
    def test_execute_ora_indirect_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_indirect_x_command, self.target.get_ora_command_executed)

    def test_execute_ora_zero_page_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_zero_page_command, self.target.get_ora_command_executed)

    def test_execute_ora_immediate_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_immediate_command, self.target.get_ora_command_executed)

    def test_execute_ora_absolute_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_absolute_command, self.target.get_ora_command_executed)

    def test_execute_ora_indirect_y_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_indirect_y_command, self.target.get_ora_command_executed)

    def test_execute_ora_zero_page_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_zero_page_x_command, self.target.get_ora_command_executed)

    def test_execute_ora_absolute_y_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_absolute_y_command, self.target.get_ora_command_executed)

    def test_execute_ora_absolute_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_absolute_x_command, self.target.get_ora_command_executed)


