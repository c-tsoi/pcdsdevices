"""
Module for the two dimension laser coupling in TMO.
"""
from lightpath import LightpathState
from ophyd.device import Component as Cpt

from .device import GroupDevice
from .epics_motor import BeckhoffAxisEPS
from .interface import BaseInterface, LightpathMixin


class TMOLaserCouplingTwoDimension(BaseInterface, GroupDevice, LightpathMixin):
    """

    TMO two dimension laser coupling LI2K4 class.


    Parameters:
    -----------
    prefix : str
        Base PV for the motion system

    name : str
        Alias for the device
    """
    # UI Representation
    _icon = 'fa.minus-square'
    tab_component_names = True

    # LaserCoupling LI2K4 x and Y
    li2k4_x = Cpt(BeckhoffAxisEPS, ':MMS:X', doc="X-axis of lasercoupling li2k4", kind='normal')
    li2k4_y = Cpt(BeckhoffAxisEPS, ':MMS:Y', doc="Y-axis of lasercoupling li2k4", kind='normal')
    removed = False
    transmission = 1
    SUB_STATE = 'state'

    # dummy signal, state is always the same
    lightpath_cpts = ['li2k4_x.user_readback']

    def calc_lightpath_state(self, **kwargs) -> LightpathState:
        # TODO: get real logic here, instead of legacy hard-coding
        return LightpathState(
            inserted=True,
            removed=False,
            output={self.output_branches[0]: 1}
        )
