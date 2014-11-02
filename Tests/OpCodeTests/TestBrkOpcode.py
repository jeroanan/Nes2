from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBrkOpCode(OpCodeTestBase):

    def test_brk_command_calls_brk_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.brk_command, self.target.get_brk_command_executed)