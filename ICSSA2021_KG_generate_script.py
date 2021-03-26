import xml.etree.ElementTree as xml
import random
from random import randrange
from datetime import datetime
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('3/1/21 00:00:00', '%m/%d/%y %H:%M:%S')
d2 = datetime.strptime('3/3/21 23:59:59', '%m/%d/%y %H:%M:%S')

#print(random_date(d1, d2))

Max_Hubs = 3
Max_Devices = 100
Max_Users = 100
Max_Assets = 1000
Max_Actions_1 = 100
Max_Actions_2 = 100
Max_Actions_3 = 100
Max_Step_1 = 100
Max_Step_2 = 100
Max_Step_3 = 100
SPARQL_path = "C:/Blazegraph/1"


def createXML(filename):
    """
    Создаем XML файл.
    """
#Open SPARQL file
    spql = open("sparql_script.spql", "wt")

# Add header
    header = '''<?xml version="1.0"?>\n<rdf:RDF\nxmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\nxmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#"\nxmlns:geo="http://www.w3.org/2003/01/geo/"\nxmlns:net="http://purl.org/toco/"\nxmlns:tmno="http://127.0.0.1/tmno/"\n>\n'''
    print (header)

# Add Device  definitions
    FileNum = 0
    i=1
    k=1
    while i <= Max_Devices:
        FileNum = FileNum + 1
        f = open(filename + "_device_" + str(FileNum) + "_.nq", "at")
        f.write(header)
        f.write("\n<!--Device definitions-->\n")
        while k <= Max_Step_1:
            #body = str("<rdf:Description rdf:about='http://127.0.0.1/Device_") + str(i) + str("/'>\n<my:has_id>D") + str (i) + str("</my:has_id>\n<my:is_connected_to_hub>H") + str(random.randint(1, Max_Hubs)) + str("</my:is_connected_to_hub>\n<my:has_the_device_model>") + str(random.choice(j)) + str("</my:has_the_device_model>\n</rdf:Description>\n")
            body = str('<rdf:Description rdf:about="http://127.0.0.1/tmno/Device_') + str(i) + str('/">\n<rdf:type>net:Device</rdf:type>\n<net:hasMAC>MAC_') + str(i) + str('</net:hasMAC>\n</rdf:Description>\n')
            f.write(body)
            i=i+1
            k=k+1
        f.write("\n</rdf:RDF>\n")
        f.close()
        spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_device_" + str(FileNum) + "_.nq>;\n")
        k=1


# Add Users actions definitions
    FileNum = 0
    i = 1
    k = 1
    while i <= Max_Actions_1:
        FileNum = FileNum + 1
        f = open(filename + "_actions_" + str(FileNum) + "_.nq", "at")
        f.write(header)
        f.write("\n<!--User action definitions-->\n")
        while k <= Max_Step_2:
            body = '''<rdf:Description rdf:about='http://127.0.0.1/tmno/Request_''' + str(i) + '''/'>\n<rdf:type>tmno:Request</rdf:type>\n<tmno:request_timestamp rdf:datatype='http://www.w3.org/2001/XMLSchema#datetime'>''' + str(random_date(d1, d2).strftime("%Y-%m-%dT%H:%M:%S")) + '''</tmno:request_timestamp>\n<geo:Point geo:lat="55.701" geo:long="12.552"/>\n<tmno:has_req_type>tmno:user_action</tmno:has_req_type>\n<tmno:request_detailes>\n<rdf:Description>\n<rdf:type>rdf:statement</rdf:type>\n<rdf:predicat>tmno:is_requested_with</rdf:predicat>\n<rdf:subject><rdf:Description rdf:about='http://127.0.0.1/tmno/Service_ID/'></rdf:Description></rdf:subject>\n<rdf:object>\n<rdf:Description rdf:about='http://127.0.0.1/tmno/Asset_ID/'></rdf:Description>\n</rdf:object>\n</rdf:Description>\n</tmno:request_detailes>\n<tmno:Requests>\n<rdf:Description rdf:about='http://127.0.0.1/tmno/Device_''' + str(random.randint(1, Max_Users)) + '''/'>\n</rdf:Description>\n</tmno:Requests>\n</rdf:Description>'''
            print(body)
            f.write(body)
            i = i + 1
            k = k + 1
        f.write("\n</rdf:RDF>\n")
        f.close()
        spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_actions_" + str(FileNum) + "_.nq>;\n")
        k = 1


# Add Events  definitions
    FileNum = 0
    i = 1
    k = 1
    while i <= Max_Actions_2:
        FileNum = FileNum + 1
        f = open(filename + "_events_" + str(FileNum) + "_.nq", "at")
        f.write(header)
        f.write("\n<!--Events definitions-->\n")
        while k <= Max_Step_2:
                device_num = str(random.randint(1,Max_Users))
                body = '''<rdf:Description rdf:about='http://127.0.0.1/tmno/TN_Event_''' + str(i) + '''/'>\n<rdf:type>tmno:TN_Event</rdf:type>\n<tmno:event_timestamp rdf:datatype='http://www.w3.org/2001/XMLSchema#datetime'>''' + str(random_date(d1, d2).strftime("%Y-%m-%dT%H:%M:%S"))  + '''</tmno:event_timestamp>\n<geo:Point geo:lat="55.701" geo:long="12.552"/>\n<tmno:has_event_type>tmno:device_error</tmno:has_event_type>\n<tmno:event_detailes>\n<rdf:Description>\n<rdf:type>rdf:statement</rdf:type>\n<rdf:predicat>tmno:device_event</rdf:predicat>\n<rdf:subject><rdf:Description rdf:about='http://127.0.0.1/tmno/Device_''' + device_num + '''/'></rdf:Description></rdf:subject>\n<rdf:object>tn_event_code</rdf:object>\n</rdf:Description>\n</tmno:event_detailes>\n<tmno:tn_event>\n<rdf:Description rdf:about='http://127.0.0.1/tmno/Device_''' + device_num + '''/'></rdf:Description>\n</tmno:tn_event>\n</rdf:Description>\n'''
                f.write(body)
                i = i + 1
                k = k + 1
        f.write("\n</rdf:RDF>\n")
        f.close()
        spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_events_" + str(FileNum) + "_.nq>;\n")
        k = 1

# Add Monitoring items definitions
        FileNum = 0
        i = 1
        k = 1
        while i <= Max_Actions_3:
            FileNum = FileNum + 1
            f = open(filename + "_monitoring_" + str(FileNum) + "_.nq", "at")
            f.write(header)
            f.write("\n<!--Monitoring items definitions-->\n")
            while k <= Max_Step_3:
                device_num = str(random.randint(1, Max_Users))
                body = '''<rdf:Description rdf:about='http://127.0.0.1/tmno/Parameter_M_''' + str(i) + '''/'>\n<rdf:type>tmno:Parameter_M</rdf:type>\n<tmno:parameter_timestamp rdf:datatype='http://www.w3.org/2001/XMLSchema#datetime'>''' + str(random_date(d1, d2).strftime("%Y-%m-%dT%H:%M:%S")) + '''</tmno:parameter_timestamp>\n<geo:Point geo:lat="55.701" geo:long="12.552"/>\n<tmno:has_parameter_type>tmno:device_state</tmno:has_parameter_type>\n<tmno:parameter_detailes>\n<rdf:Description>\n<rdf:type>rdf:statement</rdf:type>\n<rdf:predicat>tmno:parameter_monitoring</rdf:predicat>\n<rdf:subject><rdf:Description rdf:about='http://127.0.0.1/tmno/Device_''' + device_num + '''/'></rdf:Description></rdf:subject>\n<rdf:object>parameter_value</rdf:object>\n</rdf:Description>\n</tmno:parameter_detailes>\n<tmno:device_parameter>\n<rdf:Description rdf:about='http://127.0.0.1/tmno/Device_''' + device_num + '''/'></rdf:Description>\n</tmno:device_parameter>\n</rdf:Description>\n'''
                f.write(body)
                i = i + 1
                k = k + 1
            f.write("\n</rdf:RDF>\n")
            f.close()
            spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_monitoring_" + str(FileNum) + "_.nq>;\n")
            k = 1

    spql.close()


if __name__ == "__main__":
    createXML("KG_telecom")
