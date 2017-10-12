"""
/***************************************************************************
Test
A QGIS plugin
Plugin for testing things
-------------------
begin : 2017-10-10
copyright : (C) 2017 by sanchezfranco
email : saanchezfranco@gmail.com
***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Test"
def description():
    return "For testing purposes"
def version():
    return "Version 1.0"
def icon():
    return "boton1.png"
def qgisMinimumVersion():
    return "2.0"
def classFactory(iface):
    # load Test class from file test.py
    from test import Test
    return Test(iface)
