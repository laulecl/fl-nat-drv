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
import transport
import midi
import playlist



class Context(Abstract.Context):

    def enabled(self) -> bool:
        return self.router.daw.mode == Consts.MODE_PLAYLIST



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        if modes & Consts.JOG_DEFAULT and not press:
            transport.globalTransport(midi.FPT_Jog, step)

        elif modes & Consts.JOG_DEFAULT and press:
            track = self.getTrackSelected()
            if track + step > 0 and track + step <= playlist.trackCount():
                playlist.selectTrack(track)
                playlist.selectTrack(track + step)
                if step > 0:
                    ui.down()
                else:
                    ui.up()

        elif modes & Consts.JOG_SHIFT:
            transport.globalTransport(midi.FPT_PatternJog, step)

        # elif modes & Consts.JOG_SWING:

        elif modes & Consts.JOG_SAMPLING:
            transport.globalTransport(midi.FPT_Jog2, step)

        else:
            return False

        return True



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if btn == Consts.BTN_SOLO:
            playlist.soloTrack(self.getTrackSelected())

        elif btn == Consts.BTN_MUTE:
            playlist.muteTrack(self.getTrackSelected())

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
            pass

        else:
            return False

        print('Pad ', pad)

        return True



    def getTrackSelected(self) -> int:
        for track in range(1, playlist.trackCount()):
            if playlist.isTrackSelected(track):
                return track

        return 0
