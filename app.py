from cgi import parse_qs
from exp_syst_calc import *
#from exp_syst_dict import *
html = """Введите значения в интервале от 0 до 1 в формате '0.1'.<br>
<form method="get">Вы предпочитаете телефон компании Samsung?<input name="Answer1"></input><br>
<form method="get">Вы предпочитаете телефон компании Apple?<input name="Answer2"></input><br>
<form method="get">Вы предпочитаете телефон компании Lenovo?<input name="Answer3"></input><br>
<form method="get">Вам необходима модель последнего поколения?<input name="Answer4"></input><br>
<form method="get">Вы предпочитаете операционную систему Android?<input name="Answer5"></input><br>
<form method="get">Вы предпочитаете операционную систему iOS?<input name="Answer6"></input><br>
<button>OK</button></form>"""
def wsgi_app(environ, start_response): 
    response_headers = [('Content-type', 'text/html; charset=UTF-8')]
    response_body = html
    status = '200 OK'
    start_response(status, response_headers)
    yield response_body.encode()
    x = []
    good=0
    d = parse_qs(environ['QUERY_STRING'])
    Answer1 = d.get('Answer1',[None])[0]
    Answer2 = d.get('Answer2',[None])[0]
    Answer3 = d.get('Answer3',[None])[0]
    Answer4 = d.get('Answer4',[None])[0]
    Answer5 = d.get('Answer5',[None])[0]
    Answer6 = d.get('Answer6',[None])[0]
    x.append(Answer1)
    x.append(Answer2)
    x.append(Answer3)
    x.append(Answer4)
    x.append(Answer5)
    x.append(Answer6)
    if Answer1 and Answer2 and Answer3 and Answer4 and Answer5 and Answer6:
        try:
            for i in range(0,len(x)-1):
                x[i]=float(x[i])
            #y=calc(x)
            response_body=x
            start_response(status, response_headers)
            yield response_body.encode()
        except:
            response_body="Пожалуйста, введите корректные значения.<br>"
            start_response(status, response_headers)
            yield response_body.encode()
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
