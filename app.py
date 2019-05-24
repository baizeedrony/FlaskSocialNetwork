from flask import Flask, render_template, url_for

app=Flask(__name__)

posts = [

    {
        'author': 'kamal khan',
        'title':'it is a first title',
        'content':'it is a first content',
        'date_posted':'may 5,2019'
    },

     {
        'author': 'jamal khan',
        'title':'it is a second title',
        'content':'it is a second content',
        'date_posted':'may 6,2019'
    }
]

@app.route('/')
def home():
    return render_template('home.html',variable_poll=posts)
print(home)

@app.route('/about')
def about():
    return render_template('about.html',title='about')

if __name__=='__main__':
    app.run(debug=True)


