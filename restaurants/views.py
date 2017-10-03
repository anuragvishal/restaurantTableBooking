from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework.response import Response

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def list(self, request):
        if request.GET.get('a') and request.GET.get('b'):
            if request.GET['a']=='location' and request.GET['b']:
                queryset = Restaurant.objects.filter(location=request.GET['b'])
                serializer_class = RestaurantSerializer
                serialzzdedata = RestaurantSerializer(queryset, many=True)
                return Response({
                                'message': 'hello world',
                                'data': serialzzdedata.data
                            })

            if request.GET['a']=='name' and request.GET['b']:
                queryset = Restaurant.objects.filter(name__icontains=request.GET['b'])
                serializer_class = RestaurantSerializer
                serialzzdedata = RestaurantSerializer(queryset, many=True)
                return Response({
                                'message': 'hello world',
                                'data': serialzzdedata.data
                            })


            if request.GET['a']=='cuisine' and request.GET['b']:
                queryset = Restaurant.objects.filter(cuisine=request.GET['b'])
                serializer_class = RestaurantSerializer
                serialzzdedata = RestaurantSerializer(queryset, many=True)
                return Response({
                                'message': 'hello world',
                                'data': serialzzdedata.data
                            })

        else:
            serialzzdedata = RestaurantSerializer(self.queryset, many=True)
            return Response({
                            'message': 'hello world',
                            'data': serialzzdedata.data
                        })
