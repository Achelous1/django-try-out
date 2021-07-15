from django.shortcuts import render


# View가 Django에서는 MVC의 Controller를 담당한다

def post_list(request):
    return render(request, 'blog/post_list.html')