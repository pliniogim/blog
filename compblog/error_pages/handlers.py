# handlers.py

from flask import Blueprint, render_template
error_pages = Blueprint('error_pages',__name__)


@error_pages.app_errorhandler(404)
@error_pages.app_errorhandler(500)
def handle_error(error):
    print(error)
    return render_template(
        'error_pages/error.html', 
        code=error.code, 
        name=error.name,
        description=error.description
    ), error.code