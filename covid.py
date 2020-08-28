
#21563..25384
S = "".join(["MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFR",
"SSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIR",
"GWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVY",
"SSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQ",
"GFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFL",
"LKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITN",
"LCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCF",
"TNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYN",
"YLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPY",
"RVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFG",
"RDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAI",
"HADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPR",
"RARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTM",
"YICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFG",
"GFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFN",
"GLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQN",
"VLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGA",
"ISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMS",
"ECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAH",
"FPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELD",
"SFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELG",
"KYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSE",
"PVLKGVKLHYT"])

# 25393..26220
orf3a = "".join(["MDLFMRIFTIGTVTLKQGEIKDATPSDFVRATATIPIQASLPFG",
"WLIVGVALLAVFQSASKIITLKKRWQLALSKGVHFVCNLLLLFVTVYSHLLLVAAGLE",
"APFLYLYALVYFLQSINFVRIIMRLWLCWKCRSKNPLLYDANYFLCWHTNCYDYCIPY",
"NSVTSSIVITSGDGTTSPISEHDYQIGGYTEKWESGVKDCVVLHSYFTSDYYQLYSTQ",
"LSTDTGVEHVTFFIYNKIVDEPEEHVQIHTIDGSSGVVNPVMEPIYDEPTTTTSVPL"])

# 26245..26472
E = "MYSFVSEETGTLIVNSVLLFLAFVVFLLVTLAILTALRLCAYCCNIVNVSLVKPSFYVYSRVKNLNSSRVPDLLV"

# 26523..27191
M = "".join(["MADSNGTITVEELKKLLEQWNLVIGFLFLTWICLLQFAYANRNR",
"FLYIIKLIFLWLLWPVTLACFVLAAVYRINWITGGIAIAMACLVGLMWLSYFIASFRL",
"FARTRSMWSFNPETNILLNVPLHGTILTRPLLESELVIGAVILRGHLRIAGHHLGRCD",
"IKDLPKEITVATSRTLSYYKLGASQRVAGDSGFAAYSRYRIGNYKLNTDHSSSSDNIALLVQ"])

#27202..27387
orf6 = "MFHLVDFQVTIAEILLIIMRTFKVSIWNLDYIINLIIKNLSKSLTENKYSQLDEEQPMEID"

#27394..27759
orf7a = "".join(["MKIILFLALITLATCELYHYQECVRGTTVLLKEPCSSGTYEGNS",
"PFHPLADNKFALTCFSTQFAFACPDGVKHVYQLRARSVSPKLFIRQEEVQELYSPIFL",
"IVAAIVFITLCFTLKRKTE"])

# 27894..28259
orf8 = "".join(["MKFLVFLGIITTVAAFHQECSLQSCTQHQPYVVDDPCPIHFYSK",
"WYIRVGARKSAPLIELCVDEAGSKSPIQYIDIGNYTVSCLPFTINCQEPKLGSLVVRC",
"SFYEDFLEYHDVRVVLDFI"])

#28274..29533
N = "".join(["MSDNGPQNQRNAPRITFGGPSDSTGSNQNGERSGARSKQRRPQG",
"LPNNTASWFTALTQHGKEDLKFPRGQGVPINTNSSPDDQIGYYRRATRRIRGGDGKMK",
"DLSPRWYFYYLGTGPEAGLPYGANKDGIIWVATEGALNTPKDHIGTRNPANNAAIVLQ",
"LPQGTTLPKGFYAEGSRGGSQASSRSSSRSRNSSRNSTPGSSRGTSPARMAGNGGDAA",
"LALLLLDRLNQLESKMSGKGQQQQGQTVTKKSAAEASKKPRQKRTATKAYNVTQAFGR",
"RGPEQTQGNFGDQELIRQGTDYKHWPQIAQFAPSASAFFGMSRIGMEVTPSGTWLTYT",
"GAIKLDDKDPNFKDQVILLNKHIDAYKTFPPTEPKKDKKKKADETQALPQRQKKQQTV",
"TLLPAADLDDFSKQLQQSMSSADSTQA"])

#29558..29674
orf10 = "MGYINVFAFPFTIYSLLLCRMNSRNYIAQVDVVNFNLT"

RC = {  ("CCU", "CCC","CCA","CCG"):"P",
        ("UUU","UUC"):"F",
        ("CAU","CAC"):"H",
        ("UUA","UUG","CUU","CUC","CUA","CUG"):"L",
        ("AUU","AUC","AUA"):"I", 
        ("GUU","GUC","GUA","GUG"):"V",
        ("UCU","UCC","UCA","UCG","AGU","AGC"):"S",
        ("CCU","CCC","CCA","CCG"):"P",
        ("ACU","ACC","ACA","ACG"):"T",
        ("UGG"):"W", 
        ("GCU","GCC","GCA","GCG"):"A",
        ("CAA","CAG"):"Q",
        ("AAU","AAC"):"N", 
        ("AAA","AAG"):"K",
        ("GAU","GAC"):"D",
        ("GAA","GAG"):"E", 
        ("UGU","UGC"):"C", 
        ("UAU","UAC"):"Y",
        ("CGU","CGC","CGA","CGG","AGA","AGG"):"R", 
        ("UCU","UCC","UCA","UCG","AGU","AGC"):"S", 
        ("GGU","GGC","GGA","GGG"):"G",
        ("AUG"):"M"}
testdict = {
    ("UUU", "UUC"):"F"
}

def translate(xlst):
    """
    INPUT an RNA list of letters
    RETURN a protein as a string of uppercase letters
    """
    # TODO: Implement function   
    remain = len(xlst)%3
    fullPro = ""
    for i in range(remain):
        xlst.pop(-1)
    while len(xlst) > 0:
        currpro = xlst[0]+xlst[1]+xlst[2]
        if len(xlst) == 3:
            break
        else:
            xlst.pop(0)
            xlst.pop(1)
            xlst.pop(2)
    print(fullPro)
    print(testdict["UUU"])
        
  

#variable to hold RNA sequence as a list
rna_seq = []


# Changes for this TODO go below this line
##################################################
# TODO: Get data from file
#       Translate DNA to RNA
alldna = open("FinalSpring2020/sequence.fasta", "r")
readdna = alldna.read()
readdna = readdna.replace("T", "U")
for i in readdna:
    if i != "\n":
        rna_seq.append(i)
for j in range(114):
    rna_seq.pop(0)
rna_seq.insert(0, " ")


##################################################
# Changes for this TODO go above this line


gene_list = [(21563, 25384, "S"),
(25393, 26220, "orf3a"),
(26245, 26472, "E"),
(26523,27191, "M"),
(27202,27387, "orf6"),
(27394, 27759, "orf7a"),
(27894, 28259, "orf8"),
(28274, 29533, "N"),
(29558, 29674, "orf10")]

for i in gene_list:
    x,y,gene_name = i

    #rna_seq is a list of RNA letters
    #and has been translated from DNA
    rna = rna_seq[x:y] 
	
	#call your function to take RNA and return protein
    protein = translate(rna)

    #displays gene name and whether your translation
    #is identical to gene found
    print(gene_name, protein == eval(gene_name))

