import requests
import json

api_key="ee5b5e51acf636cd598a7552"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

print("1 {0} = {1} {2}".format(bozulan_doviz, sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))

'''
AFGANİSTAN	Afgan	AFN	971
AFRİKA GELİŞTİRME BANKASI GRUBU ÜYE ÜLKELERİ	ADB Hesap Birimi	XUA	965
ALAND ADALARI	Euro	EUR	978
ALMANYA	Euro	EUR	978
AMERİKA BİRLEŞİK DEVLETLERİ	Amerikan Doları	USD	840
AMERİKA BİRLEŞİK DEVLETLERİ	Amerikan Doları (Ertesi gün)	USN	997
AMERİKA BİRLEŞİK DEVLETLERİ KÜÇÜK DIŞ ADALARI	Amerikan Doları	USD	840
AMERİKAN SAMOASI	Amerikan Doları	USD	840
ANDORA	Euro	EUR	978
ANGOLA	Kwanza	AOA	973
ANGUİLLA	Doğu Karayip Doları	XCD	951
ANTARKTİKA	Evrensel para birimi yok		
ANTİGUA VE BARBUDA	Doğu Karayip Doları	XCD	951
ARJANTİN	Arjantin Pezosu	ARS	032
ARNAVUTLUK	Lek	ALL	008
ARUBA	Aruban Florin	AWG	533
AVRUPA BİRLİĞİ	Euro	EUR	978
AVUSTRALYA	Avustralya Doları	AUD	036
AVUSTURYA	Euro	EUR	978
AZERBAYCAN	Azerbaycan Manatı	AZN	944
BAHAMALAR	Bahama Doları	BSD	044
BAHREYN	Bahreyn Dinarı	BHD	048
BANGLADEŞ	Taka	BDT	050
BARBADOS	Barbados Doları	BBD	052
BATI SAHRA	Fas Dirhemi	MAD	504
BELARUS	Belarus Rublesi	BYR	974
BELİZE	Belize Doları	BZD	084
BELÇİKA	Euro	EUR	978
BENİN	CFA Frangı BCEAO	XOF	952
BERMUDA	Bermuda Doları	BMD	060
BİRLEŞİK ARAP EMİRLİKLERİ	BAE Dirhemi	AED	784
BOLİVYA	Bolivianosu	BOB	068
BOLİVYA	Mvdol	BOV	984
BONAİR, SINT EUSTATIUS VE SABA	Amerikan Doları	USD	840
BOSNA HERSEK	Çevirilebilir Mark	BAM	977
BOTSVANA	Pula	BWP	072
BREZİLYA	Brezilya Reali	BRL	986
BRUNEI DARUSSALAM	Brunei Doları	BND	096
BULGARİSTAN	Bulgar Levası	BGN	975
BURKİNA FASO	CFA Frangı BCEAO	XOF	952
BURUNDİ	Burundi Frangı	BIF	108
BUTAN	Ngultrum	BTN	064
BUTAN	Hint Rupisi	INR	356
BÜVETE ADASI	Norveç Kronu	NOK	578
BÜYÜK BRİTANYA BİRLEŞİK KRALLIĞI VE KUZEY İRLANDA	İngiliz Sterlini	GBP	826
CABO VERDE	Cabo Verde Escudo	CVE	132
CAYMAN ADALARI	Cayman Adaları Doları	KYD	136
CEBELİTARIK	Cebelitarık Lirası	GIP	292
CEZAYİR	Cezayir Dinarı	DZD	012
CİBUTİ	Cibuti Frangı	DJF	262
COCOS ADALARI	Avustralya Doları	AUD	036
COOK ADALARI	Yeni Zellanda Doları	NZD	554
CURACAO	Hollanda Antilleri Guilder	ANG	532
DANİMARKA	Danimarka Kronu	DKK	208
DOMİNİK	Doğu Karayip Doları	XCD	951
DOMİNİK CUMHURİYETİ	Dominik Pezosu	DOP	214
DOĞU TİMOR	Amerikan Doları	USD	840
EKVADOR	Amerikan Doları	USD	840
EKVATOR GİNESİ	CFA Frangı BEAC	XAF	950
EL SALVADOR	El Salvador Kolonu	SVC	222
EL SALVADOR	Amerikan Doları	USD	840
ENDONEZYA	Rupiah	IDR	360
ERİTRE	Nakfa	ERN	232
ERMENİSTAN	Ermeni Dram	AMD	051
ESTONYA	Euro	EUR	978
ETİYOPYA	Etiyopya Birri	ETB	230
FALKLAND ADALARI	Falkland Adaları Lirası	FKP	238
FAROE ADALARI	Danimarka Kronu	DKK	208
FAS	Fas Dirhemi	MAD	504
FİJİ	Fiji Doları	FJD	242
FİLDİŞİ SAHİLİ	CFA Frangı BCEAO	XOF	952
FİLİPİNLER	Filipin Pezosu	PHP	608
FİLİSTİN DEVLETİ	Evrensel para birimi yok		
FİNLANDİYA	Euro	EUR	978
FRANSA	Euro	EUR	978
FRANSIZ GUYANASI	Euro	EUR	978
FRANSIZ GÜNEY ÜLKELERİ	Euro	EUR	978
FRANSIZ POLİNEZYASI	CFP Frangı	XPF	953
GABON	CFA Frangı BEAC	XAF	950
GAMBİYA	Dalaş	GMD	270
GANA	Gana Cedi	GHS	936
GİNE	Gine Frangı	GNF	324
GİNE BİSAU	CFA Frangı BCEAO	XOF	952
GRENADA	Doğu Karayip Doları	XCD	951
GRÖNLAND	Danimarka Kronu	DKK	208
GUADALUP	Euro	EUR	978
GUAM	Amerikan Doları	USD	840
GUATEMALA	Quetzal	GTQ	320
GUERNSEY	İngiliz Sterlini	GBP	826
GUYANA	Guyana Doları	GYD	328
GÜNEY AFRİKA	Güney Afrika Parası	ZAR	710
GÜNEY GÜRCİSTAN VE GÜNEY SANDWICH ADALARI	Evrensel para birimi yok		
GÜNEY SUDAN	Güney Sudan Poundu	SSP	728
GÜRCİSTAN	Lari	GEL	981
HAİTİ	Gurdu	HTG	332
HAİTİ	Amerikan Doları	USD	840
HEARD ADASI VE McDONALD ADALARI	Avustralya Doları	AUD	036
HİNDİSTAN	Hint Rupisi	INR	356
HOLLANDA	Euro	EUR	978
HONDURAS	Lempira	HNL	340
HONG KONG	Hong Kong Doları	HKD	344
HIRVATİSTAN	Kuna	HRK	191
İNGİLİZ HİNT OKYANUSU TERRİTESİ	Amerikan Doları	USD	840
IRAK	Irak Dinarı	IQD	368
İRAN (İSLAM CUMHURİYETİ)	İran Riyali	IRR	364
İRLANDA	Euro	EUR	978
İSPANYA	Euro	EUR	978
İSRAİL	Yeni İsrail Şekeli	ILS	376
İSVEÇ	İsveç Kronu	SEK	752
İSVİÇRE	WIR Euro	CHE	947
İSVİÇRE	İsviçre Frangı	CHF	756
İSVİÇRE	WIR Frangı	CHW	948
İTALYA	Euro	EUR	978
İZLANDA	İzlanda Kronası	ISK	352
JAMAİKA	Jamaika Doları	JMD	388
JAPONYA	Yen	JPY	392
JERSEY	İngiliz Sterlini	GBP	826
KAMBOÇYA	Riel	KHR	116
KAMERUN	CFA Frangı BEAC	XAF	950
KANADA	Kanada Doları	CAD	124
KARADAĞ	Euro	EUR	978
KATAR	Katar Riyali	QAR	634
KAZAKİSTAN	Tenge	KZT	398
KENYA	Kenya Şilini	KES	404
KIBRIS	Euro	EUR	978
KİRİBATİ	Avustralya Doları	AUD	036
KOLOMBİYA	Kolombiya Pezosu	COP	170
KOLOMBİYA	Unidad de Valor Real	COU	970
KOMORLAR	Komor Frangı	KMF	174
KONGO	CFA Frangı BEAC	XAF	950
KONGO (DEMOKRATİK CUMHURİYETİ)	Kongo Frangı	CDF	976
KORE	Kuzey Kore Wonu	KPW	408
KORE (CUMHURİYETİ)	Won	KRW	410
KOSTA RİKA	Kosta Rika Kolonu	CRC	188
KUTSAL BAKIN	Euro	EUR	978
KUVEYT	Kuveyt Dinarı	KWD	414
KUZEY MARİANA ADALARI	Amerikan Doları	USD	840
KÜBA	Çevirilebilir Pezo	CUC	931
KÜBA	Küba Pezosu	CUP	192
KIRGIZİSTAN	Som	KGS	417
LAO DEMOKRATİK CUMHURİYETİ	Kip	LAK	418
LESOTO	Loti	LSL	426
LESOTO	Güney Afrika Parası	ZAR	710
LETONYA	Euro	EUR	978
LİBERYA	Liberya Doları	LRD	430
LİBYA	Libya Dinarı	LYD	434
LİHTENŞTAYN	İsviçre Frangı	CHF	756
LİTVANYA	Euro	EUR	978
LÜBNAN	Lübnan Poundu	LBP	422
LÜKSEMBURG	Euro	EUR	978
MACAO	Pataca	MOP	446
MACARİSTAN	Forint	HUF	348
MADAGASKAR	Madagaskar Ariary	MGA	969
MAKEDONYA (ESKİ YUGOSLAV CUMHURİYETİ)	Dinar	MKD	807
MALAWİ	Kvaça	MWK	454
MALDİVLER	Rufiyaa	MVR	462
MALEZYA	Malezya Ringiti	MYR	458
MALİ	CFA Frangı BCEAO	XOF	952
MALTA	Euro	EUR	978
MAN ADASI	İngiliz Sterlini	GBP	826
MARSHALL ADALARI	Amerikan Doları	USD	840
MARTİNİK	Euro	EUR	978
MAURITIUS	Mauritius Rupisi	MUR	480
MAYOTTE	Euro	EUR	978
MEKSİKA	Meksika Pezosu	MXN	484
MEKSİKA	Meksika Unidad de Inversion (UDI)	MXV	979
MİKRONEZYA FEDERE DEVLETLERİ	Amerikan Doları	USD	840
MISIR	Mısır Poundu	EGP	818
MOLDOVA (CUMHURİYETİ)	Moldova Leu	MDL	498
MONAKO	Euro	EUR	978
MONTSERRAT	Doğu Karayip Doları	XCD	951
MORİTANYA	Ouguiya	MRU	929
MOZAMBİK	Mozambik Metical	MZN	943
MOĞOLİSTAN	Tugriki	MNT	496
MYANMAR	Kyat	MMK	104
NAMİBYA	Namibya Doları	NAD	516
NAMİBYA	Güney Afrika Parası	ZAR	710
NAURU	Avustralya Doları	AUD	036
NEPAL	Nepal Rupisi	NPR	524
NİJER	CFA Frangı BCEAO	XOF	952
NİJERYA	Naira	NGN	566
NİKARAGUA	Cordoba Oro	NIO	558
NİUE	Yeni Zellanda Doları	NZD	554
NOEL ADASI	Avustralya Doları	AUD	036
NORFOLK ADASI	Avustralya Doları	AUD	036
NORVEÇ	Norveç Kronu	NOK	578
ORTA AFRİKA CUMHURİYETİ	CFA Frangı BEAC	XAF	950
PAKİSTAN	Pakistan Rupisi	PKR	586
PALAU	Amerikan Doları	USD	840
PANAMA	Balboa	PAB	590
PANAMA	Amerikan Doları	USD	840
PAPUA YENİ GİNE	Kina	PGK	598
PARAGUAY	Guarani	PYG	600
PERU	Nuevo Sol	PEN	604
POLONYA	Zloti	PLN	985
PORTEKİZ	Euro	EUR	978
PORTO RİKO	Amerikan Doları	USD	840
PITCAİRN	Yeni Zellanda Doları	NZD	554
ROMANYA	Romen Leyi	RON	946
RUANDA	Ruanda Frangı	RWF	646
RUSYA FEDERASYONU	Rus Rublesi	RUB	643
RÉUNION	Euro	EUR	978
SAINT BARTHÉLEMY	Euro	EUR	978
SAINT HELENA, ASCENSION ve TRISTAN DA CUNHA	Saint Helena Lirası	SHP	654
SAINT KITTS VE NEVIS	Doğu Karayip Doları	XCD	951
SAINT LUCIA	Doğu Karayip Doları	XCD	951
SAINT MARTIN (FRANSIZ TARAFI)	Euro	EUR	978
SAINT PIERRE VE MIQUELON	Euro	EUR	978
SAMOA	Tala	WST	882
SAN MARİNO	Euro	EUR	978
SAO TOME VE PRENSİP	Dobra	STN	930
SAINT VINCENT VE GRENADİNLER	Doğu Karayip Doları	XCD	951
SENEGAL	CFA Frangı BCEAO	XOF	952
SEYŞELLER	Seyşeller Rupisi	SCR	690
SIERRA LEONE	Leone	SLL	694
SİNGAPUR	Singapur Doları	SGD	702
SINT MAARTEN (DUTCH TARAFI)	Hollanda Antilleri Guilder	ANG	532
SISTEMA UNITARIO DE COMPENSACION REGIONAL DE PAGOS "SUCRE"	Sucre	XSU	994
SLOVAKYA	Euro	EUR	978
SLOVENYA	Euro	EUR	978
SOLOMON ADALARI	Solomon Adaları Doları	SBD	090
SOMALİ	Somali Şilini	SOS	706
SRİ LANKA	Sri Lanka Rupisi	LKR	144
SUDAN	Sudan Lirası	SDG	938
SURİNAM	Surinam Doları	SRD	968
SURİYE ARAP CUMHURİYETİ	Suriye Lirası	SYP	760
SUUDİ ARABİSTAN	Suudi Riyali	SAR	682
SVALBARD VE JAN MAYEN	Norveç Kronu	NOK	578
SVAZİLAND	Lilangeni	SZL	748
SIRBİSTAN	Sırp Dinarı	RSD	941
TACİKİSTAN	Somoni	TJS	972
TANZANYA BİRLEŞİK CUMHURİYETİ	Tanzanya Şilini	TZS	834
TAYLAND	Baht	THB	764
TAYVAN (ÇİN'İN EYALETİ)	Yeni Tayvan Doları	TWD	901
TOGO	CFA Frangı BCEAO	XOF	952
TOKELAU	Yeni Zellanda Doları	NZD	554
TONGA	Pa'anga	TOP	776
TRİNİDAD VE TOBAGO	Trinidad ve Tobago Doları	TTD	780
TUNUS	Tunus Dinarı	TND	788
TURKS VE CAİCOS ADALARI	Amerikan Doları	USD	840
TUVALU	Avustralya Doları	AUD	036
TÜRKİYE	Türk Lirası	TRY	949
TÜRKMENİSTAN	Türkmenistan Yeni Manat	TMT	934
UGANDA	Uganda Şilini	UGX	800
UKRAYNA	Grivna	UAH	980
ULUSLARARASI PARA FONU (IMF) 	SDR (Özel Çekme Hakkı)	XDR	960
UMMAN	Umman Riyali	OMR	512
URUGUAY	Uruguay Peso en Unidades Indexadas (URUIURUI)	UYI	940
URUGUAY	Uruguay Pezosu	UYU	858
VANUATU	Vatu	VUV	548
VENEZUELA (BOLİVARİSTAN CUMHURİYETİ)	Bolivar	VEF	937
VİETNAM	Dong	VND	704
VİRGİN ADALARI (A.B.D.)	Amerikan Doları	USD	840
VİRGİN ADALARI (İNGİLİZ)	Amerikan Doları	USD	840
WALLİS VE FUTUNA	CFP Frangı	XPF	953
YEMEN	Yemen Riyali	YER	886
YENİ KALEDONYA	CFP Frangı	XPF	953
YENİ ZELANDA	Yeni Zellanda Doları	NZD	554
YUNANİSTAN	Euro	EUR	978
ZAMBİYA	Zambiya Kvaçası	ZMW	967
ZİMBABVE	Zimbabve Doları	ZWL	932
ÇAD	CFA Frangı BEAC	XAF	950
ÇEK CUMHURİYETİ	Çek Korunası	CZK	203
ÇİN	Yuan Renminbi	CNY	156
ÖZBEKİSTAN	Özbekistan Sum	UZS	860
ÜRDÜN	Ürdün Dinarı	JOD	400
ŞİLİ	Unidad de Fomento	CLF	990
ŞİLİ	Şili Pezosu	CLP	152
'''