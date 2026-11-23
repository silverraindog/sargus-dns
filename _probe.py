import dns.server as s
import dns.message as m
import dns.resolver as r
print("SERVER members:", [x for x in dir(s) if not x.startswith('_') and x[0].islower() or x in ('Handler','Server','AsyncServer','start','start_async','AddressFamily','Transport','Handler','Server','AsyncServer')])
print("---")
print("Handler base:", getattr(s, 'Handler', None))
print("Server:", s.Server)
print("AsyncServer:", getattr(s, 'AsyncServer', None))
print("start_async:", getattr(s, 'start_async', None))
print("message Response:", m.Response)
print("message Message:", m.Message)
print("FLAG ANSWER:", m.FLAG.ANSWER, "NOANSWER:", m.FLAG.NOANSWER)
print("Rcode OK:", m.Rcode.OK, "SERVFAIL:", m.Rcode.SERVFAIL, "NODATA:", m.Rcode.NODATA)
print("resolver Resolver:", r.Resolver)
print("Resolver.nameservers attr?")
res = r.Resolver()
print("  nameservers=", res.nameservers)
print("  timeout attr:", res.timeout)
print("---build a Response from request---")
req = m.Query(name=m.DNAME.from_txt('x.example'), rd=True, ra=True)
req.qtype = m.QTYPE.A
# try Response(request)
try:
    resp = m.Response(req)
    print("Response(req) OK; type=", type(resp), "flag ANSWER=", resp.flags & m.FLAG.ANSWER)
    resp.flag(m.FLAG.ANSWER)
    print(" after set flag:", resp.flags & m.FLAG.ANSWER)
    rec = m.RRecord('x.example', m.QTYPE.A, 300, m.ANSTR('192.0.2.1'))
    resp.answer.append(rec)
    print(" answer append OK:", resp)
except Exception as e:
    print("Response(req) FAILED:", repr(e))
print("---resolver.resolve ---")
print(" resolve signature ok? type:", r.Resolver)
