from flask import Flask, render_template, request, Response
import matplotlib.pyplot as plt
import io  # Add this line

mylabels = ["ToothPaste", "FaceCream", "FaceWash", "Bathing Soap", "Shampoo", "Moisturizer"]

app = Flask(__name__)

@app.route('/')
def num_start():
    return render_template('plot.html')

@app.route('/numbers', methods=['POST'])
def numbers():
    data = request.form.to_dict()

    ypoints = [float(data[key]) for key in mylabels]

    fig, ax = plt.subplots()
  
    ax.axis('equal')
    ax.pie(ypoints, labels=mylabels,autopct='%1.1f%%') 
    ax.legend()
    fname = './static/linechart.jpg'
    plt.savefig(fname)
    return fname


