# Python for Loop exercises 
clothes = ["shirt", "socks", "pants", "Towel"]
paired_socks = []
for item in clothes:
    if item == "socks":
        continue
    else:
        print(f"washing{item}")
        paired_socks.append(item)
        print(f"washing{paired_socks}")
        