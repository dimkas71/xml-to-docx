from dataclasses import dataclass
from datetime import date

from datetime import datetime
from xml.etree import ElementTree as ET

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

EMPTY_STRING = ""
DATE_TIME_FORMAT_STRING = "%Y-%m-%dT%H:%M:%S"
EMPTY_DATE = date(1, 1, 1)


@dataclass
class HealthInfo:
    health_number: str = EMPTY_STRING
    ident_number: str = EMPTY_STRING
    first_name: str = EMPTY_STRING
    second_name: str = EMPTY_STRING
    surname: str = EMPTY_STRING
    begin_date: date = EMPTY_DATE
    end_date: date = EMPTY_DATE


def load_health_info(path: str) -> list[HealthInfo]:
    tree = ET.parse("export.xml")
    root = tree.getroot()
    health_info: list[HealthInfo] = []
    for e in root.iter('Row'):
        health_number: str = EMPTY_STRING
        ident_number: str = EMPTY_STRING
        first_name: str = EMPTY_STRING
        second_name: str = EMPTY_STRING
        surname: str = EMPTY_STRING
        begin_date: date = EMPTY_DATE
        end_date: date = EMPTY_DATE
        for child in e:
            if child.tag == 'WIC_NUM':
                health_number = child.text
            if child.tag == 'NP_NUMIDENT':
                ident_number = child.text
            if child.tag == 'NP_SURNAME':
                first_name = child.text
            if child.tag == 'NP_NAME':
                second_name = child.text
            if child.tag == 'NP_PATRONYMIC':
                surname = child.text
            if child.tag == 'WIC_DT_BEGIN':
                begin_date = datetime.strptime(child.text, DATE_TIME_FORMAT_STRING)
            if child.tag == 'WIC_DT_END':
                end_date = datetime.strptime(child.text, DATE_TIME_FORMAT_STRING)
        health_info.append(
            HealthInfo(health_number, ident_number, first_name, second_name, surname, begin_date, end_date))
    return health_info


def save_health_info(source: str, target: str) -> None:
    document = Document()
    p = document.add_paragraph('РЕЄСТР')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = document.add_paragraph('листків непрацездатності, які передані зі служби управління персоналом')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = document.add_paragraph('до комісії зі соціального страхування КП МТК <<Калинівський ринок>>')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    health_info = load_health_info(source)

    table = document.add_table(rows=1, cols=4)
    table_header = table.rows[0].cells
    table_header[0].text = '№ з/п'
    table_header[1].text = 'Прізвище,ім\'я, по батькові'
    table_header[2].text = '№ листка непрацездатності'
    table_header[3].text = 'Номер страхового свідоцтва'

    for index, r in enumerate(health_info):
        row = table.add_row().cells
        row[0].text = f"{index + 1}"
        row[1].text = f"{r.first_name} {r.second_name} {r.surname}"
        row[2].text = f"{r.health_number}"
        row[3].text = f"{r.ident_number}"

    p = document.add_paragraph(f"Листки непрацездатності в кількості {len(health_info)} штуки")
    p = document.add_paragraph(f"Передала:              Прийняв:")
    p = document.add_paragraph(f"Начальник служби       Голова комісії із соціального")
    p = document.add_paragraph(f"управління персоналом  страхування")

    document.save(target)


if __name__ == '__main__':
    save_health_info('export.xml', 'reestr.docx')
