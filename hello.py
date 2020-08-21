def app(environ, start_response):
	data = "\r\n".join(environ["QUERY_STRING"].split('&'))
	start_response("200 OK", [("Content-Type", "text/plain")])
	return [bytes(data, encoding="utf-8")]