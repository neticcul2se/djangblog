from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Hello(request):
    rating=3
    tags = ['น้ำตก', 'ธรรมชาติ', 'หน้าฝน', 'ตากหมอก']
    return render(request, 'index.html', {'name': 'บทความท่องเที่ยว', 'author': 'wachira','tags': tags,'rating':rating})
def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'form.html')