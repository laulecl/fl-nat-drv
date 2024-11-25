# name=FLNatDrv Komplete Kontrol S88
# supportedHardwareIds=00 20 6B 02 00 04 04 ## Changer
# url=

"""
[[
	Surface:	Komplete Kontrol S88
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""
import Test

#import TestUsb

#from MaschineMikroMK3 import MaschineMikroMK3

from nihia import buttons


def OnKeyPressure(event):
    #global _mmmk3
    #_mmmk3.onPadPressure(event)
    Test.printEvent(event, "OnKeyPressure")




def OnControlChange(event):
    #global _mmmk3
    #_mmmk3.onControlChange(event)
    Test.printEvent(event, "OnControlChange")
    buttons.setLight()



#def OnUpdateMeters():
    #global _mmmk3
    #_mmmk3.onGlobalChange()




def OnNoteOn(event):
    #event.handled = True
    #_mmmk3.onPadPress(event)
    Test.printEvent(event, "OnNoteOn")



def OnProgramChange(event):
    Test.printEvent(event, "OnProgramChange")



def OnPitchBend(event):
    Test.printEvent(event, "OnPitchBend")



def OnChannelPressure(event):
    Test.printEvent(event, "OnChannelPressure")



def OnSysEx(event):
    Test.printEvent(event, "OnSysEx")



def OnInit():
    #global _mmmk3
    print('Loaded MIDI driver FLNatDrv for Komplete Kontrol S88')
    #_mmmk3 = MaschineMikroMK3()
