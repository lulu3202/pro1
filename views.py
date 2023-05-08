from flask import Blueprint, render_template, request, jsonify, redirect, url_for

main = Blueprint("main", __name__)

@main.route("/")
def home():
    country = request.args.get("country")
    source = request.args.get("source")  
    return render_template("index.html", country=country, source=source)

@main.route("/about")
def about():
    context = {
        "name": "Shubham",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis quisquam provident consectetur expedita quaerat odit sit voluptates laborum debitis est laboriosam corrupti ratione, aperiam, sed odio cumque quas dolor esse pariatur voluptatem, placeat eum vitae. Eum maxime et, amet itaque aliquam incidunt qui magnam id officia voluptate sequi quidem ut. Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis quisquam provident consectetur expedita quaerat odit sit voluptates laborum debitis est laboriosam corrupti ratione, aperiam, sed odio cumque quas dolor esse pariatur voluptatem, placeat eum vitae. Eum maxime et, amet itaque aliquam incidunt qui magnam id officia voluptate sequi quidem ut!",
    }
    return render_template("about.html", context=context)

@main.route('/about-us')
def about_us():
    return redirect(url_for("main.about"))

@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/portfolio")
def portfolio():
    projects_list = [
        {'name': 'Taskmate', 'description': 'This is the first project.', 'endpoint': 'taskmate'},
        {'name': 'Codebook', 'description': 'This is the second project.', 'endpoint': 'codebook'},
    ]
    return render_template("portfolio.html", projects=projects_list)

@main.route("/portfolio/<project>")
def project(project):
    projects_lst = ["taskmate", "codebook"]
    if project in projects_lst:
        return render_template(f"portfolio/{project}.html")
    else:
        return redirect("/404")
    
@main.route('/portfolio/json')
def portfolio_json():
    projects = {
        "taskmate": {
            "langauge": "python",
            "framework": "django",
            "status": "completed"
        },
        "codebook": {
            "langauge": "javascript",
            "framework": "react",
            "status": "learning"
        }
    }
    return jsonify(projects)
    
@main.route("/s")
def search():
    keyword = request.args.get("k")
    return f"{keyword}"

@main.route('/404')
def not_found_404():
    return render_template("404.html"), 404

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404