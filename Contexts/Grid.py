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
import channels
import ui
import midi



class Context(Abstract.Context):

    def enabled(self) -> bool:
        return ui.getFocusedFormID() == midi.widChannelRack and self.router.isBtnPressed(Consts.BTN_STEP)



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        if False:
            pass

        else:
            return False

        return True



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if False:
            pass

        else:
            return False

        return True



    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        if pressure > 0:
            if shift:
                if pad == 9:
                    self.clear()
            else:
                self.router.daw.channelStepToggle(pad)

        return True


    def clear(self):
        for i in range(16):
            channels.setGridBit(channels.selectedChannel(), i, 0)
