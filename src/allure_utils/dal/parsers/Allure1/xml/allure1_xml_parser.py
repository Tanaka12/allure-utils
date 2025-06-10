from datetime import datetime
from allure_utils.model.test import \
(
    TestAttachment,
    TestCase, 
    TestFailure,
    TestLabel,
    TestParameter,
    TestParameterKind,
    TestStatus,
    TestStep,
    TestSuite
)
import xml.etree.ElementTree as ET

class Allure1XMLParser:

    @staticmethod
    def parse(content: str) -> TestSuite:
        test_suite = TestSuite()

        root_element: ET.Element
        try:
            root_element = ET.fromstring(content)
        except:
            raise ValueError('Error while parsing XML. Wrong format')
        
        if root_element.tag != '{urn:model.allure.qatools.yandex.ru}test-suite':
            raise ValueError('Error while parsing XML. Wrong format')
            
        root_element_attribs = root_element.attrib
        if 'start' not in root_element_attribs:
            raise ValueError('Error while parsing XML. Start attribute missing on test-suite')
        
        test_suite.start_time = datetime.fromtimestamp(int(root_element_attribs['start']))
        
        if 'stop' not in root_element_attribs:
            raise ValueError('Error while parsing XML. Stop attribute missing on test-suite')
        
        test_suite.end_time = datetime.fromtimestamp(int(root_element_attribs['stop']))
        
        if 'version' in root_element_attribs:
            test_suite.version = root_element_attribs['version']

        test_suite_name_element = root_element.find('name')
        if test_suite_name_element is None:
            raise ValueError('Error while parsing XML. Name element missing on test-suite')
        
        test_suite.name = test_suite_name_element.text

        test_suite_title_element = root_element.find('title')
        if test_suite_title_element is not None:
            test_suite.title = test_suite_title_element.text

        test_suite_description_element = root_element.find('description')
        if test_suite_description_element is not None:
            test_suite.description = test_suite_description_element.text

        test_cases_element = root_element.find('test-cases')
        if test_cases_element is not None:
            test_suite.test_cases = []
            for test_case_element in test_cases_element.findall('test-case'):
                test_suite.test_cases.append(Allure1XMLParser.__parse_test_case(test_case_element))

        test_suite_labels_element = root_element.find('labels')
        if test_suite_labels_element is not None:
            test_suite.labels = []
            for test_suite_label_element in test_suite_labels_element.findall('label'):
                test_suite.labels.append(Allure1XMLParser.__parse_test_label(test_suite_label_element))

        return test_suite

    @staticmethod
    def __parse_test_case(test_case_element: ET.Element) -> TestCase:
        test_case = TestCase()

        test_case_element_attribs = test_case_element.attrib
        if 'start' not in test_case_element_attribs:
            raise ValueError('Error while parsing XML. Start attribute missing on test-case')
        
        test_case.start_time = datetime.fromtimestamp(int(test_case_element_attribs['start']))
        
        if 'stop' not in test_case_element_attribs:
            raise ValueError('Error while parsing XML. Stop attribute missing on test-case')
        
        test_case.end_time = datetime.fromtimestamp(int(test_case_element_attribs['stop']))

        if 'status' not in test_case_element_attribs:
            raise ValueError('Error while parsing XML. Status attribute missing on test-case')
        
        test_case.status = Allure1XMLParser.__parse_test_status(test_case_element_attribs['status'])

        test_case_name_element = test_case_element.find('name')
        if test_case_name_element is None:
            raise ValueError('Error while parsing XML. Name element missing on test-case')
        
        test_case.name = test_case_name_element.text

        test_case_title_element = test_case_element.find('title')
        if test_case_title_element is not None:
            test_case.title = test_case_title_element.text

        test_case_description_element = test_case_element.find('description')
        if test_case_description_element is not None:
            test_case.description = test_case_description_element.text

        test_case_failure_element = test_case_element.find('failure')
        if test_case_failure_element is not None:
            test_case.failure = Allure1XMLParser.__parse_test_failure(test_case_failure_element)

        test_case_steps_element = test_case_element.find('steps')
        if test_case_steps_element is not None:
            test_case.steps = []
            for test_case_step_element in test_case_steps_element.findall('step'):
                test_case.steps.append(Allure1XMLParser.__parse_test_step(test_case_step_element))

        test_case_attachments_element = test_case_element.find('attachments')
        if test_case_attachments_element is not None:
            test_case.attachments = []
            for test_case_attachment_element in test_case_attachments_element.findall('attachment'):
                test_case.attachments.append(Allure1XMLParser.__parse_test_attachment(test_case_attachment_element))

        test_case_labels_element = test_case_element.find('labels')
        if test_case_labels_element is not None:
            test_case.labels = []
            for test_case_label_element in test_case_labels_element.findall('label'):
                test_case.labels.append(Allure1XMLParser.__parse_test_label(test_case_label_element))

        test_case_parameters_element = test_case_element.find('parameters')
        if test_case_parameters_element is not None:
            test_case.parameters = []
            for test_case_parameter_element in test_case_parameters_element.findall('parameter'):
                test_case.parameters.append(Allure1XMLParser.__parse_test_parameter(test_case_parameter_element))

        return test_case
    
    @staticmethod
    def __parse_test_step(step_element: ET.Element) -> TestStep:
        test_step = TestStep()
        
        test_step_element_attribs = step_element.attrib
        if 'start' not in test_step_element_attribs:
            raise ValueError('Error while parsing XML. Start attribute missing on step')
        
        test_step.start_time = datetime.fromtimestamp(int(test_step_element_attribs['start']))
        
        if 'stop' not in test_step_element_attribs:
            raise ValueError('Error while parsing XML. Stop attribute missing on step')
        
        test_step.end_time = datetime.fromtimestamp(int(test_step_element_attribs['stop']))

        if 'status' not in test_step_element_attribs:
            raise ValueError('Error while parsing XML. Status attribute missing on step')
        
        test_step.status = Allure1XMLParser.__parse_test_status(test_step_element_attribs['status'])

        test_step_name_element = step_element.find('name')
        if test_step_name_element is None:
            raise ValueError('Error while parsing XML. Name element missing on step')
        
        test_step.name = test_step_name_element.text

        test_step_title_element = step_element.find('title')
        if test_step_title_element is not None:
            test_step.title = test_step_title_element.text

        test_step_attachments_element = step_element.find('attachments')
        if test_step_attachments_element is not None:
            test_step.attachments = []
            for test_step_attachment_element in test_step_attachments_element.findall('attachment'):
                test_step.attachments.append(Allure1XMLParser.__parse_test_attachment(test_step_attachment_element))

        test_step_steps_element = step_element.find('steps')
        if test_step_steps_element is not None:
            test_step.steps = []
            for test_step_step_element in test_step_steps_element.findall('step'):
                test_step.steps.append(Allure1XMLParser.__parse_test_step(test_step_step_element))

        return test_step

    @staticmethod
    def __parse_test_failure(failure_element: ET.Element) -> TestFailure:
        test_failure = TestFailure()

        test_failure_message_element = failure_element.find('message')
        if test_failure_message_element is None:
            raise ValueError('Error while parsing XML. Message element missing on failure')
        
        test_failure.message = test_failure_message_element.text

        test_failure_stack_trace_element = failure_element.find('stack-trace')
        if test_failure_stack_trace_element is not None:
            test_failure.stack_trace = test_failure_stack_trace_element.text
        
        return test_failure
    
    @staticmethod
    def __parse_test_parameter(parameter_element: ET.Element) -> TestParameter:
        test_parameter = TestParameter()

        parameter_element_attribs = parameter_element.attrib
        if 'name' not in parameter_element_attribs:
            raise ValueError('Error while parsing XML. Name attribute missing on parameter')
        
        test_parameter.name = parameter_element_attribs['name']

        if 'value' not in parameter_element_attribs:
            raise ValueError('Error while parsing XML. Value attribute missing on parameter')
        
        test_parameter.value = parameter_element_attribs['value']

        if 'kind' not in parameter_element_attribs:
            raise ValueError('Error while parsing XML. Kind attribute missing on parameter')
        
        test_parameter.kind = Allure1XMLParser.__parse_test_parameter_kind(parameter_element_attribs['kind'])

        return test_parameter

    @staticmethod
    def __parse_test_parameter_kind(parameter_kind: str) -> TestParameterKind:
        if parameter_kind == 'argument':
            return TestParameterKind.argument
        
        if parameter_kind == 'system-property':
            return TestParameterKind.system_property
        
        if parameter_kind == 'environment-variable':
            return TestParameterKind.environment_variable
        
        raise ValueError('Error while parsing XML. Parameter kind is not recognized')

    @staticmethod
    def __parse_test_attachment(attachment_element: ET.Element) -> TestAttachment:
        test_attachment = TestAttachment()

        attachment_element_attribs = attachment_element.attrib
        if 'title' not in attachment_element_attribs:
            raise ValueError('Error while parsing XML. Title attribute missing on attachment')
        
        test_attachment.title = attachment_element_attribs['title']
        
        if 'source' not in attachment_element_attribs:
            raise ValueError('Error while parsing XML. Source attribute missing on attachment')
        
        test_attachment.source = attachment_element_attribs['source']

        if 'type' not in attachment_element_attribs:
            raise ValueError('Error while parsing XML. Type attribute missing on attachment')       

        test_attachment.type = attachment_element_attribs['type']

        return test_attachment

    @staticmethod
    def __parse_test_status(status: str) -> TestStatus:
        if status == 'failed':
            return TestStatus.failed
        
        if status == 'broken':
            return TestStatus.broken
        
        if status == 'passed':
            return TestStatus.passed
        
        if status == 'canceled':
            return TestStatus.canceled
        
        if status == 'pending':
            return TestStatus.pending
        
        raise ValueError('Error while parsing XML. Status is not recognized')

    @staticmethod
    def __parse_test_label(label_element: ET.Element) -> TestLabel:
        test_label = TestLabel()
        
        label_element_attribs = label_element.attrib
        if 'name' not in label_element_attribs:
            raise ValueError('Error while parsing XML. Name attribute missing on label')
        
        test_label.name = label_element_attribs['name']

        if 'value' not in label_element_attribs:
            raise ValueError('Error while parsing XML. Value attribute missing on label')
        
        test_label.value = label_element_attribs['value']

        return test_label


        

        