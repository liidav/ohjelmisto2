from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<nro>')
def alkuluku(nro):
    isPrime = True
    nro = int(nro)

    for jakaja in range(2, nro):
        if nro % jakaja == 0:
            isPrime = False

    vastaus = {'Number': f'{nro}', 'isPrime': f'{isPrime}'}

    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3002)
