from datetime import datetime 
from datetime import date

from xml.etree import ElementTree as ET
from dataclasses import dataclass

@dataclass
class HealthInfo:
    health_number: str = ""
    ident_number:str = ""
    first_name: str = ""
    second_name: str = ""
    surname: str = ""
    begin_date: date = date(1, 1, 1)
    end_date: date = date(1,1,1)

def load_health_info(path: str)->list[HealthInfo]:
    tree = ET.parse("export.xml")
    root = tree.getroot()
    health_info: list[HealthInfo] = []
    for e in root.iter('Row'):
        health_number: str = ""
        ident_number: str = ""
        first_name: str = ""
        second_name: str = ""
        surname: str = ""
        begin_date: date = date(1, 1, 1)
        end_date: date = date(1, 1, 1)
        for child in e:
            if (child.tag == 'WIC_NUM'):
                health_number = child.text
            if (child.tag == 'NP_NUMIDENT'):
                ident_number = child.text
            if (child.tag == 'NP_SURNAME'):
                first_name = child.text
            if (child.tag == 'NP_NAME'):
                second_name = child.text
            if (child.tag == 'NP_PATRONYMIC'):
                surname = child.text
            if (child.tag == 'WIC_DT_BEGIN'):
                begin_date = datetime.strptime(child.text, "%Y-%m-%dT%H:%M:%S")                   
            if (child.tag == 'WIC_DT_END'):
                end_date = datetime.strptime(child.text, "%Y-%m-%dT%H:%M:%S")
        health_info.append(HealthInfo(health_number,ident_number,first_name,second_name,surname,begin_date, end_date))
    return health_info           

if (__name__ == '__main__'):
    print(load_health_info('export.xml'))