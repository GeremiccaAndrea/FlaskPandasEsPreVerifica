from flask import Flask, request, render_template
app = Flask(__name__)

import pandas as pd 

df = pd.read_excel('https://github.com/wtitze/3E/raw/main/BikeStores.xls', sheet_name = "customers")



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Es1')
def Es1():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    dfinfocliente = df[(df['first_name'] == nome) & (df['last_name'] == cognome)].to_html()
    return render_template('risultato.html', tabella = dfinfocliente )


@app.route('/Es2')
def Es2():
    città = request.args.get('città')
    dfcittà = df[df['city'].str.contains(città)][['first_name', 'last_name']].to_html()
    return render_template('risultato.html', tabella = dfcittà)


@app.route('/Es3')
def Es3():
    dfstato = df.groupby('state')[['zip_code']].count().reset_index().to_html()
    return render_template('risultato.html', tabella = dfstato)


@app.route('/Es4')
def Es4():
    dfstato = df.groupby('state')[['zip_code']].count().reset_index()
    dfricercastato = dfstato[dfstato['zip_code'] == dfstato['zip_code'].max()].to_html() #quando utilizzo una variabile utilizzata precedentemente devo ricopiare il codice scritto sopra
    return render_template('risultato.html', tabella = dfricercastato)

@app.route('/Es5')
def Es5():
    dfnomail = df[df['email'].isnull()][['first_name', 'last_name', 'phone']].to_html()
    return render_template('risultato.html', tabella = dfnomail)

@app.route('/Es6')
def Es6():
    email = request.args.get('email')
    dfmail = df[df['email'].str.contains(email, na = False)].to_html()
    return render_template('risultato.html', tabella = dfmail)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)