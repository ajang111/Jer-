import sqlite3

from flask import Blueprint, redirect, render_template, request, session

import student_network.helpers.helper_connections as helper_connections
import student_network.helpers.helper_general as helper_general

shop_blueprint = Blueprint(
    "shop", __name__, static_folder="static", template_folder="templates"
)

@shop_blueprint.route("/shop")
def shop():
    return render_template("shop.html", 
        requestCount=helper_connections.get_connection_request_count(),
        notifications=helper_general.get_notifications()
    )