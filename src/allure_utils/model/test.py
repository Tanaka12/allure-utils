from datetime import datetime
from enum import Enum
from typing import List, Optional
from typing_extensions import Self

class TestStatus(str, Enum):
    failed = "failed"
    broken = "broken"
    passed = "passed"
    canceled = "canceled"
    pending = "pending"

class TestAttachment:
    title: str
    source: str
    type: str
    
    def __init__(self):
        self.title = ""
        self.source = ""
        self.type = ""

    def __eq__(self, other: Self) -> bool:
        if self.title == other.title \
           and self.source == other.source \
           and self.type == other.type:
            return True
        
        return False

class TestParameterKind(str, Enum):
    argument = "argument"
    system_property = "system-property"
    environment_variable = "environment-variable"

class TestFailure:
    message: str
    stack_trace: Optional[str]

    def __init__(self):
        self.message = ""
        self.stack_trace = None

    def __eq__(self, other: Self) -> bool:
        if self.message == other.message \
           and self.stack_trace == other.stack_trace:
            return True
        
        return False

class TestStep:
    start_time: datetime
    end_time: datetime
    status: TestStatus
    name: str
    title: Optional[str]
    attachments: Optional[List[TestAttachment]]
    steps: Optional[List[Self]]

    def __init__(self):
        self.start_time = datetime.fromtimestamp(0)
        self.end_time = datetime.fromtimestamp(0)
        self.status = TestStatus.failed
        self.name = ""
        self.title = None
        self.attachments = None
        self.steps = None

    def __eq__(self, other: Self) -> bool:
        if self.start_time == other.start_time \
           and self.end_time == other.end_time \
           and self.status == other.status \
           and self.name == other.name \
           and self.title == other.title \
           and self.attachments == other.attachments \
           and self.steps == other.steps:
            return True
        
        return False

class TestLabel:
    name: str
    value: str

    def __init__(self):
        self.name = ""
        self.value = ""

    def __eq__(self, other: Self) -> bool:
        if self.name == other.name \
           and self.value == other.value:
            return True
        
        return False

class TestParameter:
    name: str
    value: str
    kind: TestParameterKind

    def __init__(self):
        self.name = ""
        self.value = ""
        self.kind = TestParameterKind.argument

    def __eq__(self, other: Self) -> bool:
        if self.name == other.name \
           and self.value == other.value \
           and self.kind == other.kind:
            return True
        
        return False

class TestCase:
    start_time: datetime
    end_time: datetime
    status: TestStatus
    name: str
    title: Optional[str]
    description: Optional[str]
    failure: Optional[TestFailure]
    steps: Optional[List[TestStep]]
    attachments: Optional[List[TestAttachment]]
    labels: Optional[List[TestLabel]]
    parameters: Optional[List[TestParameter]]

    def __init__(self):
        self.start_time = datetime.fromtimestamp(0)
        self.end_time = datetime.fromtimestamp(0)
        self.status = TestStatus.failed
        self.name = ""
        self.title = None
        self.description = None
        self.failure = None
        self.steps = None
        self.attachments = None
        self.labels = None
        self.parameters = None

    def __eq__(self, other: Self) -> bool:
        if self.start_time == other.start_time \
           and self.end_time == other.end_time \
           and self.status == other.status \
           and self.name == other.name \
           and self.title == other.title \
           and self.description == other.description \
           and self.failure == other.failure \
           and self.steps == other.steps \
           and self.attachments == other.attachments \
           and self.labels == other.labels \
           and self.parameters == other.parameters:
            return True
        
        return False

class TestSuite:
    start_time: datetime
    end_time: datetime
    version: Optional[str]
    name: str
    title: Optional[str]
    description: Optional[str]
    test_cases: Optional[List[TestCase]]
    labels: Optional[List[TestLabel]]

    def __init__(self):
        self.start_time = datetime.fromtimestamp(0)
        self.end_time = datetime.fromtimestamp(0)
        self.name = ""
        self.version = None
        self.title = None
        self.description = None
        self.test_cases = None
        self.labels = None

    def __eq__(self, other: Self) -> bool:
        if self.start_time == other.start_time \
           and self.end_time == other.end_time \
           and self.version == other.version \
           and self.name == other.name \
           and self.title == other.title \
           and self.description == other.description \
           and self.test_cases == other.test_cases \
           and self.labels == other.labels:
            return True
        
        return False