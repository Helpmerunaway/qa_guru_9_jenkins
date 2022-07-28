from selene.core.entity import Element
from selene.core.wait import Command


def resource(path):
	from tests.demoqa_tests import test_register_students
	from pathlib import Path
	return str(Path(test_register_students.__file__).parent.parent.parent.joinpath(f'resources/{path}'))


def upload_resource(path: str) -> Command[Element]:
	def fn(element: Element):
		element.send_keys(resource(path))

	return Command(f'upload file from resources: {path}', fn)