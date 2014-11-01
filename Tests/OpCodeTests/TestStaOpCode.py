from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestStaOpCode(OpCodeTestBase):

    def test_sta_indirect_x_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sta_indirect_x_command, self.target.get_sta_command_executed)

    def test_sta_zero_page_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sta_zero_page_command, self.target.get_sta_command_executed)

    def test_sta_absolute_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sta_absolute_command, self.target.get_sta_command_executed)

    def test_sta_indirect_y_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sta_indirect_y_command, self.target.get_sta_command_executed)

    def test_sta_zero_page_x_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sta_zero_page_x_command, self.target.get_sta_command_executed)

    def test_sta_absolute_y_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sta_absolute_y_command, self.target.get_sta_command_executed)

    def test_sta_absolute_x_command_calls_sta_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.sta_absolute_x_command, self.target.get_sta_command_executed)

