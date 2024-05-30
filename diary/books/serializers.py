from datetime import datetime
from django.db.models import Sum
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
        book = validated_data.get('book')
        user_settings_pages = book.user.user_settings.expected_pages_per_day
        pages_sum = Note.objects.filter(date=datetime.now().date()).aggregate(Sum('num_pages')).get('num_pages__sum')
        total_pages = (pages_sum or 0) + validated_data.get('num_pages')

        if total_pages >= user_settings_pages:
            book.goal_state = True
            book.save()
        else:
            book.goal_state = False
            book.save()

        return super().create(validated_data)
