import pyshark
from chum import *

live_cap = pyshark.LiveCapture(interface='lo',display_filter="sccp")
live_cap.sniff(timeout=50)
M3ua_Data = {}



Sccp_Data = {}



def main():
   for pkt in live_cap
       try:
          print(pkt)
          print pkt.gsm_map.e164_country_code
          print pkt.gsm_map.e164_msisdn
          print pkt.gsm_map.extension
          print pkt.gsm_map.field_names
          print pkt.gsm_map.get
          print pkt.gsm_map.get_field
          print pkt.gsm_map.get_field_by_showname
          print pkt.gsm_map.get_field_value
          print pkt.gsm_map.gsm_old_invoke_element
          print pkt.gsm_map.gsm_old_invokeid
          print pkt.gsm_map.gsm_old_localvalue
          print pkt.gsm_map.gsm_old_opcode
          print pkt.gsm_map.nature_of_number
          print pkt.gsm_map.number_plan
          print pkt.gsm_map.sm_msisdn
          print pkt.gsm_map.sm_servicecentreaddress
          print pkt.gsm_map.sm_sm_rp_pri
 
       except:
          pass    

