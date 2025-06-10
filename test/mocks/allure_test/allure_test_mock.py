from enum import Enum
import xml
import os
import pathlib

SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'scenarios')

class AllureTestMocks(str, Enum):
    EMPTY_DOCUMENT = "EMPTY_DOCUMENT"
    HAPPY_PATH     = "HAPPY_PATH"
    WRONG_TAG_TEST_SUITE = "WRONG_TAG_TEST_SUITE"
    TEST_SUITE_MISSING_NAME     = "TEST_SUITE_MISSING_NAME"
    TEST_SUITE_MISSING_START_TIME = "TEST_SUITE_MISSING_START_TIME"
    TEST_SUITE_MISSING_END_TIME = "TEST_SUITE_MISSING_END_TIME"
    TEST_CASE_MISSING_NAME = "TEST_CASE_MISSING_NAME"
    TEST_CASE_MISSING_START_TIME = "TEST_CASE_MISSING_START_TIME"
    TEST_CASE_MISSING_END_TIME = "TEST_CASE_MISSING_END_TIME"
    TEST_CASE_MISSING_STATUS = "TEST_CASE_MISSING_STATUS"
    TEST_CASE_WRONG_STATUS = "TEST_CASE_WRONG_STATUS"
    TEST_LABEL_MISSING_NAME = "TEST_LABEL_MISSING_NAME"
    TEST_LABEL_MISSING_VALUE = "TEST_LABEL_MISSING_VALUE"
    TEST_PARAMETER_MISSING_NAME = "TEST_PARAMETER_MISSING_NAME"
    TEST_PARAMETER_MISSING_VALUE = "TEST_PARAMETER_MISSING_VALUE"
    TEST_PARAMETER_MISSING_KIND = "TEST_PARAMETER_MISSING_KIND"
    TEST_PARAMETER_WRONG_KIND = "TEST_PARAMETER_WRONG_KIND"
    TEST_STEP_MISSING_NAME = "TEST_STEP_MISSING_NAME"
    TEST_STEP_MISSING_START_TIME = "TEST_STEP_MISSING_START_TIME"
    TEST_STEP_MISSING_END_TIME = "TEST_STEP_MISSING_END_TIME"
    TEST_STEP_MISSING_STATUS = "TEST_STEP_MISSING_STATUS"
    TEST_STEP_WRONG_STATUS = "TEST_STEP_WRONG_STATUS"
    TEST_FAILURE_MISSING_MESSAGE = "TEST_FAILURE_MISSING_MESSAGE"
    TEST_ATTACHMENT_MISSING_SOURCE = "TEST_ATTACHMENT_MISSING_SOURCE"
    TEST_ATTACHMENT_MISSING_TITLE = "TEST_ATTACHMENT_MISSING_TITLE"
    TEST_ATTACHMENT_MISSING_TYPE = "TEST_ATTACHMENT_MISSING_TYPE"
    
ALLURE_TEST_MOCKS: dict[AllureTestMocks, dict] = \
{
    AllureTestMocks.EMPTY_DOCUMENT: open(os.path.join(SCENARIOS_PATH, 'empty_document.xml')).read(),
    AllureTestMocks.HAPPY_PATH: open(os.path.join(SCENARIOS_PATH, 'happy_path.xml')).read(),
    AllureTestMocks.WRONG_TAG_TEST_SUITE: open(os.path.join(SCENARIOS_PATH, 'wrong_tag_test_suite.xml')).read(),
    AllureTestMocks.TEST_SUITE_MISSING_NAME: open(os.path.join(SCENARIOS_PATH, 'test_suite_missing_name.xml')).read(),
    AllureTestMocks.TEST_SUITE_MISSING_START_TIME: open(os.path.join(SCENARIOS_PATH, 'test_suite_missing_start_time.xml')).read(),
    AllureTestMocks.TEST_SUITE_MISSING_END_TIME: open(os.path.join(SCENARIOS_PATH, 'test_suite_missing_end_time.xml')).read(),
    AllureTestMocks.TEST_CASE_MISSING_NAME: open(os.path.join(SCENARIOS_PATH, 'test_case_missing_name.xml')).read(),
    AllureTestMocks.TEST_CASE_MISSING_START_TIME: open(os.path.join(SCENARIOS_PATH, 'test_case_missing_start_time.xml')).read(),
    AllureTestMocks.TEST_CASE_MISSING_END_TIME: open(os.path.join(SCENARIOS_PATH, 'test_Case_missing_end_time.xml')).read(),
    AllureTestMocks.TEST_CASE_MISSING_STATUS: open(os.path.join(SCENARIOS_PATH, 'test_case_missing_status.xml')).read(),
    AllureTestMocks.TEST_CASE_WRONG_STATUS: open(os.path.join(SCENARIOS_PATH, 'test_case_wrong_status.xml')).read(),
    AllureTestMocks.TEST_LABEL_MISSING_NAME: open(os.path.join(SCENARIOS_PATH, 'test_label_missing_name.xml')).read(),
    AllureTestMocks.TEST_LABEL_MISSING_VALUE: open(os.path.join(SCENARIOS_PATH, 'test_label_missing_value.xml')).read(),
    AllureTestMocks.TEST_PARAMETER_MISSING_NAME: open(os.path.join(SCENARIOS_PATH, 'test_parameter_missing_name.xml')).read(),
    AllureTestMocks.TEST_PARAMETER_MISSING_VALUE: open(os.path.join(SCENARIOS_PATH, 'test_parameter_missing_value.xml')).read(),
    AllureTestMocks.TEST_PARAMETER_MISSING_KIND: open(os.path.join(SCENARIOS_PATH, 'test_parameter_missing_kind.xml')).read(),
    AllureTestMocks.TEST_PARAMETER_WRONG_KIND: open(os.path.join(SCENARIOS_PATH, 'test_parameter_wrong_kind.xml')).read(),
    AllureTestMocks.TEST_STEP_MISSING_NAME: open(os.path.join(SCENARIOS_PATH, 'test_step_missing_name.xml')).read(),
    AllureTestMocks.TEST_STEP_MISSING_START_TIME: open(os.path.join(SCENARIOS_PATH, 'test_step_missing_start_time.xml')).read(),
    AllureTestMocks.TEST_STEP_MISSING_END_TIME: open(os.path.join(SCENARIOS_PATH, 'test_step_missing_end_time.xml')).read(),
    AllureTestMocks.TEST_STEP_MISSING_STATUS: open(os.path.join(SCENARIOS_PATH, 'test_step_missing_status.xml')).read(),
    AllureTestMocks.TEST_STEP_WRONG_STATUS: open(os.path.join(SCENARIOS_PATH, 'test_step_wrong_status.xml')).read(),
    AllureTestMocks.TEST_FAILURE_MISSING_MESSAGE: open(os.path.join(SCENARIOS_PATH, 'test_failure_missing_message.xml')).read(),
    AllureTestMocks.TEST_ATTACHMENT_MISSING_SOURCE: open(os.path.join(SCENARIOS_PATH, 'test_attachment_missing_source.xml')).read(),
    AllureTestMocks.TEST_ATTACHMENT_MISSING_TITLE: open(os.path.join(SCENARIOS_PATH, 'test_attachment_missing_title.xml')).read(),
    AllureTestMocks.TEST_ATTACHMENT_MISSING_TYPE: open(os.path.join(SCENARIOS_PATH, 'test_attachment_missing_type.xml')).read()
}