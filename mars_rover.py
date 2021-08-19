from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Rover(object):
    def execute(self, command):
        if (command == 'R'):
            return "0:0:E"
        return "0:0:N"