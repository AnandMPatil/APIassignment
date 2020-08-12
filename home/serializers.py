from rest_framework import serializers
from .models import Article, ActivityPeriods, Members


class ActivityPeriodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = ['start_time', 'end_time']


class MembersSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodsSerializer(many=True)

    class Meta:
        model = Members
        fields = ['id', 'real_name', 'tz', 'activity_periods']

    def create(self, validated_data):
        activity_periods_data = validated_data.pop('activity_periods')
        members = Members.objects.create(**validated_data)
        for activity_data in activity_periods_data:
            ActivityPeriods.objects.create(members=members, **activity_data)
        return members


class ArticleSerializer(serializers.ModelSerializer):
    activityPeriods = ActivityPeriodsSerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'activityPeriods']


class ArticleSerializer1(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        # Create and return a new `Article` instance, given the validated data.
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        # Update and return an existing `Article` instance, given the validated data.

        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
