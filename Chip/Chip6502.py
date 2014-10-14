from Chip import OpCodes


class Chip6502(object):
    def execute(self, command):
        if command == OpCodes.brk_command:
            self.brk_command()
        elif self.is_ora_command(command):
            self.ora_command()
        elif self.is_asl_command(command):
            self.asl_command()
        elif command == OpCodes.php_implied_command:
            self.php_command()
        elif command == OpCodes.bpl_relative_command:
            self.bpl_command()
        elif command == OpCodes.clc_implied_command:
            self.clc_command()
        elif command == OpCodes.jsr_absolute_command:
            self.jsr_command()
        elif self.is_and_command(command):
            self.and_command()
        elif self.is_bit_command(command):
            self.bit_command()
        elif self.is_rol_command(command):
            self.rol_command()
        elif command == OpCodes.plp_implied_command:
            self.plp_command()
        elif command == OpCodes.bmi_relative_command:
            self.bmi_command()

    def brk_command(self):
        pass

    def is_ora_command(self, op_code):
        return op_code == OpCodes.ora_indirect_x_command or op_code == OpCodes.ora_zero_page_command or \
               op_code == OpCodes.ora_immediate_command or op_code == OpCodes.ora_absolute_command or \
               op_code == OpCodes.ora_indirect_y_command or op_code == OpCodes.ora_zero_page_x_command or \
               op_code == OpCodes.ora_absolute_y_command or op_code == OpCodes.ora_absolute_x_command

    def ora_command(self):
        pass

    def is_asl_command(self, command):
        return command == OpCodes.asl_zero_page_command or command == OpCodes.asl_accumulator_command or \
               command == OpCodes.asl_absolute_command or command == OpCodes.asl_zero_page_x_command or \
               command == OpCodes.asl_absolute_x_command

    def asl_command(self):
        pass

    def php_command(self):
        pass

    def bpl_command(self):
        pass

    def clc_command(self):
        pass

    def jsr_command(self):
        pass

    def is_and_command(self, command):
        return command == OpCodes.and_indirect_x_command or command == OpCodes.and_zero_page_command or \
               command == OpCodes.and_immediate_command or command == OpCodes.and_absolute_command

    def and_command(self):
        pass

    def is_bit_command(self, command):
        return command == OpCodes.bit_zero_page_command or command == OpCodes.bit_absolute_command

    def bit_command(self):
        pass

    def is_rol_command(self, command):
        return command == OpCodes.rol_zero_page_command or command == OpCodes.rol_accumulator_command or \
               command == OpCodes.rol_absolute_command

    def rol_command(self):
        pass

    def plp_command(self):
        pass

    def bmi_command(self):
        pass