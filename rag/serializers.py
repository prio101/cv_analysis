from rest_framework import serializers

class RagQuerySerializer(serializers.Serializer):
    query = serializers.CharField(required=True)
