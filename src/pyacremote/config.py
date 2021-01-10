import logging
from enum import IntEnum

class FanSpeed(IntEnum):
    """Simplified fan speeds for AC"""
    AUTO = 0
    MIN = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    MAX = 5

class OperationMode(IntEnum):
    """Simplified operation modes for AC"""
    OFF = -1
    AUTO = 0
    COOL = 1
    HEAT = 2
    DRY = 3
    FAN = 4

class VerticalSwing(IntEnum):
    """Simplified AC settings for vertical swing"""
    OFF = -1
    AUTO = 0
    HIGHEST = 1
    HIGH = 2
    MIDDLE = 3
    LOW = 4
    LOWEST = 5

class HorizontalSwing(IntEnum):
    """Simplified AC settings for horizontal swing"""
    OFF = -1
    AUTO = 0
    LEFTMAX = 1
    LEFT = 2
    MIDDLE = 3
    RIGHT = 4
    RIGHTMAX  = 5
    WIDE = 6

class ACState(object):
    """Simple representation of common AC controls.

    This should be a very subset of controls that you will 
    find on most AC units and should be reusable over models and makes.
    """
    def __init__(self, 
                 power=False, 
                 mode=OperationMode.OFF, 
                 temperature=21, 
                 fanspeed=FanSpeed.AUTO,
                 verticalswing = VerticalSwing.AUTO,
                 horizontalswing = HorizontalSwing.AUTO,
                 turbo = False,
                 econo = False,
                 json = None) -> None:
        """
        Create a new ACState instance.

        :param power: optional setting for power
        :param mode: optional setting for operation mode
        :param temperature: optional setting for temperature
        :param fanspeed: optional setting for fanspeed
        :param verticalswing: optional setting for vertical swing
        :param horizontalswing: optional setting for horizontal swing
        :param turbo: optional setting for turbo mode
        :param econo: optional setting for economical mode
        """
        if json is not None:
            self._mode  = json.get("opmode")
            self._power = json.get("power")
            self._fanspeed = json.get("fanspeed")
            self._verticalswing = json.get("swingv")
            self._horizontalswing = json.get("swingh")
            self._econo = json.get("econo")
            self._turbo = json.get("turbo")
            self._temperature = json.get("temperature")
        else:
            self._power = power
            self._mode = mode
            self._temperature = temperature
            self._fanspeed = fanspeed
            self._verticalswing = verticalswing
            self._horizontalswing = horizontalswing
            self._turbo = turbo
            self._econo = econo
            
        self._hasChanges = False

    @property
    def fanspeed(self):
        """Set fanspeed"""
        return self._fanspeed
    
    @fanspeed.setter
    def fanspeed(self, value):
        if (self._fanspeed != value):
            self._hasChanges = True
            self._fanspeed = value

    @property
    def mode(self):
        """State for the operation mode"""
        return self._mode

    @mode.setter
    def mode(self, value):
        if (self._mode != value):
            self._hasChanges = True
            self._mode = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if (self._temperature != value):
            self._hasChanges = True
            self._temperature = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if (self._power != value):
            self._hasChanges = True
            self._power = value
    
    @property
    def verticalswing(self):
        return self._verticalswing

    @verticalswing.setter
    def verticalswing(self, value):
        if (self._verticalswing != value):
            self._hasChanges = True
            self._verticalswing = value

    @property
    def horizontalswing(self):
        return self._horizontalswing

    @horizontalswing.setter
    def horizontalswing(self, value):
        if (self._horizontalswing != value):
            self._hasChanges = True
            self._horizontalswing = value

    @property
    def turbo(self):
        return self._turbo

    @turbo.setter
    def turbo(self, value):
        if (self._turbo != value):
            self._hasChanges = True
            self._turbo = value
    
    @property
    def econo(self):
        return self._turbo

    @econo.setter
    def econo(self, value):
        if (self._econo != value):
            self._hasChanges = True
            self._econo = value

