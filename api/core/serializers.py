from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method

class   OutliersProbabilitySerializer(serializers.Serializer):
    project_name = serializers.CharField(max_length=100)
    table_name = serializers.CharField(max_length=100)
    outlier = serializers.CharField()

    def validate_outlier(self, value):
        outlier_list = value.split()
        if len(outlier_list) != 2:
            raise serializers.ValidationError({'data':["Format not allowed! This format '1 0.7' is required"]})
        return value


class GetOutliersProbabilitySerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    outlier = serializers.SerializerMethodField()

    def get_outlier(self, obj):
        return obj[2]

    def get_id(self, obj):
        return obj[1]
    