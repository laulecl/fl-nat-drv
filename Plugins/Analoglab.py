"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

import Abstract
import Consts
import transport
import midi
import device


#PORT_MIDICC_ANALOGLAB = 10


# test de plugin...
class Plugin(Abstract.Plugin):

    def name(self) -> str:
        return "Analog Lab V"


    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        if modes & Consts.JOG_DEFAULT:
           if step == 1:
                # 	Specify message as: message = status + (data1 << 8) + (data2 << 16) + (port << 24)
                #device.forwardMIDICC(16 + (data1 << 8) + (data2 << 16) + (midiPort << 24))
                transport.globalTransport(midi.FPT_Down, 1)
                #transport.globalTransport(midi.FPT_Enter, 1)
           else:
                transport.globalTransport(midi.FPT_Up, 1)
                #transport.globalTransport(midi.FPT_Enter, 1)

        else:
            return False

        return True



    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        return True
