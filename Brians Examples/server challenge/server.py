import web
        
urls = (
    '/(.*)', 'hello'
)

class hello:        
    def GET(self,name):
        raise web.seeother('/show_this.html')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
