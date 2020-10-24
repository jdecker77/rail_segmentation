from flask import Flask, request, session, redirect, render_template, jsonify


# Application Definition
# ___________________________________________________________________________________________
ppe = Flask(__name__)



# Homepage
# ___________________________________________________________________________________________
@ppe.route('/', methods=['GET'])
def render_index():
    title = 'Pantograph Pose Estimation'
    return render_template('index.html', page_title=title)
