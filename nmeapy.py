#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
        PYTHON PARSER FOR NMEA FRAME
"""
import re
def verif(frame):
    """
        form is test on nmea frame
        return True if frame is an good NMEA frame. else False
    """
    # Talker id
    talker="(BD|GB|GA|GP|GL)"
    # NMEA Frame Name 
    frame_name="(AAM|ALM|APA|APB|BOD|BWC|DTM|GGA|GLL|GRS|GSA|GST|GSV|MSK|MSS|RMA|RMB|RMC|RTE|TRF|STN|VBW|VTG|WCV|WPL|XTC|XTE|ZDA|HCHDG|PSLIB)"
    regex_nmea="^\$"+talker+frame_name+",.*"+"(\*[0-F][0-F]\r\n)$"
    print regex_nmea
    if (re.search(regex_nmea, frame)==None):
        return False
    else:
        return True
    
test=["$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E\r\n","$GPGGA,065218.,","$GPGGA,065218.235,","$GPGGA489494","$GGA","","$","zerze$GPGGA"]

for i in test:
    print i,":",verif(i)