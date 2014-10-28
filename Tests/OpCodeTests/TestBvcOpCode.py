from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBvcOpCode(OpCodeTestBase):
    def test_bvc_relative_command_calls_bvc_method(self):
        self.assert_opcode_execution(OpCodes.bvc_relative_command, self.target.get_bvc_command_executed)
