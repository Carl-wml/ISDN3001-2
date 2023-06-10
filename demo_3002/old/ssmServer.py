from ssm import ScreenMirrorServer

# ssm_server = ScreenMirrorServer(host = '10.89.74.186', port=7890)
ssm_server = ScreenMirrorServer()  # default: all ip & 7890 port

ssm_server.start()


from ssm import ScreenMirrorClient

ssm_client = ScreenMirrorClient(host = '10.89.74.186', port=7890, quality=90, cursor=True)

ssm_client.start()