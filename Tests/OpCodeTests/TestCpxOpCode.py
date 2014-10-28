from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestCpxOpCode(OpCodeTestBase):
        def test_cpx_immediate_command_calls_cpx_method(self):
            self.assert_opcode_execution(OpCodes.cpx_immediate_command, self.target.get_cpx_command_executed)

        def test_cpx_zero_page_command_calls_cpx_method(self):
            self.assert_opcode_execution(OpCodes.cpx_zero_page_command, self.target.get_cpx_command_executed)

        def test_cpx_absolute_command_calls_cpx_method(self):
            self.assert_opcode_execution(OpCodes.cpx_absolute_command, self.target.get_cpx_command_executed)
