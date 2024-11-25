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
import general
import transport
import midi
import channels
import ui



class Context(Abstract.Context):

    def enabled(self) -> bool:
        return self.router.daw.mode == Consts.MODE_PIANO_ROLL



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        if modes & Consts.JOG_DEFAULT:
            transport.globalTransport(midi.FPT_Jog2, step * -1)

        elif modes & Consts.JOG_SHIFT:
            transport.globalTransport(midi.FPT_Jog, step)

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
        if shift:
            return False

        if 0 == pressure:
            return True

        if 1 == pad:
            general.undoUp()

        elif 2 == pad:
            general.undoDown()

        elif 3 == pad:
            general.undoUp()

        elif 4 == pad:
            general.undoDown()

        elif 5 == pad:
            channels.quickQuantize(channels.selectedChannel(2))

        elif 6 == pad:
            channels.quickQuantize(channels.selectedChannel(1))

        elif 9 == pad:
           ui.delete()

        elif 10 == pad:
           ui.delete()

        elif 11 == pad:
           ui.copy()

        elif 12 == pad:
            ui.paste()

        else:
            return False



        print('Pad ', pad)

        return True
