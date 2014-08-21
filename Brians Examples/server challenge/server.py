import web
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self):
        raise web.seeother('show_this.html')


if __name__ == "__main__":
    app.run()
