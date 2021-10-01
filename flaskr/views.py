import os

from flask import (
    Blueprint, render_template, request
)

earnings_bp = Blueprint('get_earnings', __name__, url_prefix='/')


@earnings_bp.route('/earnings/', methods=('GET', 'POST'))
def get_earnings():
    from db import get_db

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()

    return render_template('earnings.html')
