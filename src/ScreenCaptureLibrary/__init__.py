from keywords import *
from robot.libraries.BuiltIn import BuiltIn

class ScreenCaptureLibrary (
    _CaptureKeywords,
    _ScreenAreaKeywords):
    """
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        """
        """

        self._sel2lib = BuiltIn().get_library_instance('Selenium2Library')
