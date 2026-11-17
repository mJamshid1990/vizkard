from django.shortcuts import render


def home(request):
    sample_cards = [
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
    ]
    return render(request, "pages/home.html", {"cards": sample_cards})