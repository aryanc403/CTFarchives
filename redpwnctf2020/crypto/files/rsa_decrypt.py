ct=2082926013138674164997791605512226759362824531322433048281306983526001801581956788909408046338065370689701410862433705395338736589120086871506362760060657440410056869674907314204346790554619655855805666327905912762300412323371126871463045993946331927129882715778396764969311565407104426500284824495461252591576672989633930916837016411523983491364869137945678029616541477271287052575817523864089061675401543733151180624855361245733039022140321494471318934716652758163593956711915212195328671373739342124211743835858897895276513396783328942978903764790088495033176253777832808572717335076829539988337505582696026111326821783912902713222712310343791755341823415393931813610365987465739339849380173805882522026704474308541271732478035913770922189429089852921985416202844838873352090355685075965831663443962706473737852392107876993485163981653038588544562512597409585410384189546449890975409183661424334789750460016306977673969147
N=2739699434633097765008468371124644741923408864896396205946954196101304653772173210372608955799251139999322976228678445908704975780068946332615022064030241384638601426716056067126300711933438732265846838735860353259574129074615298010047322960704972157930663061480726566962254887144927753449042590678730779046154516549667611603792754880414526688217305247008627664864637891883902537649625488225238118503996674292057904635593729208703096877231276911845233833770015093213639131244386867600956112884383105437861665666273910566732634878464610789895607273567372933766243229798663389032807187003756226177111720510187664096691560511459141773632683383938152396711991246874813205614169161561906148974478519987935950318569760474249427787310865749167740917232799538099494710964837536211535351200520324575676987080484141561336505103872809932354748531675934527453231255132361489570816639925234935907741385330442961877410196615649696508210921
e=65537

p=139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409397803
q=139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409494847
r=139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409208581

print(len(bin(p)),bin(p))
print(len(bin(q)),bin(q))
print(len(bin(r)),bin(r))

phi = (p-1)*(q-1)*(r-1)

def po(a,n,mod):
    ans=1
    while n:
        if n%2:
            ans=(ans*a)%mod
        a=(a*a)%mod
        n//=2
    return ans

assert(po(2,phi,N)==1)

def extended_gcd(a, b):
    """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0

d=extended_gcd(e,phi)[1]%phi
# print(d)
ans=po(ct,d,N)
# print(ans)
print(hex(ans))
