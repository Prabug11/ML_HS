# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:33:54 2022

@author: The Net Zero Lab
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class HSbiogas(BaseModel):
    TS: float 
    Temp: float 
    OLR: float 
    HRT: float
    pH: float