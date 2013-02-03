from robot.api import logger

AREA_DEFINING_ACTIONS = ['of', 'from', 'down', 'right', 'up', 'left']
DIRECTIONAL_MARKERS = ['of', 'past', 'to']

class _CaptureKeywords(object):

    def take_screenshot(self, *args):
        """
        Example:
        | Take screenshot | of id=header|
        
        To do:
        | Take screenshot | of id=header|
        | ... | from <element> down|right|up|left [of/to <element>]
        | ... | add <drawing object>
	| ... | obscuring <element>
	| ... | (saving) as
        
        """
        #import pdb, sys; pdb.Pdb(stdout=sys.__stdout__).set_trace()
        # area starts with full screen
        sel2lib = self._sel2lib
        
        body = sel2lib._element_find('tag=body',True, True)
        area = body.size
        for arg in args:
            self._parse_arg(arg)
        
    def capture_region(self):
        """
        """

        pass

    def capture_window(self):
        """
        """

        pass

    def capture_fullscreen(self):
        """
        """

        pass
    
    def _parse_arg(self, arg):
        """
        Highly simple parser to parse out action ('of', 'from', ... )
        from noun (<element> or <screenarea>)
        """
        noun = arg
        while noun:
            action, sep, noun = noun.partition(' ')
            print action, sep, noun
            logger.console("\n%s :: %s :: %s" % (action, sep, noun))

    def _define_area(self):
        pass

