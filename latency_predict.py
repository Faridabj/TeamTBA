"""
Input: a row of 500 lagged log-returns, delimited by commas
Output: prediction of 1 if next-log return will be positive, 0 otherwise
"""
import sys
import numpy as np

COEFS = np.array([[-0.2355752345409834,0.0986764028123043,-0.08033563489216311,0.02022996596749721,-0.2452590493536127,0.15267273788095384,-0.1708881262353568,-0.08881433246901763,-0.08444730426345297,0.08034599325293913,0.14183521629101692,-0.05707590959601249,-0.1778276523026228,-0.15590813000459225,0.06363953490222184,-0.19020557294688736,0.03586774135272687,0.34344747603634085,-0.17131394638345174,0.13003223830686916,-0.22342667706653385,0.1828184879446713,-0.09715573014812082,0.10456806918962352,0.08945658322854241,-0.034553790271879124,0.06341516434923043,-0.13499596990453425,-0.19428630408452513,-0.05416831918462775,0.050675103956749575,0.005718021422519695,-0.14187493189183611,0.06892032874590058,-0.13520540748488963,0.1820646855327685,0.07408298372931447,0.05617525831878769,-0.04533414084929167,0.14518546829437673,-0.12181618065672278,0.23168970626554836,-0.06370611978672193,-0.03524817713504122,-0.006539578804633309,-0.11399857014045416,0.32772823550066577,0.47158295200858935,-0.005800726404588561,-0.16793024647970287,-0.43814398305937047,0.032839049821101855,-0.3686691146473387,-0.010527458646939776,-0.31052666944843976,0.05589304880301773,0.2165034918025523,0.04685862144101545,0.08487826755623225,0.046042161342525034,-0.11352828293342894,-0.023124214684728427,-0.04610304828141431,0.05643804206545558,-0.13585249442306302,0.18760238060229523,0.011626937054494526,-0.023316514028736298,-0.12509355493246957,-0.10705031639643708,0.09084363716333052,0.0727940559480482,-0.15668802688100977,0.09424680428597966,0.039723954039701255,-0.16058421308405416,0.02803817924780057,-0.3064557359782156,0.2398862645534476,0.13588604236929658,0.04148811952601,-0.008037251409042335,0.08496609124494225,0.0332686312293159,0.04243697781926341,0.08002974156714632,-0.07527721002737547,0.2718684664668527,0.09297990452084044,-0.0685816232217801,0.297457324148543,0.44094096685808637,-0.19025726222839037,0.38754693233776893,-0.2134204352745933,0.11490466049555831,0.05705353657934595,0.21050978534855894,0.04823819557848881,0.17505843795543855,-0.192695740551386,-0.15372622644214542,-0.05496860059266372,0.01624847391464853,-0.24078293533366676,0.1492340289047772,0.06496183170665097,0.04364570646450961,0.06895706659500431,-0.032865779412196976,-0.0072959836768663735,-0.008005851529068703,0.08622493932960527,-0.012659854618415432,0.13902126964973763,0.3381431510387155,-0.3346952779397621,0.09793599692025083,0.13121101617839256,0.2093855639897012,0.039183573539507556,0.26900642626061255,-0.027081537364674328,0.12676846432048172,-0.1000839335653877,-0.23081106482435493,-0.008652758352402678,0.06708091879639821,-0.24998759412303836,0.30444437167285,-0.004273327886283306,-0.30119466742655965,0.0856896988521012,0.060819476994124155,-0.17215699552122313,0.1602483257638588,-0.08515733027114175,-0.08786354897257773,0.11103749856631484,0.22346350991048405,-0.2880858709072011,-0.20016617908251289,-0.1558302923596275,-0.021811100939294854,-0.046270609434654976,-0.017891337385333734,-0.16673754208026365,0.05368606313560051,-0.3543418060865487,-0.10949688981555922,-0.42834865464720545,-0.13766132438095957,0.06395304254283138,0.5171967727698034,0.06785601043378499,0.11209357365470723,-0.19063535744666413,0.006451324451886686,-0.2078852866350848,-0.06680822256124715,-0.050419165557877794,-0.27062510464987405,0.21236942322746424,-0.318810500197803,0.17544727333970495,-0.23694487178155027,0.08611193132991905,0.16280771245725836,-0.18209581906066805,-0.10770167692834007,-0.30710043026179135,0.1499363555591125,-0.15918768922634643,-0.15630248136215769,0.004926182069690152,0.01735752411319183,-0.09126616355298475,0.19664001546006055,0.1334323489991432,0.3146004047590174,-0.22173229210140386,0.008924104118172196,0.12498488129606136,-0.03484682739064438,0.08698445968242341,-0.02870281145550796,0.18864147998717595,0.16705515991807746,-0.1973517955787085,0.18433512205323502,0.3505985576504645,0.13319272308627925,-0.20282569786859805,-0.017508621163221706,0.23331571786474542,-0.13612385965837775,-0.020667054019249672,-0.014696965409765752,-0.33898492772734556,-0.00828989064254151,0.512321545376076,0.1457150390032754,0.04681271067945393,-0.09069570042573777,-0.022600082911521328,-0.19693628589988238,0.1558942491309547,-0.15163150060106276,0.14991806515512826,0.08388322190881761,0.13697000058314532,0.11215193111225308,0.2618006989957401,-0.026915251554191697,-0.0028734376212006126,-0.0018222437800950572,-0.5923050677458476,-0.018255081317325037,-0.025093076663358537,0.25770054282050026,0.01330314214351924,0.2844279675095285,-0.4043923082517312,-0.2669881246003281,0.13866597983448228,-0.08013682258886774,-0.03412494469796844,0.011460371221878896,-0.029073044907987265,0.02452195575221969,0.02988782631650481,0.11253175341957479,-0.07489718664838711,-0.06931851655350343,-0.05582322480619271,-0.18627877379140703,-0.030853895431891435,-0.07566849234037903,0.14017750531855033,0.12002951306041042,-0.5387602610650208,0.11620338484373166,-0.35680546390172563,-0.36996230570899824,-0.09507966284376665,0.13520739664600576,0.0769824088284114,0.05802598125852906,0.07538758896011848,-0.03186949040909449,-0.19288581462156185,-0.07846815980678859,-0.04716685368268439,0.21415851960227023,0.013899911070549964,-0.19733899995735432,0.22741815558079517,0.1482268994264833,0.04542273046523418,-0.0654646345164034,-0.22831716615153153,-0.03701455021749444,-0.08161635177878897,0.15485069575912838,-0.21257931248000567,-0.23798157104450274,0.16543084520426338,-0.0342917007842597,0.08043895820421582,0.43117001405694444,-0.11499076530156625,-0.32972045374767556,0.22487767678251255,-0.04261810662857332,0.023034157616801568,0.1591750347434951,-0.29934604150042193,0.04240155743398199,0.20320019680039145,-0.14354813829690785,-0.07086142441699879,0.22674859210159476,0.13634649963690168,0.24179658455883568,-0.05785605212311279,0.3297779194546818,0.012252083804095832,0.1637377446731794,-0.14279913381447826,-0.06782939120917246,0.38322522183699315,0.2079061031604372,-0.09702862997720607,0.03844007152697283,-0.20865048731164665,-0.056817826369260804,0.1183816787977997,0.18365236935413393,0.20168006672845828,0.08285061049994993,0.12587039634391065,0.28778749778083274,-0.026935144739516737,-0.1576523719230701,-0.1412268472916615,-0.002916356828958046,-0.10594039705462686,0.11830552256368648,-0.044607571328050155,-0.07556146619134,0.2983795444691078,-0.09480329070635236,-0.09068578480757263,0.0324401911019012,-0.31398197456919025,0.09742421054652708,-0.45775703340813545,0.26506912392391757,-0.08001201109035641,-0.22997238429782102,0.28803001373615333,-0.049641828653215585,-0.31450986695471267,0.22972418949707482,0.04315613891801971,0.314890992559569,-0.06242162229668467,-0.1656846935795065,0.1937332756648762,-0.16187441160223393,0.002840122584662701,-0.026730978358210367,0.22137898660351074,-0.12406129698204534,0.16549630301734597,-0.13016317759118032,-0.23045852453702656,-0.15348682766748806,0.05429078955214371,0.026587372045983517,0.054294050619843624,-0.020294406059039857,-0.1864904767886676,0.4479136487774346,-0.0010762448798546736,0.23710684771791113,-0.06680150407417962,0.07735505961135493,-0.06286247468561561,-0.1110676420353775,-0.2037903621323946,-0.19544172513063976,0.16853583330554178,0.27783255271499485,0.44811929365315056,-0.21919244504058977,-0.10856467178627657,0.048733850180177854,-0.12346600169013024,-0.21869396216020245,-0.02270800316779925,0.04876416188184231,-0.2866929564063948,-0.028975947319020336,0.3335631256803877,0.11538870645850552,-0.16523525407139736,0.6468608540383409,0.04957859760011458,0.37264779818951504,-0.396598891608418,-0.009002976029382243,-0.04549868917384988,-0.34319928822965734,0.0704091968017773,-0.1187175231905119,0.2530108999551927,-0.1682142413389758,0.13283011322749566,0.22238275045546563,0.26710619033501454,0.3837310342616176,0.24274049577491377,-0.07011073506092723,-0.20296612595329885,0.25468566692907546,-0.21288331204835972,-0.08665151497303707,0.12701537888849715,0.055338492735991174,0.21948861242591952,0.09244339356292043,0.14802616792952109,-0.1929438635642549,-0.14149861394236035,-0.031151474269611176,0.39133572424105906,-0.19098374361958953,-0.03701158738167295,0.3410594812285875,-0.39297407507806165,0.5783363733287034,0.16066131209130755,0.023500797573716925,-0.24661149228936016,0.12979552639937852,0.0562157028402978,-0.03633129446950562,-0.252224862853239,0.10030914574290296,-0.2583598753661973,-0.06494686020210964,0.31545516068517554,-0.3092086557298757,0.04343218205397576,-0.124920642710312,0.23534491111078087,-0.2803677205795255,-0.2488084677236047,0.1734051599174528,0.22909431471473948,-0.11486817560445164,0.44269735165502405,0.000871036587215613,-0.0584176945343881,-0.3322005337130338,-0.06040232215906198,-0.3265012199095988,-0.26806625326602956,-0.08248098310839609,0.004648337516170914,-0.029333163881004914,-0.22186213532507185,0.22801669574187278,-0.07308316801399724,0.19809080135370793,0.1950662074669332,0.013625035777153112,-0.0031780026359946876,0.07766837493322393,-0.19791107821083465,0.1754404021457612,-0.25718214924310767,0.2004425545264216,-0.07961829092714082,-0.10630692070464481,-0.0004672469228409376,-0.10750762908540103,-0.0778838137810955,0.3784459053121952,-0.025730658324574125,-0.03954038026536595,-0.25365661111380333,0.12210165390729931,-0.1024210132309026,-0.17488456715274037,-0.03646470155486463,-0.11347626088479064,-0.08304405572868834,0.27633147872390207,-0.03555853627500632,0.34468893730517514,-0.08898020336047412,0.20298766871288904,0.21261571338702998,-0.04105684856792305,-0.11143227389753968,0.07307778261268534,-0.21689233233475091,-0.2747293551374313,-0.22913012753981807,0.12603029425895781,-0.36986742075099466,0.020810504500510058,0.1774889380042809,-0.09072342592120336,0.11316631676243558,-0.05045522676482911,-0.039799251912061295,0.2853055414038945,-0.33096021233136935,0.3814420448739055,-0.21697807994432208,0.08321248009763163,0.11281423434733845,-0.08017402293138218,-0.27689753407119794,0.3331329610449198,0.04835624992328108,0.16441782962885534,-0.27271800056472467,0.07005690894349566,0.23973187131448992,0.05887070434423597,-0.261070830456945,0.3223316397806494,-0.23834479401486267,0.28041909255538533,-0.16673667910302983,-0.3311416596967256]])

if __name__ == '__main__':
	# Read Data
	for line in sys.stdin:
		X_in = np.array([float(i) for i in line.split(",")]).reshape(1, -1)
		# p = 1 / (1 + np.exp(-(np.dot(X_in, COEFS.T) + 0.11098996)))
		p2 = ((np.dot(X_in, COEFS.T) + 0.11098996)[0][0] > 0) * 1
		print(p2)