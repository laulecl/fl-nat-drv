"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	1.0

    Copyright (c) 2022 Laurent LECLUSE
]]
"""

import device
import ui
import time
import transport
import mixer
import channels
import midi
import plugins
import playlist
import general

import Consts



def test():
    printPlugin()


    #channels.midiNoteOn(channels.selectedChannel(), 1, 127)
    #print('p=',channels.getCurrentStepParam(channels.selectedChannel(), 0, midi.pPitch))
    status = [2 for _ in range(80)]

    value = 5
    bvalue = 5
    cvalue = 5

    val = 5
    status[39 + 8] = val

    device.midiOutSysex(bytes([128] + status))


    #print(ui.getFocusedPluginName())

    pass



def dataOut(data1: int or hex, data2: int or hex):
    """ Function for easing the communication with the device. By just entering the DATA1 and DATA2 bytes of the MIDI message that has to be sent to the device, it
    composes the full message in order to satisfy the syntax required by the midiOutSysex method,
    as well as setting the STATUS of the message to BF as expected and sends the message.

    data1, data2 -- Corresponding bytes of the MIDI message."""

    # Composes the MIDI message and sends it
    device.midiOutSysex(bytes([240, 191, data1, data2, 247]))


def testJog(step: int):
    #length = transport.getSongLength(midi.SONGLENGTH_S)
    pass








def printPlugin():
    index = channels.selectedChannel()
    if not plugins.isValid(index):
        return None

    print( "Nom du plugin:",plugins.getPluginName(index) )
    print("Index du plugin:", index)
    print("Nombre de paramètres:", plugins.getParamCount(index))
    for p in range(plugins.getParamCount(index)):
        pname = plugins.getParamName(p, index)
        pvalue = plugins.getParamValue(p, index)
        if pname != "" and pname != "#"+str(p).ljust(3,'0'):
            print(str(p).ljust(5, ' '), pname.ljust(50, ' '), pvalue)



def printEvent(event, evtype=""):
    nameLength = 15
    valLength = 15

    # res HIDDEN

    print('\u250C' + '\u2500MIDI\u2500EVENT\u2500\u2500\u2500\u2500' + str(evtype).ljust(22, '\u2500') + str('').rjust(20, '\u2500') + '\u2510')

    print(_eventAttr("status", str(event.status)) + _eventAttr("midiId", str(event.midiId)) + "\u2502")
    print(_eventAttr("data1", str(event.data1)) + _eventAttr("controlNum", str(event.controlNum)) + "\u2502")
    print(_eventAttr("data2", str(event.data2)) + _eventAttr("controlVal", str(event.controlVal)) + "\u2502")
    print(_eventAttr("port", str(event.port)) + _eventAttr("isIncrement", str(event.isIncrement)) + "\u2502")
    print(_eventAttr("note", str(event.note)) + _eventAttr("progNum", str(event.progNum)) + "\u2502")
    print(_eventAttr("velocity", str(event.velocity)) + _eventAttr("pressure", str(event.pressure)) + "\u2502")
    print(_eventAttr("pitchBend", str(event.pitchBend)) + _eventAttr("sysex", str(event.sysex)) + "\u2502")
    print(_eventAttr("inEv", str(event.inEv)) + _eventAttr("midiChanEx", str(event.midiChanEx)) + "\u2502")
    print(_eventAttr("outEv", str(event.outEv)) + _eventAttr("midiChan", str(event.midiChan)) + "\u2502")

    print("\u2514" + str("").rjust(57, "\u2500") + "\u2518")
    print(" ")



def _eventAttr(name: str, value: str):
    return "\u2502 " + name.ljust(11, ' ') + " = " + value.rjust(12, ' ') + ' '



def btnName(btn: int):
    return Consts.DEFAULTS[btn]["name"]



"""
presets

ui.previous()
ui.next()


ui.showWindow(midi.widPianoRoll)

Jouer une note...
channels.midiNoteOn(channels.selectedChannel(), 45, 127)

"""
