from django.shortcuts import render
from business.models import BusinessForm, Arkans, ContactForm


def hello(request) :


	info_get = request.GET
	info_session = request.session.get('info_get')

	if info_get == {}:
		contacts = ContactForm(info_session)
	else :
		contacts = ContactForm(info_get)
		request.session['info_get'] = info_get


	context = {	'contacts' : contacts}

	return render(request, "index.html", context)



def rezultat(request, name=None) :

	if request.method == "POST" :
		arkan_cel = {}
		arkan_osnova = {}
		arkan_jertva = {}
		t = 0
		osnova = 0
		jertva = 0
		karma_txt = ''

		info_post = request.POST

		info_get = request.GET

		if info_get == {} :
			info_session = request.session.get('info_get')
			contacts = ContactForm(info_session)
		else :
			contacts = ContactForm(info_get)
			request.session['info_get'] = info_get
			info_session = request.session.get('info_get')

		userform = BusinessForm(request.POST)

		business = info_post['business_name'].lower()  # lower case letters
		birth_day = info_session['birth_day']
		birth_month = info_session['birth_month']
		birth_year = info_session['birth_year']

		# dict with alphabet

		d = {
			'а' : 1, 'б' : 2, 'в' : 3, 'г' : 4, 'д' : 5, 'е' : 6, 'ё' : 7, 'ж' : 8,
			'з' : 9, 'и' : 1, 'й' : 2, 'к' : 3,	'л' : 4, 'м' : 5, 'н' : 6, 'о' : 7,
			'п' : 8, 'р' : 9, 'с' : 1, 'т' : 2, 'у' : 3, 'ф' : 4, 'х' : 5, 'ц' : 6,
			'ч' : 7, 'ш' : 8, 'щ' : 9, 'ъ' : 1, 'ы' : 2, 'ь' : 3, 'э' : 4, 'ю' : 5,
			'я' : 6,

			'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8,
			'i' : 9, 'j' : 1, 'k' : 2, 'l' : 3, 'm' : 4, 'n' : 5, 'o' : 6, 'p' : 7,
			'q' : 8, 'r' : 9, 's' : 1, 't' : 2, 'u' : 3, 'v' : 4, 'w' : 5, 'x' : 6,
			'y' : 7, 'z' : 8,

			'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9
		}

		# Массив, содержащий согласные буквы

		sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф',
		        'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'й',
		        'b', 'c,' ,'d', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r',
		        's', 't', 'v', 'x', 'z'
		]
		glasn = ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я',
		         'a', 'e', 'i', 'o', 'u', 'y'
		]

		for i in business :

			if i in d :  # считаем все слово
				t += d[i]

				if i in sogl :
					osnova += d[i]  # считаем основу

					if osnova > 22 :  # проверяем чтобы было меньше 22
						osnova = osnova - int(osnova / 22) * 22

				if i in glasn :  # считаем жертву
					jertva += d[i]
					if jertva > 22 :  # проверяем чтобы было меньше 22
						jertva = jertva - int(jertva / 22) * 22

		# считаем цель
		if t > 22 :  # проверяем чтобы было меньше 22
			cel = t - int(t / 22) * 22

		else :
			cel = t

		# проверяем чтобы было не равно 0
		if cel == 0 :
			cel = 22

		if osnova == 0 :
			osnova = 22

		if jertva == 0 :
			jertva = 22

		# расчет кармичности

		if birth_day != '' and birth_month != '' and birth_year != '' :

			birth_day = int(birth_day)
			birth_month = int(birth_month)

			if (birth_day >= 14) and (birth_day <= 22) :

				Karma1 = birth_day - birth_month
				Karma2 = birth_day


			else :
				dt = birth_day
				if (birth_day > 22) :
					dt = birth_day - 22

				Karma1 = abs(dt - birth_month)

				if Karma1 == 0 :
					Karma1 = 22
				Karma2 = 0

				if cel == Karma1 or cel == Karma2 :
					karma_txt = 'НАЗВАНИЕ КАРМИЧНО'
				if osnova == Karma1 or osnova == Karma2 :
					karma_txt = 'НАЗВАНИЕ КАРМИЧНО'
				if jertva == Karma1 or jertva == Karma2 :
					karma_txt = 'НАЗВАНИЕ КАРМИЧНО'

			arkan_cel = Arkans.objects.get(arkan_number=cel)
			cel_txt = arkan_cel.cel
			arkan_osnova = Arkans.objects.get(arkan_number=osnova)
			osnova_txt = arkan_osnova.osnova
			arkan_jertva = Arkans.objects.get(arkan_number=jertva)
			jertva_txt = arkan_jertva.jertva

			context = {
				'form' : userform, 'business' : business, 'contacts': contacts,
				'cel' : cel, 'osnova' : osnova, 'jertva' : jertva, 'cel_txt' : cel_txt,
				'osnova_txt' : osnova_txt, 'jertva_txt' : jertva_txt, 'birth_day' : birth_day,
				'birth_month' : birth_month, 'birth_year' : birth_year, 'karma_txt' : karma_txt
			}
			return render(request, "business_name.html", context)

		else :

			arkan_cel = Arkans.objects.get(arkan_number=cel)
			cel_txt = arkan_cel.cel
			arkan_osnova = Arkans.objects.get(arkan_number=osnova)
			osnova_txt = arkan_osnova.osnova
			arkan_jertva = Arkans.objects.get(arkan_number=jertva)
			jertva_txt = arkan_jertva.jertva


			context = {
				'form' : userform, 'business' : business, 'contacts': contacts,
				'cel' : cel, 'osnova' : osnova, 'jertva' : jertva, 'cel_txt' : cel_txt,
				'osnova_txt' : osnova_txt, 'jertva_txt' : jertva_txt, 'birth_day' : birth_day,
				'birth_month' : birth_month, 'birth_year' : birth_year, 'karma_txt' : karma_txt,

			}
			return render(request, "business_name.html", context)



	else :

		form = BusinessForm()

		info_get = request.GET
		info_session = request.session.get('info_get')

		if info_get == {} :
			contacts = ContactForm(info_session)
		else :
			contacts = ContactForm(info_get)
			request.session['info_get'] = info_get

		context = {
			'form' : form, 'contacts': contacts
		}

		return render(request, "business_name.html", context)
