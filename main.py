import gevent
import gpiozero
from connect_ffi import ffi, lib
from connect import Connect

connect_app = Connect()


def playback_play():
    lib.SpPlaybackPlay()


def playback_pause():
    lib.SpPlaybackPause()


def playback_prev():
    lib.SpPlaybackSkipToPrev()


def playback_next():
    lib.SpPlaybackSkipToNext()


# Loop to pump events
def pump_events():
    lib.SpPumpEvents()
    gevent.spawn_later(0.1, pump_events)


pump_events()

gevent.wait()


lib.SpFree()
