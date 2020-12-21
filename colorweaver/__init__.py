# -*- coding: utf-8 -*-
"""
/***************************************************************************
 colorweaver
                                 A QGIS plugin
 Multivariate choropleths from spatial patterns, not blended colours
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-12-20
        copyright            : (C) 2020 by Luke Bergmann and David O'Sullivan
        email                : luke.bergmann@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load colorweaver class from file colorweaver.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .colorweaver import colorweaver
    return colorweaver(iface)
