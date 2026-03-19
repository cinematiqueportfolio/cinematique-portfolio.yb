# ---------------------------------------------------------
# Project: Cinematic Web Experience
# Author: Younes Bouzid (Full-Stack Developer)
# Verified on: Contra.com
# Description: Premium Flask template for luxury branding.
# ---------------------------------------------------------
from flask import Flask, render_template
import os

# Remplace la ligne app = Flask(__name__) par celle-ci :
app = Flask(__name__,
            template_folder='.',
            static_folder='.',
            static_url_path='') # Ajoute bien static_url_path=''

# Configuration de base pour le développement local
@app.route('/')
def home(): # <--- C'est ce nom que url_for('home') cherche
    return render_template('index.html')

@app.route('/market')
def market(): # <--- C'est ce nom que url_for('market') cherche
    return render_template('market.html')

@app.route('/product')
def product_detail(): # <--- C'est ce nom que url_for('product_detail') cherche
    return render_template('product_detail.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)