import pytest

from allure_utils.dal.parsers.Allure1.xml import Allure1XMLParser
from allure_utils.model.test import TestParameterKind, TestStatus, TestSuite

from datetime import datetime

from mocks.allure_test import AllureTestMocks, ALLURE_TEST_MOCKS
from test_utilities.builders.test_builder import \
(
    TestAttachmentBuilder,
    TestCaseBuilder,
    TestFailureBuilder,
    TestLabelBuilder, 
    TestParameterBuilder, 
    TestStepBuilder, 
    TestSuiteBuilder
)

class TestAllure1XMLParser():

    @pytest.mark.parametrize(
      "file_content, expected_test_suite",
      [
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.HAPPY_PATH],
            TestSuiteBuilder().set_start_time(datetime.fromtimestamp(1)) \
                              .set_end_time(datetime.fromtimestamp(2)) \
                              .set_version('1') \
                              .set_name('TestSuiteName') \
                              .set_title('TestSuiteTitle') \
                              .set_description('TestSuiteDescription') \
                              .set_labels(
                                  [
                                    TestLabelBuilder().set_name('label1Name') \
                                                      .set_value('label1Value') \
                                                      .get_element(),
                                    TestLabelBuilder().set_name('label2Name') \
                                                      .set_value('label2Value') \
                                                      .get_element()                 
                                  ]
                              )
                              .set_test_cases(
                                  [
                                    TestCaseBuilder().set_start_time(datetime.fromtimestamp(1)) \
                                                    .set_end_time(datetime.fromtimestamp(2)) \
                                                    .set_status(TestStatus.passed) \
                                                    .set_name('TestCase1Name') \
                                                    .set_title('TestCase1Title') \
                                                    .set_description('TestCase1Description') \
                                                    .set_labels(
                                                        [
                                                            TestLabelBuilder().set_name('label1Name') \
                                                                                .set_value('label1Value') \
                                                                                .get_element(),
                                                            TestLabelBuilder().set_name('label2Name') \
                                                                                .set_value('label2Value') \
                                                                                .get_element()   
                                                        ]
                                                    )
                                                    .set_parameters(
                                                        [
                                                            TestParameterBuilder().set_name('parameter1Name') \
                                                                                    .set_value('parameter1Value') \
                                                                                    .set_kind(TestParameterKind.argument) \
                                                                                    .get_element(),
                                                            TestParameterBuilder().set_name('parameter2Name') \
                                                                                    .set_value('parameter2Value') \
                                                                                    .set_kind(TestParameterKind.system_property) \
                                                                                    .get_element(),
                                                            TestParameterBuilder().set_name('parameter3Name') \
                                                                                    .set_value('parameter3Value') \
                                                                                    .set_kind(TestParameterKind.environment_variable) \
                                                                                    .get_element()
                                                        ]
                                                    )
                                                    .set_attachments(
                                                        [
                                                            TestAttachmentBuilder().set_title('attachment1Title') \
                                                                                    .set_source('attachment1Source') \
                                                                                    .set_type('attachment1Type') \
                                                                                    .get_element(),
                                                            TestAttachmentBuilder().set_title('attachment2Title') \
                                                                                    .set_source('attachment2Source') \
                                                                                    .set_type('attachment2Type') \
                                                                                    .get_element()
                                                        ]
                                                    )
                                                    .set_steps(
                                                        [
                                                            TestStepBuilder().set_start_time(datetime.fromtimestamp(1)) \
                                                                            .set_end_time(datetime.fromtimestamp(2)) \
                                                                            .set_status(TestStatus.failed) \
                                                                            .set_name('Step1Name') \
                                                                            .set_title('Step1Title') \
                                                                            .set_attachments(
                                                                                [
                                                                                    TestAttachmentBuilder().set_title('attachment1Title') \
                                                                                                        .set_source('attachment1Source') \
                                                                                                        .set_type('attachment1Type') \
                                                                                                        .get_element(),
                                                                                    TestAttachmentBuilder().set_title('attachment2Title') \
                                                                                                        .set_source('attachment2Source') \
                                                                                                        .set_type('attachment2Type') \
                                                                                                        .get_element()
                                                                                ]
                                                                            )
                                                                            .set_steps(
                                                                                [
                                                                                    TestStepBuilder().set_start_time(datetime.fromtimestamp(1)) \
                                                                                                        .set_end_time(datetime.fromtimestamp(2)) \
                                                                                                        .set_status(TestStatus.broken) \
                                                                                                        .set_name('Step1Name') \
                                                                                                        .set_title('Step1Title') \
                                                                                                        .get_element()
                                                                                ]
                                                                            )
                                                                            .get_element(),
                                                            TestStepBuilder().set_start_time(datetime.fromtimestamp(1)) \
                                                                            .set_end_time(datetime.fromtimestamp(2)) \
                                                                            .set_status(TestStatus.broken) \
                                                                            .set_name('Step2Name') \
                                                                            .set_title('Step2Title') \
                                                                            .get_element(),
                                                            TestStepBuilder().set_start_time(datetime.fromtimestamp(1)) \
                                                                            .set_end_time(datetime.fromtimestamp(2)) \
                                                                            .set_status(TestStatus.passed) \
                                                                            .set_name('Step3Name') \
                                                                            .set_title('Step3Title') \
                                                                            .get_element(),
                                                            TestStepBuilder().set_start_time(datetime.fromtimestamp(1)) \
                                                                            .set_end_time(datetime.fromtimestamp(2)) \
                                                                            .set_status(TestStatus.canceled) \
                                                                            .set_name('Step4Name') \
                                                                            .set_title('Step4Title') \
                                                                            .get_element(),
                                                            TestStepBuilder().set_start_time(datetime.fromtimestamp(1)) \
                                                                            .set_end_time(datetime.fromtimestamp(2)) \
                                                                            .set_status(TestStatus.pending) \
                                                                            .set_name('Step5Name') \
                                                                            .set_title('Step5Title') \
                                                                            .get_element()
                                                        ]
                                                    ).get_element(),
                                    TestCaseBuilder().set_start_time(datetime.fromtimestamp(1)) \
                                                     .set_end_time(datetime.fromtimestamp(2)) \
                                                     .set_status(TestStatus.failed) \
                                                     .set_name('TestCase2Name') \
                                                     .set_title('TestCase2Title') \
                                                     .set_description('TestCase2Description') \
                                                     .set_failure(
                                                        TestFailureBuilder().set_message('TestCaseFailureMessage') \
                                                                            .set_stack_trace('TestCaseFailureStackTrace') \
                                                                            .get_element()
                                                     )
                                                     .get_element(),
                                  ]
                              ).get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_file_returns_expected_value(self, file_content: str, expected_test_suite: TestSuite) -> None:
        test_suite = Allure1XMLParser.parse(file_content)
        assert expected_test_suite == test_suite

    @pytest.mark.parametrize(
      "file_content, expected_exception",
      [
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.EMPTY_DOCUMENT],
            ValueError('Error while parsing XML. Wrong format')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.WRONG_TAG_TEST_SUITE],
            ValueError('Error while parsing XML. Wrong format')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_SUITE_MISSING_START_TIME],
            ValueError('Error while parsing XML. Start attribute missing on test-suite')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_SUITE_MISSING_END_TIME],
            ValueError('Error while parsing XML. Stop attribute missing on test-suite')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_SUITE_MISSING_NAME],
            ValueError('Error while parsing XML. Name element missing on test-suite')
        )
      ]
    )
    def test_parse_test_suite_raises_expected_exception(self, file_content: str, expected_exception: ValueError) -> None:
        with pytest.raises(ValueError) as value_error_exception:
            Allure1XMLParser.parse(file_content)
            
        assert expected_exception.args == value_error_exception.value.args

    @pytest.mark.parametrize(
      "file_content, expected_exception",
      [
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_CASE_MISSING_START_TIME],
            ValueError('Error while parsing XML. Start attribute missing on test-case')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_CASE_MISSING_END_TIME],
            ValueError('Error while parsing XML. Stop attribute missing on test-case')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_CASE_MISSING_STATUS],
            ValueError('Error while parsing XML. Status attribute missing on test-case')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_CASE_WRONG_STATUS],
            ValueError('Error while parsing XML. Status is not recognized')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_CASE_MISSING_NAME],
            ValueError('Error while parsing XML. Name element missing on test-case')
        )
      ]
    )
    def test_parse_test_case_raises_expected_exception(self, file_content: str, expected_exception: ValueError) -> None:
        with pytest.raises(ValueError) as value_error_exception:
            Allure1XMLParser.parse(file_content)
            
        assert expected_exception.args == value_error_exception.value.args

    @pytest.mark.parametrize(
      "file_content, expected_exception",
      [
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_STEP_MISSING_START_TIME],
            ValueError('Error while parsing XML. Start attribute missing on step')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_STEP_MISSING_END_TIME],
            ValueError('Error while parsing XML. Stop attribute missing on step')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_STEP_MISSING_STATUS],
            ValueError('Error while parsing XML. Status attribute missing on step')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_STEP_WRONG_STATUS],
            ValueError('Error while parsing XML. Status is not recognized')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_STEP_MISSING_NAME],
            ValueError('Error while parsing XML. Name element missing on step')
        )
      ]
    )
    def test_parse_test_step_raises_expected_exception(self, file_content: str, expected_exception: ValueError) -> None:
        with pytest.raises(ValueError) as value_error_exception:
            Allure1XMLParser.parse(file_content)
            
        assert expected_exception.args == value_error_exception.value.args

    @pytest.mark.parametrize(
      "file_content, expected_exception",
      [
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_LABEL_MISSING_NAME],
            ValueError('Error while parsing XML. Name attribute missing on label')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_LABEL_MISSING_VALUE],
            ValueError('Error while parsing XML. Value attribute missing on label')
        )
      ]
    )
    def test_parse_test_label_raises_expected_exception(self, file_content: str, expected_exception: ValueError) -> None:
        with pytest.raises(ValueError) as value_error_exception:
            Allure1XMLParser.parse(file_content)
            
        assert expected_exception.args == value_error_exception.value.args

    @pytest.mark.parametrize(
      "file_content, expected_exception",
      [
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_FAILURE_MISSING_MESSAGE],
            ValueError('Error while parsing XML. Message element missing on failure')
        )
      ]
    )
    def test_parse_test_failure_raises_expected_exception(self, file_content: str, expected_exception: ValueError) -> None:
        with pytest.raises(ValueError) as value_error_exception:
            Allure1XMLParser.parse(file_content)
            
        assert expected_exception.args == value_error_exception.value.args

    @pytest.mark.parametrize(
      "file_content, expected_exception",
      [
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_ATTACHMENT_MISSING_SOURCE],
            ValueError('Error while parsing XML. Source attribute missing on attachment')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_ATTACHMENT_MISSING_TITLE],
            ValueError('Error while parsing XML. Title attribute missing on attachment')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_ATTACHMENT_MISSING_TYPE],
            ValueError('Error while parsing XML. Type attribute missing on attachment')
        )
      ]
    )
    def test_parse_test_attachment_raises_expected_exception(self, file_content: str, expected_exception: ValueError) -> None:
        with pytest.raises(ValueError) as value_error_exception:
            Allure1XMLParser.parse(file_content)
            
        assert expected_exception.args == value_error_exception.value.args

    @pytest.mark.parametrize(
      "file_content, expected_exception",
      [
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_PARAMETER_MISSING_NAME],
            ValueError('Error while parsing XML. Name attribute missing on parameter')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_PARAMETER_MISSING_VALUE],
            ValueError('Error while parsing XML. Value attribute missing on parameter')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_PARAMETER_MISSING_KIND],
            ValueError('Error while parsing XML. Kind attribute missing on parameter')
        ),
        (
            ALLURE_TEST_MOCKS[AllureTestMocks.TEST_PARAMETER_WRONG_KIND],
            ValueError('Error while parsing XML. Parameter kind is not recognized')
        )
      ]
    )
    def test_parse_test_parameter_raises_expected_exception(self, file_content: str, expected_exception: ValueError) -> None:
        with pytest.raises(ValueError) as value_error_exception:
            Allure1XMLParser.parse(file_content)
            
        assert expected_exception.args == value_error_exception.value.args