from flask import Flask, render_template, g, make_response
import json
import os
import os.path
import requests
import random
import string
import time
import csv
data = {'Band': 'A1', 'Name': 'Alex', 'Location': 'Dome1', 'In_Time': "1", 'Out_Time': "2", 'Date': "15"}

app = Flask(__name__)

dome1 = []
dome2 = []
dome3 = []
dome4 = []
fileName = 'stats.csv'



@app.route('/shopping')
def list():
    return render_template('shopping.html', dome1=dome1, dome1Len=len(dome1), dome2=dome2, dome2Len=len(dome2), dome3=dome3, dome3Len=len(dome3), dome4=dome4, dome4Len=len(dome4))

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/live')
def status():
    return render_template('responsive.html', dome1=dome1, dome1Len=len(dome1), dome2=dome2, dome2Len=len(dome2), dome3=dome3, dome3Len=len(dome3), dome4=dome4, dome4Len=len(dome4))


@app.route('/demo')
def live():
    return render_template('live.html', dome1=dome1, dome1Len=len(dome1), dome2=dome2, dome2Len=len(dome2), dome3=dome3, dome3Len=len(dome3), dome4=dome4, dome4Len=len(dome4))

@app.route("/download")
def download():
    return render_template('download.html')

@app.route("/getPlotCSV")
def getPlotCSV():
    csv = 'foo,bar,baz\nhai,bai,crai\n'
    response = make_response(csv)
    cd = 'attachment; filename=flask-demooutput.csv'
    response.headers['Content-Disposition'] = cd
    response.mimetype='text/csv'

    return response


@app.route('/<device_id>/<person_id>')
def trackPerson(device_id, person_id):
    g.device_id = device_id
    g.person_id = person_id
    #person_name = os.environ.get(g.person_id)
    if g.device_id == "beacon1":
        data['Location'] = g.device_id
        data['Name'] = g.person_id
        data['Band'] = g.person_id
        dome1.append(g.person_id)
        if g.person_id in dome2:
            dome2.remove(g.person_id)
        elif g.person_id in dome3:
            dome3.remove(g.person_id)
        elif g.person_id in dome4:
            dome4.remove(g.person_id)

    if g.device_id == "beacon2":
        data['Location'] = g.device_id
        data['Name'] = g.person_id
        data['Band'] = g.person_id
        dome2.append(g.person_id)
        if g.person_id in dome3:
            dome3.remove(g.person_id)
        elif g.person_id in dome4:
            dome4.remove(g.person_id)
        elif g.person_id in dome1:
            dome1.remove(g.person_id)
    if g.device_id == "beacon3":
        data['Location'] = g.device_id
        data['Name'] = g.person_id
        data['Band'] = g.person_id
        dome3.append(g.person_id)
        if g.person_id in dome2:
            dome2.remove(g.person_id)
        elif g.person_id in dome1:
            dome1.remove(g.person_id)
        elif g.person_id in dome4:
            dome4.remove(g.person_id)
    if g.device_id == "beacon4":
        data['Location'] = g.device_id
        data['Name'] = g.person_id
        data['Band'] = g.person_id
        dome4.append(g.person_id)
        if g.person_id in dome2:
            dome2.remove(g.person_id)
        elif g.person_id in dome3:
            dome3.remove(g.person_id)
        elif g.person_id in dome1:
            dome1.remove(g.person_id)

    file_basename = 'output.csv'
    server_path = os.path.dirname(os.path.abspath(__file__))
    file_exists = os.path.isfile(server_path+file_basename)
    w_file = open(server_path+file_basename, 'a')

    if not file_exists:
        w_file.write('Band,Name,Location,In-Time,Out_Time,Date \n')
        w_file.write('%s,%s,%s,%s,%s,%s \n' %(data['Band'],data['Name'],data['Location'],data['In_Time'],data['Out_Time'],data['Date']))

    #for row, x in data.items():
     #   x_as_string = str(x)
      #  w_file.write(x_as_string+ '\n')
    else:
        w_file.write('%s,%s,%s,%s,%s,%s \n' %(data['Band'],data['Name'],data['Location'],data['In_Time'],data['Out_Time'],data['Date']))
    w_file.close()

    return "OK"
if __name__ == '__main__':
    app.run(debug=True)
