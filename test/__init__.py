import pytest


@pytest.fixture(scope="session")
def empty_content():
    return """<?xml version="1.0" encoding="UTF-8"?>
        <Table>
            <Rows>
            </Rows>
        </Table>"""


@pytest.fixture(scope="session")
def content():
    return """<?xml version="1.0" encoding="UTF-8"?>
    <Table>
      <Rows>
        <Row>
          <WIC_NUM>1817771-2003468483-1</WIC_NUM>
          <WIC_CASE_NUM>1817771</WIC_CASE_NUM>
          <WIC_DT_BEGIN>2021-11-30T00:00:00</WIC_DT_BEGIN>
          <WIC_DT_END>2021-12-03T00:00:00</WIC_DT_END>
          <WIC_STATUS>A</WIC_STATUS>
          <WIC_CD>1</WIC_CD>
          <WIC_CD_Name>Тимчасова непрацездатність внаслідок захворювання або травми, що не пов’язані з нещасним випадком на виробництві</WIC_CD_Name>
          <SIGN_ANLK_NARKOTIK_INTOXICATION>false</SIGN_ANLK_NARKOTIK_INTOXICATION>
          <VIOLATION_EXTENSION>false</VIOLATION_EXTENSION>
          <NP_SURNAME>МЕЛЬНИЧУК</NP_SURNAME>
          <NP_NAME>ВЕРОНІКА</NP_NAME>
          <NP_PATRONYMIC>СТЕПАНІВНА</NP_PATRONYMIC>
          <NP_NUMIDENT>3078714906</NP_NUMIDENT>
          <NP_DOC_NUM>КР616885</NP_DOC_NUM>
          <NP_PDT>1</NP_PDT>
        </Row>
      </Rows>
    </Table>"""


all = ["empty_content", "content"]