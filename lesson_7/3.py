with open ("app.log") as log_file:
    req_dict={}
    for lines in log_file:
        ip, date, time,*other=lines.split(' ')
        time=time[0:8]
        if ip in req_dict.keys():
            req_dict[ip].append(time)         
        else:
            req_dict.update({ip:[time]})
print(req_dict)
