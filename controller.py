from app import app
from flask import render_template, request


@app.route('/about_us')
def about_button():
    return render_template('information_about_the_site.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    # Принимаем данные с POST запроса
    if request.method == 'POST':
        # Получение данных с Frontend
        login = request.form.get('username')
        password = request.form.get('password')
        # Проверка данных
        print(login, password)
        return render_template('main_menu.html')
    return render_template('authorization.html')


app.run()


@app.route('/shovel')
def shovel():
    return ('https://market.yandex.ru/product--solid-1026684'
                           '-113-sm/1778070449?sku=39610219&uniqueId=889762&do'
                           '-waremd5=x6vIZ9SzhxJyqUkxaVSXvg')


@app.route('/screen')
def screen():
    return ('https://market.yandex.ru/product--27-monitor-27-lg-27gs60f-b-'
            'black-ips-1920x1080-180hz/129615390?sku=103090671047&uniqueId='
            '919913&do-waremd5=jwoWwXW_WZYkG1HjuWi9Lw&sponsored=1')