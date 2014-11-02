from Chip import OpCodeDefinitions
from Chip.OpCodes.OraCommand import OraCommand
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestOraOpCode(OpCodeTestBase):

    def test_ora_command_does_or_correctly(self):
        self.target.set_accumulator(0x13)
        self.target.execute(OpCodeDefinitions.ora_immediate_command, 0x37)
        self.assertEqual(0x13 | 0x37, self.target.get_accumulator())

    def test_call_matches(self):
        OraCommand.matches(OpCodeDefinitions.ora_immediate_command)

    def test_matches_ora_indirect_x_command(self):
        match = OraCommand.matches(OpCodeDefinitions.ora_indirect_x_command)
        self.assertTrue(match)

    def test_matches_ora_zero_page_command(self):
        match = OraCommand.matches(OpCodeDefinitions.ora_zero_page_command)
        self.assertTrue(match)



