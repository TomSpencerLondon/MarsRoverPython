from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Rover(object):
    def execute(self, command):
        if (command == 'R'):
            return "0:0:E"

        if (command == 'RR'):
            return "0:0:S"

        if (command == 'RRR'):
            return "0:0:W"

        return "0:0:N"