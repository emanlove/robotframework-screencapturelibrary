Robot Framework library for capturing screenshots and image manipulation for the purpose of documentation.

Reason: The motivation for and the end goal of this library is to be able to reproduce the images or screenshots within manual "A User's Guide to Plone 4". By combining Plone's use of Robot Framework and Selenium for testing one should be able to automate both screen captures and various elements or parts of the Plone UI for documentation.


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
                 from <element> down|right|up|left [of/to <element>]
                 add <drawing object>
		 obscuring <element>
		 (saving) as

                 but excluding
                 and including
		 
Other keywords
--------------
Other (conceptual) keywords which will provide functionality

Create Screen Area  [union of elements]

Set screencast debug  on/off


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
