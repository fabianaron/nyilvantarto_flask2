from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
app = Flask(__name__)
app.debug = True
#a / oldalon get és post method-okat is engedünk
#https:www.w3schools.com/tags/ref_httpmethods.asp
#EZNEM EGY IGAZI BEJELENTKEZO FELULET
validuser = "aron"
@app.route("/", methods=['GET','POST'] )
def index():
	#egy error valtozot deklaralunk aminek a kezdo erteken None (azaz semmi)
	error = None
	#ha ez a page ugy van meghivva hogy a kliens POST-ot kuld
	if request.method == 'POST':
		#a login.html-ben levo form adatok , kiszedjuk qa POSt-bol, es betoltjuk,
		#ket darab valtozobe.
		email = request.form.get('email')
		passwd = request.form.get('password')
		print(email)
		print(passwd)
		#a bekuldott adatok kozul ellenorizzuk a felhasznalonevet, es ha az helyes
		if email == "aron":
			return redirect(url_for('nyilvantarto'))
		else:
			#ha rossz adatokat adott meg, akkor egy hibauzenetet kuldunk..
			error = 'Invqalid Credentials. Pleas try agin.'
			#a flask minden template file-t a templates mappan belul keres.
			# ha nem POST a http keres, hanem GET, akkor siman csak a login.html-t rendereljuk:
	return render_template('login.html', error=error)


@app.route("/nyilvantarto")
def nyilvantarto():
	user = validuser
	#a user valtozo, az az index.html file-ban is user valtozokent lest elerheto
	return render_template('index.html',user=user)

if __name__=="__main__":
	app.run(host='0.0.0.0')
