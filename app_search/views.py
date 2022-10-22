from django.shortcuts import render
from .utils import get_course_info_by_page

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def search(request):
    course = request.POST.get('search')
    total = None 
    try:
        total = int(request.POST.get('total'))
    except:
        total = 2
    data = []
    print("#",course, "#", total)
    visited_page = {}
    
    if course and len(course) > 0:
        data = get_course_info_by_page(total, course, visited_page)
    #     for i in range(1, total+1):
    #         try:
    #             data = get_course_info_by_page(i, course, visited_page)
    #         except:
    #             break

    context = {
        "data":data,
    }

    return render(request, "app_search/search.html", context=context)