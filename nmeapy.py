#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
        PYTHON PARSER FOR NMEA FRAME
"""
import re
def form(frame):
    """
        form is test on nmea frame
        return True if frame is an good NMEA frame. else False
    """
    # Pront at begin of frame
    pront="^\$"
    # Talker id
    talker="(BD|GB|GA|GP|GL)"
    # NMEA Frame Name 
    
    # control sum
    control="*0E"
    # NMEA end of frame \r\n
    end=""#"\r\n"
    virgule=""#"."
    AAM="AAM"
    ALM="ALM"
    APA="APA"
    APB="APB"
    BOD="BOD"
    BWC="BWC"
    DTM="DTM"
    GGA=pront+talker+"GGA"+virgule+end
    GLL="GLL"
    GRS="GRS"
    GSA="GSA"
    GST="GST"
    GSV="GSV"
    MSK="MSK"
    MSS="MSS"
    RMA="RMA"
    RMB="RMB"
    RMC="RMC"
    RTE="RTE"
    TRF="TRF"
    STN="STN"
    VBW="VBW"
    VTG="VTG"
    WCV="WCV"
    WPL="WPL"
    XTC="XTC"
    XTE="XTE"
    ZTG="ZTG"
    ZDA="ZDA"
    HCHDG="HCHDG"
    PSLIB="PSLIB"
    regex_nmea="("+GGA+")"
    print regex_nmea
    if (re.search(regex_nmea, frame)==None):
        return False
    else:
        return True
    
test=["$GPGGA","GPGGA","$GGA","","$","zerze$GPGGA"]
for i in test:
    print i,":",form(i)