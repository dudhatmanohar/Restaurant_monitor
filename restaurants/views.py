from rest_framework.decorators import api_view
from rest_framework.response import Response
from restaurants.report import generate_report
from restaurants.report import report_is_ready


@api_view(['POST'])
def trigger_report(request):
    report_id = generate_report()
    return Response({"report_id": report_id})

@api_view(['GET'])
def get_report(request, report_id):
    if report_is_ready(report_id):  # Implement report_is_ready logic
        return Response({"status": "Complete", "csv_url": f"/path/to/report/{report_id}.csv"})
    else:
        return Response({"status": "Running"})

