def lettercount(a, b):
    tot = 0
    for i in b:
        if i == a:
            tot += 1
    return tot

def stringcomp(a, b):
    tot = 1
    for i in range(len(a)):
        if not (a[i] == b[i]):
            tmpind = i 
            tot -= 1
        if tot < 0:
            return (False, 0)
    return (True, tmpind)

def main():
    data = """fonbsmjyqugrapsczckghtvdxl
    fonpsmjyquwrnpeczikghtvdxw
    fonbsmdymuwrapexzikghtvdxl
    fonwsmjyquwrapeczikghttdpl
    fonbsmjkquwrapeczjkghtvdxx
    yonbsmjyquwrapecgikghtvdxc
    donbsmjyquqrapeczikghtadxl
    monbsmjyquprgpeczikghtvdxl
    fonbsmjyquwvapecqgkghtvdxl
    fonbsmjyquwrkphczikghsvdxl
    fonbomjyeuwvapeczikghtvdxl
    fonwsmjyjuwrapoczikghtvdxl
    foybsmjyquwcapeczikghsvdxl
    fonbsmjyquwrtaeczikgptvdxl
    ponbsmpyquwjapeczikghtvdxl
    flnbcmjyquwrqpeczikghtvdxl
    fonbsmjyquwrapegzikvbtvdxl
    fonbjmjyqgwrazeczikghtvdxl
    zoabsmjyquwkapeczikghtvdxl
    fonbsmjyquwrapecziktxkvdxl
    fonbsxjyrpwrapeczikghtvdxl
    fonbsmjbquwqapeciikghtvdxl
    lonbsmjyquwraphczikghtvdul
    ftnbsmjyquwrapcczikghtxdxl
    fonbsmjyqgwrapeczikghtldxc
    fonbsmjsquwmapeyzikghtvdxl
    fonbsmjyqfwrapecziqghtgdxl
    yonbsmjyquwraveczikgftvdxl
    fovbsmjyquwrapeczikggkvdxl
    fonbsmjyquwrapezzikghbvdvl
    fonzsmxyquwrapeczukghtvdxl
    fonbemjyquwrapevzikghtvrxl
    conbsxjxquwrapeczikghtvdxl
    fonbsmjsmewrapeczikghtvdxl
    folbsmjyqhwrapqczikghtvdxl
    fonbsmjyquwrzneczikghtvdxn
    fonbsmjyquirapeczikjhtvdll
    fontsmgyquwrgpeczikghtvdxl
    fonbsmjyauwrapeczbfghtvdxl
    ftnbsmjyquwrapecpifghtvdxl
    fonvsmjyqewrapeczikghlvdxl
    fonbsljyquwrapecziklhtvdxw
    fonbbmjyquwrapeczikghvadxl
    ponbsmjyquwrspeczikghivdxl
    fonbsmjcquwrapeccikghtvuxl
    fonbsmjnquwrapetzikghtvlxl
    fonbsmjymuwrapeczieghtvdxr
    ffnbsxnyquwrapeczikghtvdxl
    fonbsmjytuwrajeczzkghtvdxl
    fonssmjyquwhapeczikghkvdxl
    fonbsajyuuwrapeczikghlvdxl
    fonbsmjyquwrapeczihghtcixl
    fohbsmjyquwrapzczirghtvdxl
    fonbsmjyquwrapecjqnghtvdxl
    fonbsmjytuhrapeczihghtvdxl
    foabumjyquwrapeczikghtvdxz
    conbsmjyqtwrapeczikggtvdxl
    fonbsmjyiqwrapeczokghtvdxl
    fondsmjypuwrapeczikghtvjxl
    fonbswjyquwrapeczikgvtydxl
    fonbsmjyqqwrapeczikkhtvdbl
    fonbsmjyquwrapemzitghtvdsl
    fonbsmjyquwrspecziegxtvdxl
    fonbsmpyquwrgpeczikghtwdxl
    fodbsmjqquwrapeczmkghtvdxl
    fonbsmjkquwrapeczikghpvdxr
    fonbsmjyquwrapeczikshzvmxl
    fznbsmjyqulrapeczikghkvdxl
    fonbsmjyquwripeczikghtbdjl
    fcnbsmjyquzrapecyikghtvdxl
    ronbxmjyquwrapeczikghgvdxl
    fonbsmuyvuwrgpeczikghtvdxl
    fonbsmjyyuwraplczikghtudxl
    poxbsmjyqewrapeczikghtvdxl
    foabsmjyquwrapecziqghtvpxl
    ponbsmjrquwrapeczikchtvdxl
    fonzzmjyquwrapeczikghtvdxs
    wonbsmjyquwghpeczikghtvdxl
    fofbsejyquwrapeczikgctvdxl
    ponbsmjyquwrayegzikghtvdxl
    fonbumjyquwripeczikghtvdxf
    fonbsmqyquwrapeczikgftvdxv
    qonbsmjyquwraplczitghtvdxl
    fmnbsajdquwrapeczikghtvdxl
    fonbsrjyquwrapempikghtvdxl
    fonbsmjyquwrapeczikgotudxw
    fonbsmtyquwrapeflikghtvdxl
    fzqbsmjyquwrapecjikghtvdxl
    fdnbsmjyquwraqeclikghtvdxl
    fvnbsijyquwrapechikghtvdxl
    fovbsmjyquwsapeczikghqvdxl
    ffjbsmjyqgwrapeczikghtvdxl
    fonbsmjyquwrapeczvkhhivdxl
    forbamjjquwrapeczikghtvdxl
    fonbwmjyquwtapeyzikghtvdxl
    fonvsmjyquwrapeczikglnvdxl
    fonnsmjyguwrapeczikghtvxxl
    fopbsmjyquwrapeczikghtvaxz
    fonbsmjyquwiapeczikrhavdxl
    fonbsujyquwrapeczikthtvdjl
    fonpsmkyeuwrapeczikghtvdxl
    fonbsmjyquwrapeczqkgttvdxk
    fonbsmjyqzwrapeczikgrtddxl
    fokbsmjiquwrapeczikgltvdxl
    fonbsmjyqbwrapeczikghttdxo
    fonbsejyquwrapeczikghbvdal
    fonblmjyquwyaveczikghtvdxl
    fonbsmjyquwlzpepzikghtvdxl
    fonbsmjyqulrapbczigghtvdxl
    fonbsmjyxuwrapecziyghtvsxl
    fonbyjjyquwrapeczikghtvdxn
    fonbhmjyquwrapeczikghtjhxl
    fonbspjykuwraieczikghtvdxl
    aonbsmjyquwwapeczikchtvdxl
    fombsmjyquwyapeczikghtvdll
    fonbsmjynuwrapeczivgbtvdxl
    xonbsmjfquwrapeczikghqvdxl
    fonbyzjyquwzapeczikghtvdxl
    fbnbsmjyquwrapeczimgvtvdxl
    qonbsmjyquwraoeczikgftvdxl
    fonbsrjyquwrapeczikghtvjxm
    fonbsmjyquwrapxjzykghtvdxl
    fonbwgjyquwrapecziklhtvdxl
    fonjcmjyouwrapeczikghtvdxl
    fonbsmjyquwrapefzisuhtvdxl
    fonbsmjyqywrspeczikghtvnxl
    qonbsmjyquwrapeczlkuhtvdxl
    fonbsmjyqlprapeczikghtvdbl
    fonbsmjzquwrapedzikfhtvdxl
    fonbsmjyquwrapeczizghtvjxq
    fonbsmxyquwrrpeczikghtvcxl
    fonpsmjyquwoapeczikghjvdxl
    fonbshkyauwrapeczikghtvdxl
    fonbsmjysuwrapeczilghpvdxl
    fovwsxjyquwrapeczikghtvdxl
    fonbsmjyquwrppecnikghmvdxl
    fonbkmjyiuwrrpeczikghtvdxl
    gonbsmjyquwrapeczikphtudxl
    foncsmjyqlwrapeczimghtvdxl
    fonbsmjhquwrtpeczikghtvdxg
    fogbsmjyquarapeczikghtvdil
    fonbsmjyquwraperzekghwvdxl
    fonbstjyquwrapeczicghtedxl
    fonbsmjoquhrapeczikgotvdxl
    fonbsmjykuwrareczikgdtvdxl
    fonbsmjyvuwrayeczivghtvdxl
    fonbzmgyquwraptczikghtvdxl
    fonbsmjyqubrapeczikgftvdxb
    fonbgmjyjuwrapeczikghtvdul
    fonbsmjzqurrapeczikghtvfxl
    fonbsmjyiuwrapeczikgstvtxl
    fpnbstjyquwrapeczikghtvdcl
    fonbpmjyquwrapeczivghtndxl
    fonbsmjyquwrapeczilgptvvxl
    fonbsmjyqdwripecbikghtvdxl
    fonbsmjytuwgapnczikghtvdxl
    fonbsejyquwrapedzikghtvdml
    fonbsojyqdwrapeczikghtgdxl
    fonbsmjykuwrayeczicghtvdxl
    foubsmtyquwrapeczikchtvdxl
    fonbqmjyqukrapeyzikghtvdxl
    fonbsmjyquwaapenzikghtvdwl
    fonbsmeyquwrapeyzixghtvdxl
    fonusmjyquhrapeczikgytvdxl
    fonbsmjyquwrapwazikqhtvdxl
    fonwsmeyquwrapeczikghhvdxl
    fonmsmjyquxrspeczikghtvdxl
    fonqsmjyqxwrapeczikghtvdml
    fonfsmjyquwrapeuzikgatvdxl
    fonvsmjyquwrapeczikgrtvdul
    fonbsmayquwrapeczikihtvdxm
    fonbsmnyquwrapecdifghtvdxl
    fonbsmjyeuwraseczikghtvdxo
    fonbvvjyquwrapeczikghtvdxi
    fonbsmjyquwrapeczbkghtorxl
    tonbsmjyqvwrapeczikghtvdcl
    fonbsmjyquwrapeczhkgbtvdkl
    fonqsmjyquwrapenzibghtvdxl
    fontsmeyqudrapeczikghtvdxl
    qonbsmjyauwrapeczikghtvdbl
    fynbsmjyluwrapeczekghtvdxl
    fonbsmjhquwrappczikghtvdxt
    conbsmjyquwrapeczikahtvdxz
    fonbsmjyquorapeczikvftvdxl
    fonbsriyquwrapeczikchtvdxl
    yonfsmjyquwrapeczikghtvdxq
    fonaomjyquwrapecziwghtvdxl
    fonbsxsyqdwrapeczikghtvdxl
    fonbsqjyouwrapeczikgltvdxl
    fonbstsyquwraleczikghtvdxl
    fonbsmjyquwraoecztkghtvdsl
    fonbsmjyquwrapezzjkghmvdxl
    fonbwmjyqnwrapecpikghtvdxl
    fonbsmvyqbwrapeczikghtvdsl
    fonbsijyquwrazeczikghtvdwl
    fonbsmjyouwrapewzikghtldxl
    xonbsmjyqcwrapeczikghtvdul
    fonbgmjxquwrajeczikghtvdxl
    fokbsmjyquwrapechikghtrdxl
    fonbqmjyqawrapeczikghtrdxl
    fonbwmjzquwtapeyzikghtvdxl
    fonbsmjyquwrapecdikgatvdnl
    fonbsmjyqowrkpeczikghtvdxj
    fonbsmjyquwkapejzikuhtvdxl
    fonbsmjyquwrabeozikghtmdxl
    fonbsijyeuwrapeczikghtvdxh
    fonbsmjhquprapeczizghtvdxl
    fonesmjyquwrapcczikghtvdxh
    fonbamjyquwrapeczifrhtvdxl
    foabsmjyquwpapeczikghtvdxs
    fonbsmjyquwrapeczukghivdxh
    fonbsejyoulrapeczikghtvdxl
    fonbsmjyquwraceczikgdmvdxl
    eonbsmjyquerppeczikghtvdxl
    ffnzsmjyquwgapeczikghtvdxl
    donbsmyyquwrapeczirghtvdxl
    fjnbsmjyqufrapeczikghtwdxl
    fonfsmjyquwrareczigghtvdxl
    fonusmjyquwrapeczikgetvexl
    tonbsmjyqpwrapeczikghtjdxl
    fonbsmjhqukkapeczikghtvdxl
    fonbsmjyqusraseczikghtvzxl
    fonbsmjyquygapeczxkghtvdxl
    folbsmjyquwraqeczikghjvdxl
    fonbsmjyquwrppecjinghtvdxl
    fonbsmjyquwraepczhkghtvdxl
    fonbfmjyquwrapeczisghtrdxl
    fsnbsmjwqubrapeczikghtvdxl
    fonbspjyquwrapjczikghtedxl
    fowbsmjyquwrapeczikghtbdbl
    fonbymjyquwrapeczikghlvdrl
    fonbsmjyruwrapecbikghtvixl
    fonyqmjyqufrapeczikghtvdxl
    focbscjyquwrapeczmkghtvdxl
    fonbsmjyqtwnkpeczikghtvdxl
    eonbsmjyquwrameczizghtvdxl
    zonbsmjyqcwrapeczikghtvhxl
    foubsmjyquwrapehzikghtvnxl
    ffnbsmjyquwrapetzikghtjdxl
    fonbjgjyquwrapkczikghtvdxl
    fonbwmjyquwqapeczdkghtvdxl
    forbsmjyquwrapeczikkhtvdml
    fonbsmjyiuwrapeczivghevdxl
    fonbsmjyquwrapeglikghwvdxl
    fopgsmjyquwrapegzikghtvdxl
    fonbsmjyqzwrajeczikghtldxl
    fonbsmjyruwrapexzmkghtvdxl
    fonbsmjyquwrdpeczikxstvdxl
    fonbsmjyquwrapeezivghtvdql
    fonbdmjyqujsapeczikghtvdxl"""
    
    data = data.replace(" ", "")
    data = data.split("\n")
    twotot = 0
    threetot = 0
    for i in data:
        twotest = True
        threetest = True
        for j in i:
            a = lettercount(j, i)
            if (a == 2) and twotest:
                twotot += 1
                twotest = False
            if (a == 3) and threetest:
                threetot += 1
                threetest = False
            if not (twotest or threetest):
                break
    
    check = twotot * threetot
    print("***SECOND DAY***")
    print("Checksum: ", check)

    final = ""
    for i in range(len(data)):
        current = data.pop()
        for j in data:
            tup = stringcomp(current, j)
            if tup[0]:
                ind = tup[1]
                final = current[:ind] + current[ind+1:]
                break
        if not (final == ""):
            break
    
    print("Box ID: " + final)


