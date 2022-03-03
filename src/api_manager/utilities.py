from src.api_manager.api_endpoints import RestCountry, Nationalize, ReqMethod


def asd2():
    nat = Nationalize()
    res = RestCountry()

    print("asd")

    resp = nat.send_request(ReqMethod.get, "Marco")
    b = nat.check_response(resp)
    if b.get("status") != 200:
        print("Problems")
    else:
        cc = nat.extract_results(b.get("content"))
    resp = res.send_request(ReqMethod.get, "AU")
    a = res.check_response(resp)
    asasd = res.extract_results(a.get("content")[0])
    print("asd")


if __name__ == '__main__':
    asd2()