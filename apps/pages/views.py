from django.shortcuts import render
from django.core.paginator import Paginator

SAMPLE_CARDS = [
    {
        "name": "Aziz Karimov",
        "profession": "Shifokor-kardiolog",
        "location": "Toshkent shahri, Chilonzor tumani",
        "description": "10 yillik tajribaga ega. Yurak-qon tomir kasalliklari bo‘yicha maslahat va davolash.",
    },
    {
        "name": "Namuna Soft MChJ",
        "profession": "Dasturiy ta’minot ishlab chiqish",
        "location": "Samarqand viloyati, Samarqand shahri",
        "description": "Veb-saytlar, mobil ilovalar va avtomatlashtirish tizimlari yaratamiz.",
    },
    {
        "name": "Dilnoza Rahimova",
        "profession": "Advokat",
        "location": "Buxoro viloyati, Buxoro shahri",
        "description": "Fuqarolik va tadbirkorlik huquqi bo‘yicha yuridik yordam va maslahat.",
    },
    {
        "name": "Bobur Yusupov",
        "profession": "IT mutaxassisi, backend dasturchi",
        "location": "Toshkent shahri, Yunusobod tumani",
        "description": "Django va PostgreSQL asosida veb-ilovalar yaratish, mavjud loyihalarni qo‘llab-quvvatlash.",
    },
    {
        "name": "Sog‘lom Hayot klinikasi",
        "profession": "Xususiy tibbiyot markazi",
        "location": "Toshkent shahri, Mirzo Ulug‘bek tumani",
        "description": "Terapevt, nevrolog va pediatr qabullari, laboratoriya tahlillari.",
    },
    {
        "name": "Malika Tursunova",
        "profession": "Grafik dizayner",
        "location": "Samarqand viloyati, Kattaqo‘rg‘on shahri",
        "description": "Logotip, vizitka va ijtimoiy tarmoqlar uchun dizayn tayyorlash.",
    },
    {
        "name": "Huquq Markazi MChJ",
        "profession": "Yuridik xizmatlar",
        "location": "Buxoro viloyati, G‘ijduvon tumani",
        "description": "Tadbirkorlar uchun shartnomalar, ro‘yxatdan o‘tkazish va huquqiy maslahat.",
    },
    {
        "name": "Sardor Alimov",
        "profession": "Shifokor-stomatolog",
        "location": "Toshkent shahri, Shayxontohur tumani",
        "description": "Tish davolash, protezlash va bolalar stomatologiyasi.",
    },
]


def home(request):
        return render(request, "pages/home.html", {"cards": SAMPLE_CARDS[:3]})


def catalog(request):
    paginator = Paginator(SAMPLE_CARDS, 6)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "pages/catalog.html",
        {"page_obj": page_obj, "total": paginator.count},
    )