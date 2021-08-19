from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Rover(object):
    def execute(self, command):
        return "0:0:N"