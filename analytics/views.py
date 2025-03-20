from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.decorators import api_view
from weather_data.models import WeatherData




@api_view(['GET'])
def average_temperature_view(request):
    avg_value = WeatherData.objects.aggregate(average_temperature=Avg('temperature'))
    return Response(avg_value)


