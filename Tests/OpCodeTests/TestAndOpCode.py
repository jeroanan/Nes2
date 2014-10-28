from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestAndOpCode(OpCodeTestBase):

    def test_execute_and_indirect_x_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_indirect_x_command, self.target.get_and_command_executed)

    def test_execute_and_zero_page_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_zero_page_command, self.target.get_and_command_executed)

    def test_execute_and_immediate_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_immediate_command, self.target.get_and_command_executed)

    def test_execute_and_absolute_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_absolute_command, self.target.get_and_command_executed)

    def test_execute_and_indirect_y_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_indirect_y_command, self.target.get_and_command_executed)

    def test_execute_and_zero_page_x__command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_zero_page_x_command, self.target.get_and_command_executed)

    def test_execute_and_absolute_y_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_absolute_y_command, self.target.get_and_command_executed)

    def test_execute_and_absolute_x_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_absolute_x_command, self.target.get_and_command_executed)


