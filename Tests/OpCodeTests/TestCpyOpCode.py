from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestCpyOpCode(OpCodeTestBase):

    def test_cpy_immediate_command_calls_cpy_method(self):
        self.assert_opcode_execution(OpCodes.cpy_immediate_command, self.target.get_cpy_command_executed)

    def test_cpy_zero_page_command_calls_cpy_method(self):
        self.assert_opcode_execution(OpCodes.cpy_zero_page_command, self.target.get_cpy_command_executed)

    def test_cpy_absolute_command_calls_cpy_method(self):
        self.assert_opcode_execution(OpCodes.cpy_absolute_command, self.target.get_cpy_command_executed)


