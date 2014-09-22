# -*- coding: utf-8 -*-
"""
prd.py
======

Context decorator for producing figures which are ready to publish
in Physical Review D.

EPS format for image file are used, because it is high quality and working
in actual physical size rahter than pixel unit.

"""

from .general import MPLdecorator
from .colors import brewer_set1
from .layout import GOLDEN_RATIO

__all__ = ['prd_decorator', ]

# Constants from PRD Authour Guidelines.
width_single_column = 3.4
width_double_column = 7.0

# Default ratio for a single plot figure
# I prefer a little higher than goden ratio, from 0.618 to about 0.68
height_width_ratio = GOLDEN_RATIO * 1.1  # = height / width

_width = width_single_column
_height = width_single_column * height_width_ratio

_params = {'font.family' : 'serif',
           'font.serif' : ['Computer Modern Roman','Times'],
           'font.sans-serif' :  ['Computer Modern Sans serif','Helvetica'],
           'text.usetex' : True,

           'axes.color_cycle': brewer_set1,
           'axes.labelsize' : 9,
           'axes.linewidth' : 1,

           'figure.figsize' : (_width, _height),
           'figure.subplot.left' : 0.125,
           'figure.subplot.right' : 0.95,
           'figure.subplot.bottom' : 0.1,
           'figure.subplot.top' : 0.95,

           'savefig.dpi' : 300,
           'savefig.format': 'pdf',
           #'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize' : 7.5,
           'legend.frameon' : False,
           'legend.numpoints' : 1,
           'legend.handlelength' : 2,
           'legend.scatterpoints' : 1,
           'legend.labelspacing' : 0.5,
           'legend.markerscale' : 0.9,
           'legend.handletextpad' : 0.5,  # pad between handle and text
           'legend.borderaxespad' : 0.5,  # pad between legend and axes
           'legend.borderpad' : 0.5,  # pad between legend and legend content
           'legend.columnspacing' : 1,  # pad between each legend column

           'text.fontsize' : 8,
           'xtick.labelsize' : 8,
           'ytick.labelsize' : 8,

           'lines.linewidth' : 1,
           'lines.markersize' : 4,
           #'lines.markeredgewidth' : 0,
           # 0 will make line-type markers, such as '+', 'x', invisible
          }

prd_decorator = MPLdecorator(_params)

