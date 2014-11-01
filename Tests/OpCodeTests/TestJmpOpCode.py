from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestJmpOpCode(OpCodeTestBase):
    def test_jmp_indirect_command_calls_jmp_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.jmp_indirect_command, self.target.get_jmp_command_executed)
