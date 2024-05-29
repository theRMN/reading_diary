from datetime import datetime
from rest_framework import serializers

from .models import Book, Note


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'goal_state',)


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ('date', 'time',)

    def create(self, validated_data):
        book = Book.objects.get(id=validated_data.get('book').id)
        request = self.context.get('request', None)
        user_settings_pages = request.user.user_settings.expected_pages_per_day
        objects = Note.objects.filter(date=datetime.now().date())
        pages = sum([o.num_pages for o in objects])
        total_pages = pages + validated_data.get('num_pages')

        if total_pages >= user_settings_pages:
            book.goal_state = True
            book.save()
        else:
            book.goal_state = False
            book.save()

        return super().create(validated_data)
