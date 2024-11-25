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


# test de plugin...
class Plugin(Abstract.Plugin):

    def name(self) -> str:
        return "FPC"



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        pass
        # ne fonctionne pas
        # if modes & Consts.JOG_DEFAULT:
            # if step == 1:
            #     plugins.prevPreset(channels.selectedChannel(), False)
            # else:
            #     plugins.nextPreset(channels.selectedChannel(), False)

        # else:
        #     return False

        #return True



    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        noteMap = {
            1: {"note": Consts.NOTE_DO2, "octave": 3},
            2: {"note": Consts.NOTE_DO, "octave": 3},
            3: {"note": Consts.NOTE_FA2, "octave": 3},
            4: {"note": Consts.NOTE_FA2, "octave": 4},

            5: {"note": Consts.NOTE_MI, "octave": 3},
            6: {"note": Consts.NOTE_RE, "octave": 3},
            7: {"note": Consts.NOTE_LA2, "octave": 3},
            8: {"note": Consts.NOTE_SOL2, "octave": 3},

            9:  {"note": Consts.NOTE_DO, "octave": 4},
            10: {"note": Consts.NOTE_SI, "octave": 3},
            11: {"note": Consts.NOTE_LA, "octave": 3},
            12: {"note": Consts.NOTE_SOL, "octave": 3},

            13: { "note": Consts.NOTE_DO2, "octave": 4 },
            14: {"note": Consts.NOTE_SOL, "octave": 4},
            15: {"note": Consts.NOTE_RE2, "octave": 4},
            16: {"note": Consts.NOTE_FA, "octave": 4},
        }

        if 0 == pressure:
            newPressure = 0
        elif pressure > 100:
            newPressure = 127
        else:
            newPressure = 80 + round(pressure / 127 * 47)

        self.router.note(noteMap[pad]['note'], noteMap[pad]['octave'] + (1 if shift else 0), newPressure)

        return True

