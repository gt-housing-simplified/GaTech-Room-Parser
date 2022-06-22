# GaTech-Room-Parser

Used for displaying the number of beds left for GaTech housing.

The data is collected from https://housing.gatech.edu/available-rooms using an API call to https://housing.gatech.edu/rooms/FreeRooms.json?_=1655904358700

Example outputs:
```
Updated on: 2022-06-22 11:50:04
Using Config: {'gender': 'Male', 'capacity': 'Double', 'beds': False}

Fitten:          6
Glenn:           1
Towers:          2
Montag:          29
Freeman:         28
Harrison:        54
Hefner:          70
Armstrong:       36
Field:           29
Hopkins:         26
Hanson:          72
```
```
Updated on: 2022-06-22 15:40:03
Using Config: {'gender': 'Female', 'capacity': 'All', 'beds': True}

Fitten:          24
['FIT101a', 'FIT101b', 'FIT102a', 'FIT102b', 'FIT103a', 'FIT103b', 'FIT105a', 'FIT105b', 'FIT106a', 'FIT106b', 'FIT107a', 'FIT107b', 'FIT108a', 'FIT108b', 'FIT109a', 'FIT109b', 'FIT111a', 'FIT111b', 'FIT113a', 'FIT113b', 'FIT311a', 'FIT311b', 'FIT313a', 'FIT313b']
Glenn:           0
[]
Towers:          3
['TOW217d', 'TOW358b', 'TOW373c']
Montag:          66
['MON201a', 'MON201b', 'MON202a', 'MON202b', 'MON203a', 'MON203b', 'MON205a', 'MON205b', 'MON207a', 'MON207b', 'MON208a', 'MON208b', 'MON209a', 'MON209b', 'MON211a', 'MON211b', 'MON212a', 'MON212b', 'MON213a', 'MON213b', 'MON214a', 'MON214b', 'MON215a', 'MON215b', 'MON216a', 'MON216b', 'MON217a', 'MON217b', 'MON219a', 'MON219b', 'MON220a', 'MON220b', 'MON301a', 'MON301b', 'MON302a', 'MON302b', 'MON303a', 'MON303b', 'MON306a', 'MON306b', 'MON307a', 'MON307b', 'MON308a', 'MON308b', 'MON309a', 'MON309b', 'MON310a', 'MON310b', 'MON311a', 'MON311b', 'MON312a', 'MON312b', 'MON313a', 'MON313b', 'MON314a', 'MON314b', 'MON316a', 'MON316b', 'MON317a', 'MON317b', 'MON318a', 'MON318b', 'MON319a', 'MON319b', 'MON320a', 'MON320b']
Freeman:         64
['FRE201a', 'FRE201b', 'FRE202a', 'FRE202b', 'FRE205a', 'FRE205b', 'FRE207a', 'FRE207b', 'FRE208a', 'FRE208b', 'FRE209a', 'FRE209b', 'FRE210a', 'FRE210b', 'FRE211a', 'FRE211b', 'FRE213a', 'FRE213b', 'FRE214a', 'FRE214b', 'FRE216a', 'FRE216b', 'FRE217a', 'FRE217b', 'FRE219a', 'FRE219b', 'FRE220a', 'FRE220b', 'FRE301a', 'FRE301b', 'FRE302a', 'FRE302b', 'FRE303a', 'FRE303b', 'FRE305a', 'FRE305b', 'FRE306a', 'FRE306b', 'FRE307a', 'FRE307b', 'FRE308a', 'FRE308b', 'FRE309a', 'FRE309b', 'FRE311a', 'FRE311b', 'FRE312a', 'FRE312b', 'FRE313a', 'FRE313b', 'FRE314a', 'FRE314b', 'FRE315a', 'FRE315b', 'FRE316a', 'FRE316b', 'FRE317a', 'FRE317b', 'FRE318a', 'FRE318b', 'FRE319a', 'FRE319b', 'FRE320a', 'FRE320b']
Harrison:        20
['HRN206a', 'HRN206b', 'HRN207a', 'HRN207b', 'HRN207c', 'HRN207d', 'HRN210a', 'HRN210b', 'HRN210c', 'HRN210d', 'HRN216a', 'HRN216b', 'HRN216c', 'HRN216d', 'HRN219a', 'HRN219b', 'HRN219c', 'HRN219d', 'HRN228a', 'HRN228b']
Folk:            0
[]
Hefner:          32
['HEF101a', 'HEF101b', 'HEF102a', 'HEF102b', 'HEF103a', 'HEF103b', 'HEF104a', 'HEF104b', 'HEF105a', 'HEF105b', 'HEF108a', 'HEF108b', 'HEF109a', 'HEF109b', 'HEF110a', 'HEF110b', 'HEF111a', 'HEF111b', 'HEF112a', 'HEF112b', 'HEF113a', 'HEF113b', 'HEF114a', 'HEF114b', 'HEF115a', 'HEF115b', 'HEF116a', 'HEF116b', 'HEF117a', 'HEF117b', 'HEF118a', 'HEF118b']
Armstrong:       70
['ARM101a', 'ARM101b', 'ARM102a', 'ARM102b', 'ARM103a', 'ARM103b', 'ARM104a', 'ARM104b', 'ARM106a', 'ARM106b', 'ARM107a', 'ARM107b', 'ARM108a', 'ARM108b', 'ARM109a', 'ARM109b', 'ARM110a', 'ARM110b', 'ARM111a', 'ARM111b', 'ARM112a', 'ARM112b', 'ARM113a', 'ARM113b', 'ARM114a', 'ARM114b', 'ARM116a', 'ARM116b', 'ARM117a', 'ARM117b', 'ARM118a', 'ARM118b', 'ARM119a', 'ARM119b', 'ARM301a', 'ARM301b', 'ARM302a', 'ARM302b', 'ARM303a', 'ARM303b', 'ARM304a', 'ARM304b', 'ARM306a', 'ARM306b', 'ARM307a', 'ARM307b', 'ARM308a', 'ARM308b', 'ARM309a', 'ARM309b', 'ARM310a', 'ARM310b', 'ARM311a', 'ARM311b', 'ARM312a', 'ARM312b', 'ARM313a', 'ARM313b', 'ARM314a', 'ARM314b', 'ARM315a', 'ARM315b', 'ARM316a', 'ARM316b', 'ARM317a', 'ARM317b', 'ARM318a', 'ARM318b', 'ARM320a', 'ARM320b']
Field:           7
['FLD101a', 'FLD101b', 'FLD101c', 'FLD101d', 'FLD301c', 'FLD301d', 'FLD302b']
Hopkins:         4
['HOP101a', 'HOP101b', 'HOP301c', 'HOP301d']
Hanson:          1
['HAN112b']
Woodruff South:  76
['WDS103Bb', 'WDS106Aa', 'WDS106Ab', 'WDS106Ba', 'WDS106Bb', 'WDS203Ba', 'WDS203Bb', 'WDS208Aa', 'WDS208Ab', 'WDS208Ba', 'WDS208Bb', 'WDS214Aa', 'WDS214Ab', 'WDS301Ba', 'WDS301Bb', 'WDS303Ba', 'WDS303Bb', 'WDS305Aa', 'WDS305Ab', 'WDS305Ba', 'WDS305Bb', 'WDS313Aa', 'WDS313Ab', 'WDS313Ba', 'WDS313Bb', 'WDS317Aa', 'WDS317Ab', 'WDS317Ba', 'WDS317Bb', 'WDS404Aa', 'WDS404Ab', 'WDS410Ba', 'WDS410Bb', 'WDS413Aa', 'WDS413Ab', 'WDS413Ba', 'WDS413Bb', 'WDS416Aa', 'WDS416Ab', 'WDS416Ba', 'WDS416Bb', 'WDS419Aa', 'WDS419Ab', 'WDS419Ba', 'WDS419Bb', 'WDS420Aa', 'WDS420Ab', 'WDS420Ba', 'WDS420Bb', 'WDS503Ba', 'WDS503Bb', 'WDS503Bb', 'WDS506Aa', 'WDS506Ab', 'WDS506Ba', 'WDS506Bb', 'WDS510Ba', 'WDS510Bb', 'WDS513Aa', 'WDS513Ab', 'WDS513Ba', 'WDS513Bb', 'WDS514Aa', 'WDS514Ab', 'WDS514Ba', 'WDS514Bb', 'WDS515Aa', 'WDS515Ab', 'WDS515Ba', 'WDS515Bb', 'WDS516Aa', 'WDS516Ab', 'WDS516Ba', 'WDS516Bb', 'WDS518Ba', 'WDS518Bb']
Woodruff North:  90
['WDN101Bb', 'WDN101Bb', 'WDN107Aa', 'WDN107Ab', 'WDN107Ba', 'WDN107Bb', 'WDN201Aa', 'WDN201Ab', 'WDN201Ba', 'WDN201Bb', 'WDN205Aa', 'WDN205Ab', 'WDN205Ba', 'WDN205Bb', 'WDN206Aa', 'WDN206Ab', 'WDN206Ba', 'WDN206Bb', 'WDN214Aa', 'WDN214Ab', 'WDN214Ba', 'WDN214Bb', 'WDN215Aa', 'WDN215Ab', 'WDN215Ba', 'WDN215Bb', 'WDN219Aa', 'WDN219Ab', 'WDN219Ba', 'WDN219Bb', 'WDN305Ab', 'WDN305Ba', 'WDN305Bb', 'WDN308Ab', 'WDN308Ba', 'WDN308Bb', 'WDN310Bb', 'WDN310Bb', 'WDN313Aa', 'WDN313Ab', 'WDN313Ba', 'WDN313Bb', 'WDN315Aa', 'WDN315Ab', 'WDN315Ba', 'WDN315Bb', 'WDN401Aa', 'WDN401Ab', 'WDN401Ba', 'WDN401Bb', 'WDN404Aa', 'WDN404Ab', 'WDN404Ba', 'WDN404Bb', 'WDN407Ba', 'WDN407Bb', 'WDN410Ba', 'WDN410Bb', 'WDN415Aa', 'WDN415Ab', 'WDN415Ba', 'WDN415Bb', 'WDN419Aa', 'WDN419Ab', 'WDN419Ba', 'WDN419Bb', 'WDN504Aa', 'WDN504Ab', 'WDN504Ba', 'WDN504Bb', 'WDN505Ba', 'WDN505Bb', 'WDN508Aa', 'WDN508Ab', 'WDN508Ba', 'WDN508Bb', 'WDN510Ba', 'WDN510Bb', 'WDN513Aa', 'WDN513Ab', 'WDN513Ba', 'WDN513Bb', 'WDN518Aa', 'WDN518Ab', 'WDN518Ba', 'WDN518Bb', 'WDN520Aa', 'WDN520Ab', 'WDN520Ba', 'WDN520Bb']
Smith:           0
[]
Brown:           25
['BRN201a', 'BRN201b', 'BRN202a', 'BRN202b', 'BRN204a', 'BRN204b', 'BRN205a', 'BRN205b', 'BRN206a', 'BRN206b', 'BRN207a', 'BRN207b', 'BRN209a', 'BRN209b', 'BRN210a', 'BRN210b', 'BRN211a', 'BRN211b', 'BRN213a', 'BRN213b', 'BRN214a', 'BRN214b', 'BRN216a', 'BRN216b', 'BRN217b']
Caldwell:        0
[]
```
