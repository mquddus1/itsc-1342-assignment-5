# Mohammed Abdul Quddus - Assignment 5

def sanitize_ip_list(ip_list, blocked_ip):
    clean_list = []
    for ip in ip_list:
        if ip == blocked_ip:
            continue
        elif "invalid" in ip:
            clean_list.append("0.0.0.0")
        else:
            clean_list.append(ip)
    return clean_list
