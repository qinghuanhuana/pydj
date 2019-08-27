from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from PIL import Image, ImageDraw, ImageFont
import io, random

# Create your views here.

def get_valid_img(request):
    def get_random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    img_obj = Image.new('RGB', (220, 35), get_random_color())
    draw_obj = ImageDraw.Draw(img_obj)
    font_obj = ImageFont.truetype('C:\\Windows\\Fonts\\simsun.ttc', 28)
    tmp_list = []
    for i in range(5):
        u = chr(random.randint(65, 90))
        l = chr(random.randint(97, 122))
        n = str(random.randint(0, 9))
        tmp = random.choice([u, l, n])
        tmp_list.append(tmp)
        draw_obj.text((20 + 40 * i, 0), tmp, fill=get_random_color(), font=font_obj)
    request.session['valid_code'] = ''.join(tmp_list)
    width = 200
    height = 35
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw_obj.line((x1, x2, y1, y2), fill=get_random_color())
    for i in range(40):
        draw_obj.point((random.randint(0, width), random.randint(0, height)), fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw_obj.arc((x, y, x+4, y+4), 0, 90, fill=get_random_color())
    io_obj = io.BytesIO()
    img_obj.save(io_obj, 'png')
    data = io_obj.getvalue()
    return HttpResponse(data)

def index(request):
    return render(request, 'index.html')

def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        check_code = request.POST.get('checkcode')
        session_code = request.session['valid_code']
        if check_code.strip().lower() != session_code.lower():
            return render(request, 'index.html', {'error': 'code error'})
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/event_manage/')
            return response
        # if username == 'admin' and password == 'admin123':
        #     response = HttpResponseRedirect('/event_manage/')
        #     # response.set_cookie('user', username, 3600 )
        #     request.session['user'] = username
        #     return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
    else:
        return render(request, 'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user":username,
                                                 "events": event_list})

@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username,
                                                 "events": event_list})

@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username,
                                                 "guests": contacts})

@login_required
def search_phone(request):
    username = request.session.get('user', '')
    search_phone = request.GET.get('phone', '')
    guest_list = Guest.objects.filter(Q(realname__contains=search_phone) | Q(phone__contains=search_phone))
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username,
                                                 "guests": contacts})

@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response

@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})

@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone', '')
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': 'phone error.'})

    result = Guest.objects.filter(phone=phone, event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': 'event id or phone error.'})

    result = Guest.objects.get(phone=phone, event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': 'user has sign in.'})
    else:
        Guest.objects.filter(phone=phone, event_id=event_id).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': 'sign in success!',
                                                   'guest': result})

