

#helpful packet structures
#
PACKET_OPTIONS = {'captured_length',
 'eth', 'frame_info', 'get_multiple_layers', 'gsm_map', 'highest_layer', 
'interface_captured', 'ip', 'layers', 'length', 'm3ua', 'number', 'pretty_print',
 'sccp', 'sctp', 'show', 'sniff_time', 'sniff_timestamp', 'tcap', 'transport_layer'}


Gsm_Map_Data = {'Target_e164_CC':"",'Target_e164_Msisdn':"",'Target_Extension':"",'Target_Field_names':"",'Target_Get':"",'Target_Get_Field':"",'Target_GFBSN':"",
'Target_GFV':"",'Target_GSM_Oldinvoke':"",'Target_GSM_Oldinvoke_id':"",'Target_gsm_Old_Localvalue':"",
'Target_GSM_Old_Opcode':"",'Target_Nature_Of_Number':"",'Target_Number_Plan':"",'Target_GSM_Sm_Msisdn':"",'Target_Sm_Servicecentreaddress':""
,'Target_sm_sm_rp_pri':""}

M3UA_DATA = {'message_class':"", 'message_length':"", 'message_type':"", 'mtp3_dpc':"", 'mtp3_ni':"", 'mtp3_opc':"", 'mtp3_pc':"", 'mtp3_sls':"", 'network_appearance':"", 'parameter_length':"", 'parameter_padding':"", 'parameter_tag':"", 'pretty_print':"", 'protocol_data_dpc':"", 'protocol_data_mp':"", 'protocol_data_ni':"", 'protocol_data_opc':"", 'protocol_data_si':"", 'protocol_data_sls':"", 'raw_mode':"", 'reserved':"", 'routing_context':"", 'version':""}

SCCP_DATA = {'called_digits':"", 'called_digits_length':"", 'called_es':"", 'called_gti':"", 'called_nai':"", 'called_np':"", 'called_pci':"", 'called_reserved':"", 'called_ri':"", 'called_ssn':"", 'called_ssni':"", 'called_tt':"", 'calling_digits':"", 'calling_digits_length':"", 'calling_es':"", 'calling_gti':"", 'calling_nai':"", 'calling_np':"", 'calling_pci':"", 'calling_reserved':"", 'calling_ri':"", 'calling_ssn':"", 'calling_ssni':"", 'calling_tt':"", 'class':"", 'digits':"", 'e164_country_code':"", 'field_names':"", 'get':"", 'get_field':"", 'get_field_by_showname':"", 'get_field_value':"", 'handling':"", 'layer_name':"", 'linked_dissector':"", 'message_type':"", 'parameter_length':"", 'pretty_print':"", 'raw_mode':"", 'ssn':"", 'variable_pointer1':"", 'variable_pointer2':"", 'variable_pointer3':""}

SNIFF_TIME = {'astimezone':"", 'combine':"", 'ctime':"", 'date':"", 'day':"", 'dst':"", 'fromordinal':"", 'fromtimestamp':"", 'hour':"", 'isocalendar':"", 'isoformat':"", 'isoweekday':"", 'max':"", 'microsecond':"", 'min':"", 'minute':"", 'month':"", 'now':"", 'replace':"", 'resolution':"", 'second':"", 'strftime':"", 'strptime':"", 'time':"", 'timetuple':"", 'timetz':"", 'today':"", 'toordinal':"", 'tzinfo':"", 'tzname':"", 'utcfromtimestamp':"", 'utcnow':"", 'utcoffset':"", 'utctimetuple':"", 'weekday':"", 'year':""}
