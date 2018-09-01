alphas = ['-','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def decode_msg(num, d_msgs = set(), d_msg = ''):
	if len(num) == 0:
		d_msgs.add(d_msg)
		return
	d_msg+=alphas[int(num[:1])]	
	decode_msg(num[1:], d_msgs, d_msg)
	if len(num) >= 2 and int(num[:2]) < 27:
		d_msg = d_msg[:-1]
		d_msg+=alphas[int(num[:2])]	
		decode_msg(num[2:], d_msgs, d_msg)
	return d_msgs

msgs = decode_msg("1111")
print(msgs)
msgs.clear()
msgs = decode_msg("1234567")
print(msgs)
msgs.clear()
msgs = decode_msg("111111")
print(msgs)