from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBccOpCode(OpCodeTestBase):
    def test_bcc_relative_command_calls_bcc_method(self):
        self.assert_opcode_execution(OpCodes.bcc_relative_command, self.target.get_bcc_command_executed)
