from dataclasses import field
from pkg_resources import require
from rest_framework import serializers
from .models import Task, SubTask, SubSubTask


class SubSubTaskSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = SubSubTask


class SubTaskSerializer(serializers.ModelSerializer):
    subsubtask = SubSubTaskSerializer(many=True, required=False)

    class Meta:
        fields = "__all__"
        model = SubTask


class TaskSerializer(serializers.ModelSerializer):
    subtask = SubTaskSerializer(many=True, required=False)

    class Meta:
        fields = "__all__"
        model = Task

    def create(self, validated_data):
        sub_tasks = validated_data.pop(
            'subtask') if 'subtask' in validated_data else None

        t = Task.objects.create(**validated_data)

        if sub_tasks:
            for task in sub_tasks:
                sub_sub_tasks = task.pop(
                    'subsubtask') if 'subsubtask' in task else None
                subtask = SubTask.objects.create(task=t, **task)
                if sub_sub_tasks:
                    for task in sub_sub_tasks:
                        SubSubTask.objects.create(task=subtask, **task)
        return t
