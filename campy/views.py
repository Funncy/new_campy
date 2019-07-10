from django.shortcuts import render

## 실 사용 list
def index(request):
    return render(request, 'test.html', {})