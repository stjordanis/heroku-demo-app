from flask import Flask, request, jsonify

from crawl_queue import CrawlerQueue

app = Flask(__name__)
crawler_queue = CrawlerQueue()

@app.route('/append/', methods=['GET'])
def respond():
    crawler_queue.append("lorem")
    return len(crawler_queue)


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':

    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)