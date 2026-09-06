from django.core.management.base import BaseCommand
from faker import Faker
from hangarin.models import Task, Priority, Category, Note, SubTask
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_task(10)
        self.create_subtask(10)
        self.create_note(10)

    def create_task(self, num_tasks):
        fake = Faker()
        for i in range(num_tasks):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                category=Category.objects.order_by('?').first(),
                priority=Priority.objects.order_by('?').first()
            )

    def create_subtask(self, num_subtasks):
        fake = Faker()
        for i in range(num_subtasks):
            parent_task = Task.objects.order_by('?').first()
            if parent_task:
                SubTask.objects.create(
                    parent_task=parent_task,
                    sub_title=fake.sentence(nb_words=5),
                    sub_status=fake.random_element(elements=["Pending", "In Progress", "Completed"])
                )
    
    def create_note(self, num_notes):
        fake = Faker()
        for i in range(num_notes):
            note_task = Task.objects.order_by('?').first()
            if note_task:
                Note.objects.create(
                    note_task=note_task,
                    content=fake.paragraph(nb_sentences=3)
                )