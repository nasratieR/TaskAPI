from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import TasksModel


class TasksViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='adminTest', email='admintest@test.com')
        self.user.set_password('azerty123456')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.task_data = {
            'name': 'Test task Title',
            'description': 'Test Task Content',
        }

        self.test_task = TasksModel.objects.create(author=self.user, **self.task_data)

    def test_list_tasks(self):
        response = self.client.get('/tasks/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertGreater(len(response.data), 0)

    def test_create_task_authenticated_user(self):
        response = self.client.post('/tasks/', self.task_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(TasksModel.objects.count(), 2)

        self.assertEqual(TasksModel.objects.last().description, 'Test Task Content')

    def test_retrieve_task(self):
        response = self.client.get(f'/tasks/{self.test_task.id}/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.data['description'], 'Test Task Content')

    def test_partial_update_task_authenticated_user(self):
        updated_data = {'description': 'Updated Test Task Content'}
        response = self.client.patch(f'/tasks/{self.test_task.id}/', updated_data, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.test_task.refresh_from_db()
        self.assertEquals(self.test_task.description, 'Updated Test Task Content')

    def test_destroy_task_authenticated_user(self):
        response = self.client.delete(f'/tasks/{self.test_task.id}/')

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(TasksModel.DoesNotExist):
            TasksModel.objects.get(id=self.test_task.id)

    def test_destroy_tasks_nonexistent(self):
        response = self.client.delete('/tasks/9999/')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)


