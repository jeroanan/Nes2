from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestIncOpCode(OpCodeTestBase):

    def test_inc_absolute_command_calls_inc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.inc_absolute_command, self.target.get_inc_command_executed)

    def test_inc_zero_page_x_command_calls_inc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.inc_zero_page_x_command, self.target.get_inc_command_executed)

    def test_inc_absolute_x_command_calls_sbc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.inc_absolute_x_command, self.target.get_inc_command_executed)

    def test_inc_zero_page_command_calls_inc_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.inc_zero_page_command, self.target.get_inc_command_executed)

