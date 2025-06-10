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
from datetime import datetime
from typing import List, Optional
from typing_extensions import Self

class TestCaseBuilder:
    __test_case: TestCase

    def __init__(self):
        self.__test_case = TestCase()

    def set_start_time(self, start_time: datetime) -> Self:
        self.__test_case.start_time = start_time
        return self
    
    def set_end_time(self, end_time: datetime) -> Self:
        self.__test_case.end_time = end_time
        return self
    
    def set_status(self, status: TestStatus) -> Self:
        self.__test_case.status = status
        return self
    
    def set_name(self, name: str) -> Self:
        self.__test_case.name = name
        return self
    
    def set_title(self, title: Optional[str]) -> Self:
        self.__test_case.title = title
        return self
    
    def set_description(self, description: Optional[str]) -> Self:
        self.__test_case.description = description
        return self
    
    def set_failure(self, failure: Optional[TestFailure]) -> Self:
        self.__test_case.failure = failure
        return self

    def set_steps(self, steps: Optional[List[TestStep]]) -> Self:
        self.__test_case.steps = steps
        return self

    def set_attachments(self, attachments: Optional[List[TestAttachment]]) -> Self:
        self.__test_case.attachments = attachments
        return self

    def set_labels(self, labels: Optional[List[TestLabel]]) -> Self:
        self.__test_case.labels = labels
        return self
    
    def set_parameters(self, parameters: Optional[List[TestParameter]]):
        self.__test_case.parameters = parameters
        return self   
    
    def get_element(self) -> TestCase:
        return self.__test_case

class TestLabelBuilder:
    __test_label: TestLabel

    def __init__(self):
        self.__test_label = TestLabel()
   
    def set_name(self, name: str) -> Self:
        self.__test_label.name = name
        return self
    
    def set_value(self, value: str) -> Self:
        self.__test_label.value = value
        return self
    
    def get_element(self) -> TestLabel:
        return self.__test_label
    
class TestParameterBuilder:
    __test_parameter: TestParameter

    def __init__(self):
        self.__test_parameter = TestParameter()
    
    def set_name(self, name: str) -> Self:
        self.__test_parameter.name = name
        return self
    
    def set_value(self, value: str) -> Self:
        self.__test_parameter.value = value
        return self
    
    def set_kind(self, kind: TestParameterKind) -> Self:
        self.__test_parameter.kind = kind
        return self
    
    def get_element(self) -> TestParameter:
        return self.__test_parameter
    
class TestStepBuilder:
    __test_step: TestStep

    def __init__(self):
        self.__test_step = TestStep()
   
    def set_start_time(self, start_time: datetime) -> Self:
        self.__test_step.start_time = start_time
        return self
    
    def set_end_time(self, end_time: datetime) -> Self:
        self.__test_step.end_time = end_time
        return self
    
    def set_status(self, status: TestStatus) -> Self:
        self.__test_step.status = status
        return self
    
    def set_name(self, name: str) -> Self:
        self.__test_step.name = name
        return self
    
    def set_title(self, title: Optional[str]) -> Self:
        self.__test_step.title = title
        return self
    
    def set_attachments(self, attachments: Optional[List[TestAttachment]]) -> Self:
        self.__test_step.attachments = attachments
        return self
    
    def set_steps(self, steps: Optional[List[TestStep]]) -> Self:
        self.__test_step.steps = steps
        return self

    def get_element(self) -> TestStep:
        return self.__test_step
    
class TestSuiteBuilder:
    __test_suite: TestSuite

    def __init__(self):
        self.__test_suite = TestSuite()

    def set_start_time(self, start_time: datetime) -> Self:
        self.__test_suite.start_time = start_time
        return self
    
    def set_end_time(self, end_time: datetime) -> Self:
        self.__test_suite.end_time = end_time
        return self
    
    def set_version(self, version: Optional[str]) -> Self:
        self.__test_suite.version = version
        return self
    
    def set_name(self, name: str) -> Self:
        self.__test_suite.name = name
        return self
    
    def set_title(self, title: Optional[str]) -> Self:
        self.__test_suite.title = title
        return self
    
    def set_description(self, description: Optional[str]) -> Self:
        self.__test_suite.description = description
        return self
    
    def set_test_cases(self, test_cases: Optional[List[TestCase]]) -> Self:
        self.__test_suite.test_cases = test_cases
        return self
    
    def set_labels(self, labels: Optional[List[TestLabel]]) -> Self:
        self.__test_suite.labels = labels
        return self
    
    def get_element(self) -> TestSuite:
        return self.__test_suite
    
class TestStepBuilder:
    __test_step: TestStep

    def __init__(self):
        self.__test_step = TestStep()
   
    def set_start_time(self, start_time: datetime) -> Self:
        self.__test_step.start_time = start_time
        return self
    
    def set_end_time(self, end_time: datetime) -> Self:
        self.__test_step.end_time = end_time
        return self
    
    def set_status(self, status: TestStatus) -> Self:
        self.__test_step.status = status
        return self
    
    def set_name(self, name: str) -> Self:
        self.__test_step.name = name
        return self
    
    def set_title(self, title: Optional[str]) -> Self:
        self.__test_step.title = title
        return self
    
    def set_attachments(self, attachments: Optional[List[TestAttachment]]) -> Self:
        self.__test_step.attachments = attachments
        return self
    
    def set_steps(self, steps: Optional[List[TestStep]]) -> Self:
        self.__test_step.steps = steps
        return self

    def get_element(self) -> TestStep:
        return self.__test_step
    
class TestAttachmentBuilder:
    __test_attachment: TestAttachment

    def __init__(self):
        self.__test_attachment = TestAttachment()

    def set_title(self, title: str) -> Self:
        self.__test_attachment.title = title
        return self
    
    def set_source(self, source: str) -> Self:
        self.__test_attachment.source = source
        return self
    
    def set_type(self, type: str) -> Self:
        self.__test_attachment.type = type
        return self
    
    def get_element(self) -> TestAttachment:
        return self.__test_attachment
    
class TestFailureBuilder:
    __test_failure: TestFailure

    def __init__(self):
        self.__test_failure = TestFailure()

    def set_message(self, message: str) -> Self:
        self.__test_failure.message = message
        return self
    
    def set_stack_trace(self, stack_trace: Optional[str]) -> Self:
        self.__test_failure.stack_trace = stack_trace
        return self
    
    def get_element(self) -> TestFailure:
        return self.__test_failure