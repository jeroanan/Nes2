from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestJsrOpCode(OpCodeTestBase):

    def test_execute_jsr_absolute_command_calls_jsr_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.jsr_absolute_command, self.target.get_jsr_command_executed)
