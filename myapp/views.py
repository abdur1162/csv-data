from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from .models import Appointment
from .serializers import AppointmentSerializer
import csv
import io

class AppointmentView(generics.GenericAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        """Retrieve all appointments"""
        appointments = Appointment.objects.all()
        serializer = self.serializer_class(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new appointment or upload CSV"""
        if 'file' in request.FILES:
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                return Response({'error': 'Only CSV files are allowed'}, status=status.HTTP_400_BAD_REQUEST)

            data_set = csv_file.read().decode('utf-8')
            io_string = io.StringIO(data_set)
            reader = csv.reader(io_string)
            next(reader)  # Skip header

            for row in reader:
                Appointment.objects.create(
                    date=row[0],
                    time=row[1],
                    full_name=row[2],
                    location_description=row[3],
                    mrn=row[4],
                    appointment_description=row[5],
                    appointment_comment=row[6],
                    appointment_type=row[7],
                    customize_date=row[8],
                    default_division=row[9],
                    location_region=row[10],
                    location_type=row[11],
                    main_appt=row[12],
                    phressia_filter=row[13],
                    provider_type_group=row[14],
                    quality_specialty=row[15],
                    walk_in_filter=row[16],
                    appt_scheduled_by=row[17],
                    provider_type=row[18]
                )

            return Response({'message': 'CSV uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """Update an existing appointment"""
        appointment = get_object_or_404(Appointment, pk=pk)
        serializer = self.serializer_class(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
