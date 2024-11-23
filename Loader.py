"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

import Contexts.Interface
import Contexts.Transport
import Contexts.Channel
import Contexts.Pattern
import Contexts.Grid
import Contexts.Mixer
import Contexts.Plugin
import Plugins.FlKeys
import Plugins.Kontakt
import Plugins.KompleteKontrol
import Plugins.Nexus
import Plugins.Massive
import Plugins.Battery
import Plugins.Analoglab
import Plugins.PoiZone



class Loader:

    def __init__(self, router):
        self._contexts = [
            Contexts.Interface.Context(router),
            Contexts.Transport.Context(router),

            Plugins.FlKeys.Plugin(router),
            Plugins.Kontakt.Plugin(router),
            Plugins.KompleteKontrol.Plugin(router),
            Plugins.Nexus.Plugin(router),
            Plugins.Massive.Plugin(router),
            Plugins.Battery.Plugin(router),
            Plugins.Analoglab.Plugin(router),
            Plugins.PoiZone.Plugin(router),

            Contexts.Plugin.Context(router),
            Contexts.Grid.Context(router),
            Contexts.Channel.Context(router),
            Contexts.Pattern.Context(router),
            Contexts.Mixer.Context(router)
        ]

    def contexts(self):
        return self._contexts
