# Modificacion
import web 

urls = (
    "/", "Index",
    "/webpy", "webpy",
    "/javascript", "javascrip"
    )
app = web.application(urls, globals())
render = web.templete.render("templetes/", base="layout")


class Index:
    def GET(self):
        return render.index()