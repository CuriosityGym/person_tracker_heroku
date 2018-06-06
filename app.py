from flask import Flask, render_template, Response, g, current_app as app

app = Flask(__name__)

import os



app = Flask(__name__)

dome1 = []
dome2 = []
dome3 = []
dome4 = []
#domeR1 = []
#domeR2 = []
#domeR3 = []
#domeR4 = []

@app.route('/')
def page():
   return render_template('index.html')

@app.route('/live')
def status():
    return render_template('responsive.html', dome1=dome1, dome2=dome2, dome3=dome3, dome4=dome4, domeR1=domeR1, domeR2=domeR2, domeR3=domeR3, domeR4=domeR4)


@app.route('/<device_id>/<person_id>')
def trackPerson(device_id, person_id):
    g.device_id = device_id
    g.person_id = person_id
    person_name = os.environ.get(g.person_id)
    if g.device_id == "beacon1":
        if person_name not in dome1: 
            dome1.append(person_name)
        if person_name in dome2:
            dome2.remove(person_name)
        elif person_name in dome3:
            dome3.remove(person_name)
        elif person_name in dome4:
            dome4.remove(person_name)
        '''elif person_name in domeR1:
            domeR1.remove(person_name)
        elif person_name in domeR2:
            domeR2.remove(person_name)
        elif person_name in domeR3:
            domeR3.remove(person_name)
        elif person_name in domeR4:
            domeR4.remove(person_name)  '''  

    if g.device_id == "beacon2":
        if person_name not in dome2: 
            dome2.append(person_name)
        if person_name in dome3:
            dome3.remove(person_name)
        elif person_name in dome4:
            dome4.remove(person_name)
        elif person_name in dome1:
            dome1.remove(person_name)
        '''elif person_name in domeR1:
            domeR1.remove(person_name)
        elif person_name in domeR2:
            domeR2.remove(person_name)
        elif person_name in domeR3:
            domeR3.remove(person_name)
        elif person_name in domeR4:
            domeR4.remove(person_name)'''    
    if g.device_id == "beacon3":
        if person_name not in dome3: 
            dome3.append(person_name)
        if person_name in dome2:
            dome2.remove(person_name)
        elif person_name in dome1:
            dome1.remove(person_name)
        elif person_name in dome4:
            dome4.remove(person_name)
        '''elif person_name in domeR1:
            domeR1.remove(person_name)
        elif person_name in domeR2:
            domeR2.remove(person_name)
        elif person_name in domeR3:
            domeR3.remove(person_name)
        elif person_name in domeR4:
            domeR4.remove(person_name) ''''   
    if g.device_id == "beacon4":
        if person_name not in dome4: 
            dome4.append(person_name)
        if person_name in dome2:
            dome2.remove(person_name)
        elif person_name in dome3:
            dome3.remove(person_name)
        elif person_name in dome1:
            dome1.remove(person_name)
        '''elif person_name in domeR1:
            domeR1.remove(person_name)
        elif person_name in domeR2:
            domeR2.remove(person_name)
        elif person_name in domeR3:
            domeR3.remove(person_name)
        elif person_name in domeR4:
            domeR4.remove(person_name)'''    
    return "<h3> OK </h3>"

@app.route('/remove/<device_id>/<person_id>')
def remove(device_id, person_id):
    g.device_id = device_id
    g.person_id = person_id
    person_name = os.environ.get(g.person_id)
    if g.device_id == "beacon1":
        domeR1.append(person_name)
        if person_name in dome1:
            dome1.remove(person_name)

    if g.device_id == "beacon2":
        domeR2.append(person_name)
        if person_name in dome2:
            dome2.remove(person_name)
      
    if g.device_id == "beacon3":
        domeR3.append(person_name)
        if person_name in dome3:
            dome3.remove(person_name)
      
    if g.device_id == "beacon4":
        domeR4.append(person_name)
        if person_name in dome4:
            dome4.remove(person_name)
        
    return "<h3> OK </h3>"

if __name__ == '__main__':
    app.run(debug=True)


#p1- cg account
#p2- ota, add button for ota update, remove pins
#p3- battery runtime calc,
#p4- file in out
 

