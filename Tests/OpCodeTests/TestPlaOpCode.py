from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestPlaOpcode(OpCodeTestBase):

    def test_pla_implied_command_calls_pla_method(self):
        self.assert_opcode_execution(OpCodes.pla_implied_command, self.target.get_pla_command_executed)


