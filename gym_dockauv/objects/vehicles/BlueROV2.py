import numpy as np
import os
from functools import cached_property
from ..auvsim import AUVSim
from ..statespace import StateSpace


class BlueROV2(AUVSim):
    """
    The BlueROV2 in Heavy configuration (8 T200 Thruster) by Blue Robotics, is capable of depths up to 100 metres.
    More information on the BlueROV2 can be found here: https://bluerobotics.com/store/rov/bluerov2/

    The parameters for the BlueROV2 are loaded via a xml file, SI units are used.
    The system identification data of the BlueROV2 are publicly available from
    - Einarsson, Emil Már, and Andris Lipenitis. n.d. “Model Predictive Control for the BlueROV2,”
    - Wu, Chu-Jou, and B Eng. n.d. “6-DoF Modelling and Control of a Remotely Operated Vehicle,”

    """

    def __init__(self,  xml_path):
        super().__init__()  # Call inherited init functions and then add to it
        StateSpace.read_phys_para_from_xml(self, xml_path)  # Assign BlueROV2 parameters

        # Decided to make values available as properties
        self._B = np.identity(6)
        self._u_bound = np.array([
            [-5, 5],
            [-5, 5],
            [-5, 5],
            [-1, 1],
            [-1, 1],
            [-1, 1]])

    def B(self, nu) -> np.ndarray:
        # TODO: Adapt input of BlueROV2 (for now it applies direct force uncoupled in each direction, maybe do
        #  feasibility study also about control of thrusters, make combination etc
        return self._B

    @cached_property
    def u_bound(self) -> np.ndarray:
        return self._u_bound

    # These functions below are only needed for testing to enter scenarios (cached property does not come with a setter)
    def set_B(self, value):
        self._B = value

    def set_u_bound(self, value):
        self._u_bound = value





