from flask import render_template,redirect,url_for,session,g,Blueprint,request,flash
import functools

from auth import login_required

from db import get_db
from ordenamiento import edit_time,ordenar

bp = Blueprint('user',__name__)




@bp.route('/index')
@login_required
def index():
    db,c = get_db()
    c.execute(
        'select username from usuario where id = %s',(session.get('user_id'),)
    )
    g.user = c.fetchone()
    c.execute(
        'select username,categoria,tiempo,completed from usuario inner join partida on usuario.id = partida.user_id'
    )
    user = c.fetchall()
    user = edit_time(user)
    user = ordenar(user)
    return render_template('user/index.html',user=user)



