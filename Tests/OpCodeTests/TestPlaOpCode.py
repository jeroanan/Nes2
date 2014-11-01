from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestPlaOpcode(OpCodeTestBase):

    def test_pla_implied_command_calls_pla_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.pla_implied_command, self.target.get_pla_command_executed)


