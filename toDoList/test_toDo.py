import unittest
from unittest.mock import patch
from toDo import display_tasks
from toDo import add_tasks
from toDo import update_task


class TestToDo(unittest.TestCase):

    def test_display_task(self):
        with open('tasks.txt', 'w') as task:
            task.write('Task 1')

        taskDisplayed = display_tasks('tasks.txt')

        expected_tasks = 'Task 1'
        self.assertEqual(taskDisplayed, expected_tasks)

    @patch('builtins.input', side_effect=['Buy groceries'])
    def test_add_task(self, mock_input):

        test_file = 'tasks.txt'
        add_tasks(test_file)

        with open(test_file, 'r') as task:
            content = task.read().strip()

        expected_content = 'Buy groceries'
        self.assertEqual(content, expected_content)

    @patch('builtins.input', side_effect=['1', 'Buy groceries and milk'])
    def test_update_task(self, mock_input):
        test_file = 'test_tasks.txt'
        with open(test_file, 'w') as file:
            file.write("Buy groceries\nTask 2\nTask 3")

        update_task(test_file)

        with open(test_file, 'r') as file:
            content = file.read().strip()

        expected_content = 'Buy groceries and milk\nTask 2\nTask 3'
        self.assertEqual(content, expected_content)


if __name__ == '__main__':
    unittest.main()
