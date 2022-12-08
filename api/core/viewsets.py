from rest_framework import permissions
from .serializers import OutliersProbabilitySerializer, GetOutliersProbabilitySerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from drf_yasg.utils import swagger_auto_schema

class CreateOutlierProbabilityViewset(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=OutliersProbabilitySerializer)
    def post(self, request):
        serializer = OutliersProbabilitySerializer(data=request.data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                cursor.execute("SELECT EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=%s)", (f"{serializer.data['project_name']}_{serializer.data['table_name']}",))
                exist_database_table = cursor.fetchone()[0]
                if not exist_database_table:
                    create_table = f'''CREATE TABLE "{serializer.data['project_name']}_{serializer.data['table_name']}"(
                                                    time TIMESTAMP(0),
                                                    id INT,
                                                    outlier_prob FLOAT);'''
                    cursor.execute(create_table)
                insert_data = f'''INSERT INTO "{serializer.data['project_name']}_{serializer.data['table_name']}" \
                            (time, id, outlier_prob) VALUES(NOW(),{serializer.data['outlier'].split()[0]},{serializer.data['outlier'].split()[1]})'''
                cursor.execute(insert_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListOutliersProbabilityViewset(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        project_name = kwargs['project_name']
        table_name =  kwargs['table_name']
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'''SELECT * FROM "{project_name}_{table_name}"''')
                project_data = cursor.fetchall()
                outliers = GetOutliersProbabilitySerializer(project_data, many=True)
            return Response(outliers.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)