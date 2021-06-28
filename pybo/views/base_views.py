
from ..models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Count

def index(request):
    """
    파이보 목록 출력
    """
    3/0 #강제로 오류 발생시키기
    # 입력 파라미터
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    # 조회
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer',
                                                                                                   '-create_date')
    else: #recent
        question_list = Question.objects.order_by('-create_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)  # primary key
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
    # return HttpResponse("안녕하세요 Pybo에 오신것을 환영합니다.")
