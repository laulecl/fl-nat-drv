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
import general
import midi
import transport
import ui
import patterns



class Context(Abstract.Context):

    def __init__(self, router):
        Abstract.Context.__init__(self, router)
        self.currentStep = None
        self.currentStepParam = 0 # Note pitch by default

    def enabled(self) -> bool:
        return self.router.daw.mode == Consts.MODE_CHANNEL



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if btn == Consts.BTN_SOLO:
            channels.soloChannel(channels.selectedChannel())

        elif btn == Consts.BTN_MUTE:
            channels.muteChannel(channels.selectedChannel())

        elif btn == Consts.BTN_JOG and press:
            channels.showEditor(channels.selectedChannel())

        elif btn == Consts.BTN_PITCH:
            channels.showGraphEditor(False, midi.pPitch, 0, channels.selectedChannel())

        elif btn == Consts.BTN_JOG and self.currentStep is not None:
            self.router.daw.channelStepToggle(self.currentStep)

        else:
            return False

        return True



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        if channels.isGraphEditorVisible():
            return self.graphEditorJog(jog, modes, press, step)
        else:
            return self.defaultJog(jog, modes, press, step)


    def graphEditorJog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        if self.currentStep == None:
            self.currentStepParam += step
            if self.currentStepParam < 0:
                self.currentStepParam = 7
            if self.currentStepParam > 7:
                self.currentStepParam = 0

            channels.showGraphEditor(True, self.currentStepParam, 1, channels.selectedChannel())
        else:
            value = channels.getCurrentStepParam(channels.selectedChannel(), self.currentStep-1, self.currentStepParam)
            value += step
            channels.setStepParameterByIndex(channels.selectedChannel(), patterns.patternNumber(), self.currentStep-1, self.currentStepParam, value)
            channels.updateGraphEditor()
            print('coucou', value)

        return True



    def defaultJog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        if modes & Consts.JOG_DEFAULT:
            transport.globalTransport(midi.FPT_ChannelJog, step)

        elif modes & Consts.JOG_SHIFT:
            transport.globalTransport(midi.FPT_PatternJog, step)

        elif modes & Consts.JOG_VOLUME:
            self.changeParameter(midi.REC_Chan_Vol, step, press)

        elif modes & Consts.JOG_SWING:
            self.changeParameter(midi.REC_Chan_SwingMix, step, press)

        elif modes & Consts.JOG_POSITION:
            self.changeParameter(midi.REC_Chan_Pan, step, press)

        else:
            return False

        return True


    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        if pressure > 0:
            self.currentStep = pad
        else:
            self.currentStep = None

        return True



    def focus(self):
        if not ui.getVisible(midi.widChannelRack):
            ui.showWindow(midi.widChannelRack)

        ui.setFocused(midi.widChannelRack)



    def add(self):  # todo à implémenter
        return None



    def changeParameter(self, recEvent: int, step: int, slow: bool):
        eventId = recEvent + channels.getRecEventId(channels.selectedChannel())
        newValue = channels.incEventValue(eventId, step)
        general.processRECEvent(eventId, newValue, midi.REC_UpdateValue | midi.REC_UpdateControl)
