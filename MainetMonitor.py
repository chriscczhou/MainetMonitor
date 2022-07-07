from web3 import Web3
import requests
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36","Content-Type":"application/json"}
text = '''
{"msgtype": "link",    "link": {
        "text": "%s", 
        "title": "%s", 
        "picUrl": "", 
        "messageUrl": "%s"
    }}
'''


while True:
	try:
		w3 = Web3(Web3.HTTPProvider('https://eth-rpc.gateway.pokt.network'))
		if(w3.isConnected()):
			txs = w3.eth.getBlock("pending",False)['transactions']
			for tx in txs:
				print("#############################################")
				print("交易哈希："+tx.hex())
				try:
					txDetail = w3.eth.getTransaction(tx.hex())
					print(txDetail['input'])
					if(txDetail['input'][0:10] == "0x715018a6"):
						print("renounceOwnership！")
						url = "https://cn.etherscan.com/tx/"+tx.hex()
						r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=XXXXX", data=text % ("renounceOwnership",url,url),headers=HEADERS)
					elif(txDetail['input'][0:10] == "0x7d533c1e"):
						print("lockTokens！")
						url = "https://cn.etherscan.com/tx/"+tx.hex()
						r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=XXXXX", data=text % ("Lock Tokens",url,url),headers=HEADERS)
						print(txDetail['to']) # lockTokens()
					elif(txDetail['input'][0:10] == "0xf305d719"):
						print("addLiquidityETH")
						url = "https://cn.etherscan.com/tx/"+tx.hex()
						r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=XXXX", data=text % ("add Liquidity",url,url),headers=HEADERS)
					else:
						pass
				except Exception as e:
					pass


	except Exception as e:
		print(e)
		pass
