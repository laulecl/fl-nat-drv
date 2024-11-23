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
import plugins
import channels
import ui


#PORT_MIDICC_ANALOGLAB = 10


# test de plugin...
class Plugin(Abstract.Plugin):

    def name(self) -> str:
        return "PoiZone"


    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        # ne fonctionne pas
        if modes & Consts.JOG_DEFAULT:
           if step == 1:
              paramIndex = 22

              value = plugins.getParamValue(paramIndex, channels.selectedChannel())
              plugins.setParamValue(value + 1, paramIndex, channels.selectedChannel())
              print("coucou")
           else:
                plugins.nextPreset(channels.selectedChannel(), False)

        else:
            return False

        return True



    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        return True
