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
import ui


# test de plugin...
class Plugin(Abstract.Plugin):

    def name(self) -> str:
        return "PoiZone"



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        pass
        # ne fonctionne pas
        if modes & Consts.JOG_DEFAULT:
            if step == 1:
                ui.previous()
            else:
                ui.next()

        # else:
        #     return False

        #return True
