from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBeqOpCode(OpCodeTestBase):
    def test_beq_relative_command_calls_beq_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.beq_relative_command, self.target.get_beq_command_executed)
