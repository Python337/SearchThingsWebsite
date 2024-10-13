from app import app, db
from models import User
from flask import render_template, request

from buisness_logic.check import check_login, check_password

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
        if check_login(login) and check_password(password):
            user = User(login=login, password=password)
            db.session.add(user)
            db.session.commit()
        else:
            print('Проверка НЕ пройдена')
        print(login, password)
        return render_template('main_menu.html')
    return render_template('authorization.html')


@app.route('/shovel')
def shovel():
    return open('https://market.yandex.ru/product--solid-1026684'
            '-113-sm/1778070449?sku=39610219&uniqueId=889762&do'
            '-waremd5=x6vIZ9SzhxJyqUkxaVSXvg')


@app.route('/screen')
def screen():
    return ('https://market.yandex.ru/product--27-monitor-27-lg-27gs60f-b-'
            'black-ips-1920x1080-180hz/129615390?sku=103090671047&uniqueId='
            '919913&do-waremd5=jwoWwXW_WZYkG1HjuWi9Lw&sponsored=1')


@app.route('/plate')
def plate():
    return ('https://www.muztorg.ru/produсt/A096552?utm_source=yd&utm_medium'
            '=cpc&utm_term=&utm_campaign=smart-shopping-yandex-69863387&utm_'
            'content=v2%7C%7C11583585214%7C%7C2194379%7C%7C%7C%7C2%7C%7Cpremi'
            'um%7C%7Cnone%7C%7Csearch%7C%7Cno&yclid=13533368254049288191')


@app.route('/mouse_pad')
def mouse_pad():
    return ('https://www.wildberries.ru/catalog/133030253/detail.aspx')


@app.route('/screwdriver')
def screwdriver():
    return ('https://market.yandex.ru/product--gsb-180-li-601-9f8-323/'
            '501087011?sku=100702191122&uniqueId=39375547&do-waremd5=2'
            '0KOlxyESfwUIvand-7kkg&sponsored=1')

