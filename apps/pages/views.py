from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

SAMPLE_CARDS = [
    {
        "slug": "aziz-karimov",
        "name": "Aziz Karimov",
        "profession": "Shifokor-kardiolog",
        "location": "Toshkent shahri, Chilonzor tumani",
        "description": "10 yillik tajribaga ega. Yurak-qon tomir kasalliklari bo‘yicha maslahat va davolash.",
        "about": "Kardiolog sifatida 10 yildan ortiq ishlab kelaman. Yurak-qon tomir kasalliklarini erta aniqlash, davolash va oldini olish bo‘yicha bemorlarga individual yondashaman.",
        "services": ["Kardiologik maslahat", "EKG va tekshiruvlar", "Qon bosimini nazorat qilish", "Reabilitatsiya rejasi"],
        "phone": "+998 90 000 00 01",
        "email": "aziz@example.com",
        "telegram": "aziz_namuna",
        "theme": "blue",
        "views": 128,
    },
    {
        "slug": "namuna-soft",
        "name": "Namuna Soft MChJ",
        "profession": "Dasturiy ta’minot ishlab chiqish",
        "location": "Samarqand viloyati, Samarqand shahri",
        "description": "Veb-saytlar, mobil ilovalar va avtomatlashtirish tizimlari yaratamiz.",
        "about": "Biz kichik va o‘rta biznes uchun veb-saytlar, mobil ilovalar va ichki avtomatlashtirish tizimlarini yaratadigan jamoamiz. Loyihani g‘oyadan ishga tushirishgacha olib boramiz.",
        "services": ["Veb-sayt yaratish", "Mobil ilovalar", "Biznesni avtomatlashtirish", "Texnik qo‘llab-quvvatlash"],
        "phone": "+998 90 000 00 02",
        "email": "info@namunasoft.example.com",
        "telegram": "namunasoft_namuna",
        "theme": "dark",
        "views": 342,
    },
    {
        "slug": "dilnoza-rahimova",
        "name": "Dilnoza Rahimova",
        "profession": "Advokat",
        "location": "Buxoro viloyati, Buxoro shahri",
        "description": "Fuqarolik va tadbirkorlik huquqi bo‘yicha yuridik yordam va maslahat.",
        "about": "Fuqarolik va tadbirkorlik huquqi bo‘yicha yuridik yordam ko‘rsataman. Shartnomalarni tayyorlash, nizolarni hal qilish va sudda vakillik qilish mening asosiy yo‘nalishlarim.",
        "services": ["Yuridik maslahat", "Shartnomalar tayyorlash", "Sudda vakillik", "Hujjatlarni ekspertiza qilish"],
        "phone": "+998 90 000 00 03",
        "email": "dilnoza@example.com",
        "telegram": "dilnoza_namuna",
        "theme": "green",
        "views": 87,
    },
    {
        "slug": "bobur-yusupov",
        "name": "Bobur Yusupov",
        "profession": "IT mutaxassisi, backend dasturchi",
        "location": "Toshkent shahri, Yunusobod tumani",
        "description": "Django va PostgreSQL asosida veb-ilovalar yaratish, mavjud loyihalarni qo‘llab-quvvatlash.",
        "about": "Backend dasturchiman. Django va PostgreSQL asosida veb-ilovalar yarataman, mavjud loyihalarni tahlil qilib, ularni tezlashtiraman va xavfsizligini oshiraman.",
        "services": ["Backend dasturlash", "API yaratish", "Ma’lumotlar bazasini loyihalash", "Kod audit"],
        "phone": "+998 90 000 00 04",
        "email": "bobur@example.com",
        "telegram": "bobur_namuna",
        "theme": "dark",
        "views": 215,
    },
    {
        "slug": "soglom-hayot-klinikasi",
        "name": "Sog‘lom Hayot klinikasi",
        "profession": "Xususiy tibbiyot markazi",
        "location": "Toshkent shahri, Mirzo Ulug‘bek tumani",
        "description": "Terapevt, nevrolog va pediatr qabullari, laboratoriya tahlillari.",
        "about": "Klinikamizda terapevt, nevrolog va pediatr qabul qiladi. Zamonaviy laboratoriya bir kunda natija beradi. Oilangiz salomatligi uchun qulay va ishonchli joy.",
        "services": ["Terapevt qabuli", "Nevrolog qabuli", "Bolalar shifokori", "Laboratoriya tahlillari"],
        "phone": "+998 90 000 00 05",
        "email": "info@soglom.example.com",
        "telegram": "soglom_namuna",
        "theme": "green",
        "views": 301,
    },
    {
        "slug": "malika-tursunova",
        "name": "Malika Tursunova",
        "profession": "Grafik dizayner",
        "location": "Samarqand viloyati, Kattaqo‘rg‘on shahri",
        "description": "Logotip, vizitka va ijtimoiy tarmoqlar uchun dizayn tayyorlash.",
        "about": "Grafik dizaynerman. Brendingiz uchun logotip, vizitka va ijtimoiy tarmoqlar dizaynini tayyorlayman. Har bir ishda mijozning g‘oyasi va maqsadini birinchi o‘ringa qo‘yaman.",
        "services": ["Logotip dizayni", "Vizitka va bukletlar", "Ijtimoiy tarmoqlar dizayni", "Brend uslubi"],
        "phone": "+998 90 000 00 06",
        "email": "malika@example.com",
        "telegram": "malika_namuna",
        "theme": "blue",
        "views": 164,
    },
    {
        "slug": "huquq-markazi",
        "name": "Huquq Markazi MChJ",
        "profession": "Yuridik xizmatlar",
        "location": "Buxoro viloyati, G‘ijduvon tumani",
        "description": "Tadbirkorlar uchun shartnomalar, ro‘yxatdan o‘tkazish va huquqiy maslahat.",
        "about": "Tadbirkorlarga biznesni ro‘yxatdan o‘tkazish, shartnomalar tuzish va huquqiy masalalarda maslahat berish bilan shug‘ullanamiz.",
        "services": ["Biznesni ro‘yxatdan o‘tkazish", "Shartnomalar", "Huquqiy maslahat", "Hujjatlar tayyorlash"],
        "phone": "+998 90 000 00 07",
        "email": "info@huquq.example.com",
        "telegram": "huquq_namuna",
        "theme": "blue",
        "views": 59,
    },
    {
        "slug": "sardor-alimov",
        "name": "Sardor Alimov",
        "profession": "Shifokor-stomatolog",
        "location": "Toshkent shahri, Shayxontohur tumani",
        "description": "Tish davolash, protezlash va bolalar stomatologiyasi.",
        "about": "Stomatolog sifatida tishlarni davolash, protezlash va bolalar stomatologiyasi bilan shug‘ullanaman. Davolashni og‘riqsiz va qulay o‘tkazishga harakat qilaman.",
        "services": ["Tish davolash", "Protezlash", "Bolalar stomatologiyasi", "Professional tozalash"],
        "phone": "+998 90 000 00 08",
        "email": "sardor@example.com",
        "telegram": "sardor_namuna",
        "theme": "green",
        "views": 190,
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

def card_detail(request, slug):
    card = next((c for c in SAMPLE_CARDS if c["slug"] == slug), None)
    if card is None:
        raise Http404("Vizitka topilmadi")
    return render(request, "pages/card_detail.html", {"card": card})


def login_page(request):
    return render(request, "pages/login.html")