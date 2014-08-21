import web
        
urls = (
    '/(.*)', 'hello'
)

class hello:        
    def GET(self,name):
        raise web.seeother('/static/test.png')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
