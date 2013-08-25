Robot Framework library for capturing screenshots and image manipulation for the purpose of documentation.

Reason for another capture screenshot keyword/library:
------------------------------------------------------
The motivation for and the end goal of this library is to be able to reproduce the images or screenshots within manual "A User's Guide to Plone 4". By combining Plone's use of Robot Framework and Selenium for testing one should be able to automate both screen captures and various elements or parts of the Plone UI for documentation.

The advantage this library is trying to gain over the current Capture Screenshot keyword is the automation of the cropping, enhancing and annotating of screenshots given that while we are within selenium we can extract information about where elements are. So if the template changes or is styled differently the screenshot along with annotations and enhancements can easily be redone. With an optional layered output format like svg where each enhancement or cropping step is included in the output format an editor could come through and make minor tweaks to the marked up screenshot. 


Features I would like to see:
-----------------------------

- Output to various image formats including GIMP xcf format and/or SVG so various objects (like arrows, labels, etc. can be easily post-manipulated.
- Debug keyword which takes multiple screenshots as keyword narrows down area


Other Robot Framework Libraries required
----------------------------------------
This library will "extend" or use functionality from the `Selenium2Library <https://github.com/rtomac/robotframework-selenium2library>`_. There is also a Robot Framework library, `Screenshot Built-In Library <http://robotframework.googlecode.com/hg/doc/libraries/Screenshot.html>`_, for taking a screenshoot of the entire screen.


General format of screen capture keyword
---------------------------------------
The general format of the screen capture command goes something like

Take screenshot [of <element or screenarea>
                 from <element> down|right|up|left [of/past/to <element>]
                 add <drawing object>
		 obscuring <element>
		 numbering <element> [as <integer or letter>]
		 (saving) as

                 but excluding
                 and including

		 
Other keywords
--------------
Other (conceptual) keywords which will provide functionality

Create Screen Area  [union of elements]

Set screencast debug  on/off


Parser
------
Given the general format of the 'take screenshot' keyword or as in this example

    | Take screenshot | of id=header|
    | ... | from <element> down|right|up|left [of/past/to <element>]
    | ... | add <drawing object>
    | ... | obscuring <element>
    | ... | (saving) as <filename>

the parser should seperate out a SENTENCE from the SENTANCES or arguments of the keywords. Each argument should be it's own SENTENCE and no single SENTENCE should be broken into seperate keyword arguments. Each SENTENCE should start with an ACTION (of, from, add, obscuring, as). Some ACTIONs help define the screenarea (of, from) while other ACTION(s) help to annotate the screenshot (add) and still other ACTION(s) enhance parts of the screenarea (obscuring) or used for defining the filename of the screenshot (as).

A single SENTENCE should be allowed to contain multiple ACCTIONs within itself. For example 

    | Take screenshot | of <element> adding <drawing object>

contains a single SENTENCE ('of <element> adding <drawing object>') but two ACTIONS and their corresponding object; one being 'of <element>' and the other 'adding <drawing object>'.

ACTIONs should be allowed to be in either present tense (Example: obscure) or present progressive tense (Example: obscuring) and these two should be considered the same ACTION. The define filename ACTION 'as' can also written as 'save as' or 'saving as' using present tense and present progressive tense respectively; in other words the 'save/saving' part is optional.

Alternative Method
------------------
`Asko`_ `Soukka`_ (`@datakurre`_) has presented a different model; one which doesn't rely on modifying or replacing the underlying parser. His work is part of `plone.app.robotframework`_ which is the Robot Framework toolset to help test Plone CMS. The majority of the annotation functionality is built using Robot Framework keywords (see `annotate.robot`_) while image croping is provided by a python function using PIL (see `annotate.py`_). This is different from the model I envisioned and outlined here but provides a solid model with several advantages over my model.

Screenarea references
---------------------
SVG
  <polygon points="points-specifications"/>
  example: <polygon points="0,0 5,0 5,5 0,5"/>
  units: 
  inside/outside path: clockwise path to make area inside

CSS
  http://www.w3.org/TR/CSS2/visuren.html

PIL
  region is defined by a 4-tuple, where coordinates are (left, upper, right, lower)
  coordinate system with (0, 0) in the upper left corner

svgwrite 
  a point is a 2-tuple (x, y): x, y = <number>
  All coordinate values are in the user coordinate system (no units allowed)

  
Example "keywords"
------------------
Presented here are sample examples of "keywords" using figures from "A User's Guide to Plone 4" as a goal.  The "keywords" are not an exact word-for-word Robot Framework keyword but a sketch of what I am trying to achieve.

Figure 2.1

    Take Screenshot of portal header starting with portal searchbox

    Take Screenshot of portal header right of and including portal searchbox

    Take Screenshot of portal header from portal searchbox right

Figure 2.2

    Take Screenshot of edit bar ?????????

Figure 2.3

    Take Screenshot of edit bar

    Take Screenshot of edit bar as figure-2.3

Figure 2.4

    Take screenshot of portal-column-content (no margin) from edit-bar down to 95% of archetypes-fieldname-text

Figure 2.5

Figure 2.6

    Take screenshot of Insert\Edit link overlay

    Take screenshot of id="mce_73"

    Take screenshot of Insert\Edit link overlay
        add arrow pointing towards External

Figure 2.7

    Take screenshot of Insert\Edit image overlay

Figure 2.8

    Take screenshot of Insert\Edit image overlay

Figure 2.9

   Take screenshot of portal-column-content (no margin) from cmfeditions_version_comment_block down

Figure 2.10

   Take screenshot of news_item-base-edit down to archetypes-fieldname-subject

Figure 2.11

    Take screenshot of news_item-base-edit

:: _Asko: http://datakurre.pandala.org/
:: _Soukka: https://twitter.com/datakurre
:: _@datakurre: https://github.com/datakurre
:: _plone.app.robotframework: https://github.com/plone/plone.app.robotframework
:: _annotate.robot: https://github.com/plone/plone.app.robotframework/blob/master/src/plone/app/robotframework/annotate.robot
:: _annotate.py: https://github.com/plone/plone.app.robotframework/blob/master/src/plone/app/robotframework/annotate.py
