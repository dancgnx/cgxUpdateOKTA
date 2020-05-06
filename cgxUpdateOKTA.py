#!/usr/bin ptpython3

import cgxinit
import requests
from cloudgenix import jd, jd_detailed

if __name__ == "__main__":
    # parse commands and get CGX
    cgx, args = cgxinit.go()

    IPs = set()
    # get the json file
    for key, row in requests.get(args["url"]).json().items():
        for IP in row['ip_ranges']:
            if "255/32" not in IP:
                IPs.add(IP)

    # get the list of existing prefixes in the prefix list
    for filter in cgx.get.globalprefixfilters().cgx_content['items']:
        if filter["name"] == args["prefix"]:
            filter["filters"][0]["ip_prefixes"] = list(IPs)
            res = cgx.put.globalprefixfilters(filter["id"], filter)
            if not res:
                jd_detailed(res)
            else:
                print(f"{args['prefix']} update successfuly")



