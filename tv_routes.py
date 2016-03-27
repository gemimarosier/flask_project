from flask import Flask, render_template
from tv_shows import TV_SHOWS  
app = Flask(__name__)

#write functions here 
def get_show(source):
    shows = []
    for row in source:
        show = row["TV Show"]
        shows.append(show)
    return shows
    
def get_data(source, show):
    for row in source:
        if show == row['TV Show']:
            network = row['Network'].decode('utf-8')
            year = row['Year Released']
    return show, network, year
      


@app.route ('/tv_list/<shows>')
#call functions here
def tv_list(shows):
    shows = get_show(TV_SHOWS)
    return render_template('tv_list.html', shows=shows, TV_SHOWS=TV_SHOWS)


@app.route ('/tv_detail/<id>')
#call functions here
def detail(id):
    shows = get_show(TV_SHOWS)
    number = shows.index(id)
    show = shows[number]
    show, network, year = get_data(TV_SHOWS, show)
    get_data(TV_SHOWS, show)
    return render_template('tv_detail.html', id=id, network=network, year=year)


if __name__ == '__main__':
    app.run(debug=True)