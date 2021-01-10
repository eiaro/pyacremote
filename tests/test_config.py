import unittest

from enum import IntEnum
from pyacremote.config import ACState, OperationMode, FanSpeed, HorizontalSwing, VerticalSwing

class TestACState(unittest.TestCase):
    """
    Tests for ACState
    """
    def test_state_no_args(self):
        state = ACState()

        assert state != None

    def test_state_args(self):
        state = ACState(
            power=True,
            mode=OperationMode.AUTO,
            temperature=25,
            fanspeed=FanSpeed.AUTO,
            verticalswing=VerticalSwing.AUTO,
            horizontalswing=HorizontalSwing.AUTO,
            turbo=True,
            econo=True)

        assert state != None
        assert state.power == True
        assert state.mode == OperationMode.AUTO
        assert state.temperature == 25
        assert state.fanspeed == FanSpeed.AUTO
        assert state.verticalswing == VerticalSwing.AUTO
        assert state.horizontalswing == HorizontalSwing.AUTO        
        assert state.turbo == True
        assert state.econo == True

    def test_state_json(self):
        state = ACState(json=FIXTURE_CONFIG)

        assert state != None
        assert state.power == False
        assert state.mode == OperationMode.OFF
        assert state.temperature == 25
        assert state.fanspeed == FanSpeed.AUTO
        assert state.verticalswing == VerticalSwing.OFF
        assert state.horizontalswing == HorizontalSwing.OFF
        assert state.turbo == False
        assert state.econo == False

    def test_state_temperature(self):
        state = ACState(temperature=25)
        assert state.temperature == 25

        # test that we skip setting temp if it's the same
        state.temperature = 25        
        assert state._temperature == 25
        assert state._hasChanges == False

        # test that we can change temp
        state.temperature = 36        
        assert state._temperature == 36
        assert state._hasChanges == True

    def test_state_mode(self):
        state = ACState(mode=OperationMode.DRY)
        assert state.mode == OperationMode.DRY

        state.mode = OperationMode.DRY
        assert state._mode == OperationMode.DRY
        assert state._hasChanges == False

        state.mode = OperationMode.COOL
        assert state._mode == OperationMode.COOL
        assert state._hasChanges == True

    def test_state_fanspeed(self):
        state = ACState(fanspeed=FanSpeed.MAX)
        assert state.fanspeed == FanSpeed.MAX

        state.fanspeed = FanSpeed.MAX
        assert state._fanspeed == FanSpeed.MAX
        assert state._hasChanges == False

        state.fanspeed = FanSpeed.MIN
        assert state._fanspeed == FanSpeed.MIN
        assert state._hasChanges == True

    def test_state_power(self):
        state = ACState(power=False)
        assert state.power == False

        state.power = False
        assert state._power == False
        assert state._hasChanges == False

        state.power = True
        assert state._power == True
        assert state._hasChanges == True

    def test_state_turbo(self):
        state = ACState(turbo=False)
        assert state.turbo == False

        state.turbo = False
        assert state._turbo == False
        assert state._hasChanges == False

        state.turbo = True
        assert state._turbo == True
        assert state._hasChanges == True

    def test_state_econo(self):
        state = ACState(econo=False)
        assert state.econo == False

        state.econo = False
        assert state._econo == False
        assert state._hasChanges == False

        state.econo = True
        assert state._econo == True
        assert state._hasChanges == True

    def test_state_verticalswing(self):
        state = ACState(verticalswing=VerticalSwing.MIDDLE)
        assert state.verticalswing == VerticalSwing.MIDDLE

        state.verticalswing = VerticalSwing.MIDDLE
        assert state._verticalswing == VerticalSwing.MIDDLE
        assert state._hasChanges == False

        state.verticalswing = VerticalSwing.OFF
        assert state._verticalswing == VerticalSwing.OFF
        assert state._hasChanges == True

    def test_state_horizontalswing(self):
        state = ACState(horizontalswing=HorizontalSwing.MIDDLE)
        assert state.horizontalswing == HorizontalSwing.MIDDLE

        state.horizontalswing = HorizontalSwing.MIDDLE
        assert state._horizontalswing == HorizontalSwing.MIDDLE
        assert state._hasChanges == False

        state.horizontalswing = HorizontalSwing.OFF
        assert state._horizontalswing == HorizontalSwing.OFF
        assert state._hasChanges == True

FIXTURE_CONFIG = {
    "opmode": -1,
    "fanspeed": 0,
    "swingv": -1,
    "swingh": -1,
    "econo": False,
    "turbo": False,
    "power": False,
    "temperature": 25
}






    

    