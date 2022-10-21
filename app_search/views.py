from django.shortcuts import render
from .utils import get_course_info_by_page

def search(request):
    course = request.GET.get('search')
    total = None 
    try:
        total = int(request.GET.get('total'))
    except:
        total = 2
    data = []
    print("#",course, "#", total)
    visited_page = {}
    if len(course) > 0:
        for i in range(1, total+1):
            try:
                data += get_course_info_by_page(i, course, visited_page)
            except:
                break

    context = {
        "data":data,
    }

    return render(request, "app_search/search.html", context=context)