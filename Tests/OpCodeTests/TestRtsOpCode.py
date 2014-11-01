from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestRtsOpcode(OpCodeTestBase):

    def test_rts_implied_command_calls_rts_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.rts_implied_command, self.target.get_rts_command_executed)
