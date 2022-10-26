from django.shortcuts import render
from .utils import get_course_info_by_page
import csv 
from django.http import HttpResponse, HttpResponseNotFound

from django.views.decorators.csrf import csrf_exempt

data = []

@csrf_exempt
def search(request):
    global data 
    course = request.POST.get('search')
    total = None 
    try:
        total = int(request.POST.get('total'))
    except:
        total = 1
    data = []
    print("#",course, "#", total)
    visited_page = {}
    
    # if course and len(course) > 0:
    #     # data = get_course_info_by_page(total, course, visited_page)
    #     for i in range(1, total+1):
    #         try:
    #             data += get_course_info_by_page(i, course, visited_page)
    #         except:
    #             break
    if course and len(course) > 0:
        data = get_course_info_by_page(total, course, visited_page)

    context = {
        "data":data,
    }

    return render(request, "app_search/search.html", context=context)


def get_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    if len(data) == 0:
        return HttpResponseNotFound("Sorry, no Data")
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="course info.csv"'},
    )


    writer = csv.writer(response)
    writer.writerow(['Title', 'Description', 'Rating', 'Instructor', 'Provider', 'Students Enrolled', 'Course Link'])
    for i in range(len(data)):
        writer.writerow([data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]])

    return response