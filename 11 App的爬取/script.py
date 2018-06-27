from mitmproxy import ctx

# def request(flow):
#     flow.request.headers['User-Agent'] = 'MitmProxy'
#     ctx.log.info(str(flow.request.headers))
#     print('-'*100)
#     ctx.log.info(str(flow.request.text))
#     print('-'*100)
#     # ctx.log.warn(str(flow.request.headers))
    # ctx.log.error(str(flow.request.headers))

def response(flow):
    response = flow.response
    info = ctx.log.info
    info(str(response.status_code))
    info(str(response.headers))
    ctx.log.error(str(response.text))