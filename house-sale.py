import requests

cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'index': '1',
    'representativeArticleNo': '2519415321',
}

response = requests.get('https://new.land.naver.com/api/articles', params=params, cookies=cookies, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:23:25.611Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"4a4c96bfacb24e96b51deb3832cb82be","init":false,"started":"2025-04-14T00:16:54.816Z","timestamp":"2025-04-14T00:23:25.625Z","status":"exited","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:23:25.612Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"d4af47942d3b43c689937ff866a211f1","init":true,"started":"2025-04-14T00:23:25.625Z","timestamp":"2025-04-14T00:23:25.625Z","status":"ok","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'complexNo': '',
}

response = requests.get('https://new.land.naver.com/api/articles/2519096962', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

response = requests.get('https://new.land.naver.com/api/pre-sale/1121510500', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

response = requests.get('https://new.land.naver.com/api/property/complex/13457/tour', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'pyeongTypeNumber': '6',
}

response = requests.get(
    'https://new.land.naver.com/api/property/complex/13457/vr/representative',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'p': 'adtl.apt.info',
    'rnd': 'l74459oeo6oe8',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'p': 'adtl.building',
    'rnd': 'l74459oeo6o4l',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'complexNo': '13457',
    'tradeType': 'A1',
    'year': '5',
    'areaNo': '6',
    'type': 'chart',
}

response = requests.get('https://new.land.naver.com/api/complexes/13457/prices', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

response = requests.get('https://new.land.naver.com/common/script/prismplayer-pc.js', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'dongNo': '1412830',
    'complexNo': '13457',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/13457/buildings/pyeongtype',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'dongNo': '1412830',
    'complexNo': '13457',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/13457/buildings/landprice',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20120124_143/land_system_1327405654690PkHmW_JPEG/112_13457_6_158H_GA1_1285553009573.jpg',
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'ff126_90',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20171028_245/rltr_profile_1509166002802u5YS5_JPEG/1509166002318_250.jpg',
    params=params,
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://finance-fe-static.pstatic.net/property-pc/v1/css/1744261667223/land.f232d90cf6b5d54ac8c6.css',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://finance-fe-static.pstatic.net/property-pc/v1/pc/img/icon_detail_logo--financial.svg',
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'p': 'adtl.apt.info',
    'rnd': 'l74459oeo6389',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oeo6oe8',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oeo6o4l',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'complexNo': '13457',
    'tradeType': 'A1',
    'year': '5',
    'areaNo': '6',
    'type': 'table',
}

response = requests.get('https://new.land.naver.com/api/complexes/13457/prices', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oeo6389',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 09 Jan 2025 06:40:15 GMT',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oeo6oe8',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oeo6o4l',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'complexNo': '13457',
    'tradeType': 'A1',
    'areaNo': '6',
    'type': 'table',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/13457/prices/real',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oeo6389',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oeo6oe8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oeo6o4l',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oeo6389',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

params = {
    'complexNo': '13457',
    'tradeType': 'A1',
    'year': '5',
    'areaNo': '6',
    'type': 'summary',
}

response = requests.get('https://new.land.naver.com/api/complexes/13457/prices', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=4, i',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oeo6oe8',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

data = '{"corp":"naverfinancial","svc":"land","location":"korea_real/korea","svc_tags":{},"send_ts":1744590208807,"tool":{"name":"ntm-web","ver":"nlogLibVersion=v0.1.43; verName=0.4; ntmVersion=v1.4.0"},"usr":{},"env":{"os":"MacIntel","br_ln":"en-US","br_sr":"0x0","device_sr":"822x847","platform_type":"web","device_pr":2,"timezone":"America/Los_Angeles","ch_pltf":"Android","ch_mob":true,"ch_mdl":"Nexus 5","ch_arch":"","ch_pltfv":"6.0","ch_fvls":[{"brand":"Google Chrome","version":"135.0.7049.85"},{"brand":"Not-A.Brand","version":"8.0.0.0"},{"brand":"Chromium","version":"135.0.7049.85"}]},"evts":[{"page_url":"https://new.land.naver.com/complexes?ms=37.1822883,127.0422939,10&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&p=map.dong","page_ref":"https://new.land.naver.com/complexes?ms=37.1822883,127.0422939,10&a=PRE:APT:OPST&b=A1&e=RETAIL&ad=true","page_id":"0f9fb9db4c7cd682a6a63121e222f2ef","timing":{"type":"navigate","unloadEventStart":0,"unloadEventEnd":0,"redirectStart":0,"redirectEnd":0,"workerStart":0,"fetchStart":16.30000000447035,"domainLookupStart":16.30000000447035,"domainLookupEnd":16.30000000447035,"connectStart":16.30000000447035,"secureConnectionStart":16.30000000447035,"connectEnd":16.30000000447035,"requestStart":37.399999998509884,"responseStart":196.5,"responseEnd":199.39999999850988,"domInteractive":2249.39999999851,"domContentLoadedEventStart":2249.39999999851,"domContentLoadedEventEnd":2249.60000000149,"domComplete":2774.89999999851,"loadEventStart":2775,"loadEventEnd":2775.39999999851},"type":"pageview","evt_ts":1744590208806}]}'

response = requests.post('https://nlog.naver.com/n', cookies=cookies, headers=headers, data=data)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=4, i',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oeo6o4l',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired',
}

data = '{"corp":"naverfinancial","svc":"land","location":"korea_real/korea","svc_tags":{},"send_ts":1744590208821,"tool":{"name":"ntm-web","ver":"nlogLibVersion=v0.1.43; verName=0.4; ntmVersion=v1.4.0"},"usr":{},"env":{"os":"MacIntel","br_ln":"en-US","br_sr":"0x0","device_sr":"822x847","platform_type":"web","device_pr":2,"timezone":"America/Los_Angeles","ch_pltf":"Android","ch_mob":true,"ch_mdl":"Nexus 5","ch_arch":"","ch_pltfv":"6.0","ch_fvls":[{"brand":"Google Chrome","version":"135.0.7049.85"},{"brand":"Not-A.Brand","version":"8.0.0.0"},{"brand":"Chromium","version":"135.0.7049.85"}]},"evts":[{"page_url":"https://new.land.naver.com/complexes?ms=37.1822883,127.0422939,10&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&p=map.dong","page_ref":"https://new.land.naver.com/complexes?ms=37.1822883,127.0422939,10&a=PRE:APT:OPST&b=A1&e=RETAIL&ad=true","page_id":"0f9fb9db4c7cd682a6a63121e222f2ef","timing":{"type":"navigate","unloadEventStart":0,"unloadEventEnd":0,"redirectStart":0,"redirectEnd":0,"workerStart":0,"fetchStart":17.19999999552965,"domainLookupStart":17.19999999552965,"domainLookupEnd":17.19999999552965,"connectStart":17.19999999552965,"secureConnectionStart":17.19999999552965,"connectEnd":17.19999999552965,"requestStart":27.799999997019768,"responseStart":218.89999999850988,"responseEnd":223.5,"domInteractive":2236.6999999955297,"domContentLoadedEventStart":2236.6999999955297,"domContentLoadedEventEnd":2237,"domComplete":2775.2999999970198,"loadEventStart":2775.2999999970198,"loadEventEnd":2775.6999999955297},"type":"pageview","evt_ts":1744590208820}]}'

response = requests.post('https://nlog.naver.com/n', cookies=cookies, headers=headers, data=data)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5409172',
    'bottomLat': '37.5341027',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5409172',
    'bottomLat': '37.5341027',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5409172',
    'bottomLat': '37.5341027',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.5409172&bottomLat=37.5341027&isPresale=true',
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5411384',
    'bottomLat': '37.5338815',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5411384',
    'bottomLat': '37.5338815',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5411384',
    'bottomLat': '37.5338815',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.5411384&bottomLat=37.5338815&isPresale=true',
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5416871',
    'bottomLat': '37.5333327',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5416871',
    'bottomLat': '37.5333327',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5416871',
    'bottomLat': '37.5333327',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.5416871&bottomLat=37.5333327&isPresale=true',
    cookies=cookies,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111797/50768@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111798/50768@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111799/50768@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111800/50768@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111801/50768@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111802/50768@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111803/50768@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111804/50768@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111805/50768@2x.png',
    params=params,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5420741',
    'bottomLat': '37.5329456',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5420741',
    'bottomLat': '37.5329456',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5420741',
    'bottomLat': '37.5329456',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.5420741&bottomLat=37.5329456&isPresale=true',
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5431885',
    'bottomLat': '37.531831',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5431885',
    'bottomLat': '37.531831',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5431885',
    'bottomLat': '37.531831',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.5431885&bottomLat=37.531831&isPresale=true',
    cookies=cookies,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111797/50774@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111798/50774@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111799/50774@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111800/50774@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111801/50774@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111802/50774@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111803/50774@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111804/50774@2x.png',
    params=params,
    headers=headers,
)


headers = {
    'Origin': 'https://new.land.naver.com',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

params = {
    'mt': 'bg.ol.sw.ar.lko',
}

response = requests.get(
    'https://map.pstatic.net/nrb/styles/basic/1744336608/17/111805/50774@2x.png',
    params=params,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5431758',
    'bottomLat': '37.5318438',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5431758',
    'bottomLat': '37.5318438',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5431758',
    'bottomLat': '37.5318438',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.5431758&bottomLat=37.5318438&isPresale=true',
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.543112',
    'bottomLat': '37.5319076',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.543112',
    'bottomLat': '37.5319076',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.543112',
    'bottomLat': '37.5319076',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.543112&bottomLat=37.5319076&isPresale=true',
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.542895',
    'bottomLat': '37.5321246',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.542895',
    'bottomLat': '37.5321246',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.542895',
    'bottomLat': '37.5321246',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.542895&bottomLat=37.5321246&isPresale=true',
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5427717',
    'bottomLat': '37.5322479',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5427717',
    'bottomLat': '37.5322479',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5427717',
    'bottomLat': '37.5322479',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.5427717&bottomLat=37.5322479&isPresale=true',
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5426568',
    'bottomLat': '37.5323628',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5426568',
    'bottomLat': '37.5323628',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5426568',
    'bottomLat': '37.5323628',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.5426568&bottomLat=37.5323628&isPresale=true',
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5426356',
    'bottomLat': '37.5323841',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/road/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5426356',
    'bottomLat': '37.5323841',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/rail/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'zoom': '17',
    'leftLon': '127.0635798',
    'rightLon': '127.0816042',
    'topLat': '37.5426356',
    'bottomLat': '37.5323841',
}

response = requests.get(
    'https://new.land.naver.com/api/developmentplan/jigu/list',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1121510500&zoom=17&priceType=RETAIL&markerId=13457&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=127.0635798&rightLon=127.0816042&topLat=37.5426356&bottomLat=37.5323841&isPresale=true',
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519096962',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'index': '14',
    'representativeArticleNo': '2519586749',
}

response = requests.get('https://new.land.naver.com/api/articles', params=params, cookies=cookies, headers=headers)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'f90_90',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20250410_168/17442789785192OQio_JPEG/%281%29KakaoTalk_20220405_110345635.jpg',
    params=params,
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'f90_90',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20250408_170/1744107194231wpJ1D_JPEG/%281%29KakaoTalk_20220405_110345635.jpg',
    params=params,
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'f90_90',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20250403_139/1743655775622zj8F4_JPEG/lg.jpg',
    params=params,
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:24:55.749Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"d4af47942d3b43c689937ff866a211f1","init":false,"started":"2025-04-14T00:23:25.625Z","timestamp":"2025-04-14T00:24:55.766Z","status":"exited","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:24:55.750Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"50d8a9fa9c2f4545973d7e682ce5b1c9","init":true,"started":"2025-04-14T00:24:55.766Z","timestamp":"2025-04-14T00:24:55.766Z","status":"ok","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '',
}

response = requests.get('https://new.land.naver.com/api/articles/2518802345', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/api/pre-sale/1121510500', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/api/property/complex/13457/tour', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'pyeongTypeNumber': '2',
}

response = requests.get(
    'https://new.land.naver.com/api/property/complex/13457/vr/representative',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'adtl.apt.info',
    'rnd': 'l74459oe96l33',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'adtl.building',
    'rnd': 'l74459oe96l39',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '13457',
    'tradeType': 'A1',
    'year': '5',
    'areaNo': '2',
    'type': 'chart',
}

response = requests.get('https://new.land.naver.com/api/complexes/13457/prices', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'dongNo': '1412828',
    'complexNo': '13457',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/13457/buildings/pyeongtype',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'dongNo': '1412828',
    'complexNo': '13457',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/13457/buildings/landprice',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20120124_108/land_system_1327405646777XCNYG_JPEG/112_13457_2_132J_GA1_1285552948685.jpg',
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'ff126_90',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20200515_227/rltr_profile_1589505802725ykJaL_JPEG/1589505802629_%B4%F5%BC%A5%BD%BA%C5%B8%BD%C3%C6%BC%B0%F8%C0%CE%C7%C1%B7%CE%C7%CA.jpg',
    params=params,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe96l33',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oe96l39',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'adtl.apt.info',
    'rnd': 'l74459oe96364',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '13457',
    'tradeType': 'A1',
    'year': '5',
    'areaNo': '2',
    'type': 'table',
}

response = requests.get('https://new.land.naver.com/api/complexes/13457/prices', params=params, cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe96l33',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe96364',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Wed, 02 Apr 2025 05:53:26 GMT',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe96l33',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oe96l39',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oe96l39',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '13457',
    'tradeType': 'A1',
    'areaNo': '2',
    'type': 'table',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/13457/prices/real',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe96364',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe96364',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/api/realtors/haw4002', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'realtorId': 'haw4002',
    'page': '1',
    'order': 'rank',
    'tradeType': '',
    'realEstateType': '',
    'isFixed': 'false',
}

response = requests.get('https://new.land.naver.com/api/articles', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'rdtl.info',
    'rnd': 'l74459oe97o73',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:24:57.191Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"50d8a9fa9c2f4545973d7e682ce5b1c9","init":false,"started":"2025-04-14T00:24:55.766Z","timestamp":"2025-04-14T00:24:57.208Z","status":"exited","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:24:57.192Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"bd2bb8889ac649dea633daa2054ba49b","init":true,"started":"2025-04-14T00:24:57.208Z","timestamp":"2025-04-14T00:24:57.208Z","status":"ok","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '13457',
    'tradeType': 'A1',
    'year': '5',
    'areaNo': '2',
    'type': 'summary',
}

response = requests.get('https://new.land.naver.com/api/complexes/13457/prices', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=rdtl.info&rnd=l74459oe97o73',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'ff126_90',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20140501_180/rltr_profile_1398917983376nUJcr_JPEG/1398917983204_haw4002_1363450205601.jpg',
    params=params,
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'type': 'm400_350',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20250405_121/1743820498116PPvth_JPEG/lg.jpg',
    params=params,
    headers=headers,
)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=rdtl.info&rnd=l74459oe97o73',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=rdtl.info&rnd=l74459oe97o73',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2518802345&realtorId=haw4002',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:24:58.853Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"bd2bb8889ac649dea633daa2054ba49b","init":false,"started":"2025-04-14T00:24:57.208Z","timestamp":"2025-04-14T00:24:58.870Z","status":"exited","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:24:58.853Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"20b55bc4327f4fba8235672d9c7f8a1e","init":true,"started":"2025-04-14T00:24:58.870Z","timestamp":"2025-04-14T00:24:58.870Z","status":"ok","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '',
}

response = requests.get('https://new.land.naver.com/api/articles/2519527713', params=params, cookies=cookies, headers=headers)


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/api/pre-sale/1121510500', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/api/property/complex/13457/tour', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'pyeongTypeNumber': '1',
}

response = requests.get(
    'https://new.land.naver.com/api/property/complex/97/vr/representative',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'adtl.apt.info',
    'rnd': 'l74459oe99eo4',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'adtl.building',
    'rnd': 'l74459oe99el8',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'captAreaYn': 'Y',
    'aptYn': 'Y',
    'grntEnstAmt': '300000000',
    'grntTrmStr': '20250312',
    'grntTrmEnd': '20270312',
}

response = requests.get(
    'https://new.land.naver.com/api/guarantee/expected-amount',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '97',
    'tradeType': 'B2',
    'year': '5',
    'provider': 'kbstar',
    'areaNo': '1',
    'addedRowCount': '0',
    'type': 'chart',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'dongNo': '183711',
    'complexNo': '97',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/97/buildings/pyeongtype',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'dongNo': '183711',
    'complexNo': '97',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/97/buildings/landprice',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20120124_252/land_system_1327401110403OJgcz_JPEG/112_97_1_82_GA1_1283409952580.jpg',
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'a': 'ARD.loan',
    'r': 'null',
    'i': 'null',
    'm': '0',
    'ssc': 'land.new_map',
    'u': 'about:blank',
}

response = requests.get('https://cc.naver.com/cc', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe99eo4',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oe99el8',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'a': 'ARD.loan',
    'r': 'null',
    'i': 'null',
    'm': '0',
    'ssc': 'land.new_map',
    'u': 'about:blank',
    'nt': '1744590299435',
}

response = requests.get('https://cc.naver.com/cc', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'adtl.apt.info',
    'rnd': 'l74459oe9944l',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'a': 'ARD.loan',
    'r': 'null',
    'i': 'null',
    'm': '0',
    'ssc': 'land.new_map',
    'u': 'about:blank',
    'nt': '1744590299446',
}

response = requests.get('https://cc.naver.com/cc', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'a': 'ARD.loan',
    'r': 'null',
    'i': 'null',
    'm': '0',
    'ssc': 'land.new_map',
    'u': 'about:blank',
    'nt': '1744590299508',
}

response = requests.get('https://cc.naver.com/cc', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '97',
    'tradeType': 'B2',
    'year': '5',
    'provider': 'kbstar',
    'areaNo': '1',
    'addedRowCount': '0',
    'type': 'table',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', params=params, cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe99eo4',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe99eo4',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe9944l',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oe99el8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '97',
    'tradeType': 'B2',
    'areaNo': '1',
    'type': 'table',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/97/prices/real',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459oe99el8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe9944l',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459oe9944l',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519527713&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '97',
    'tradeType': 'B2',
    'year': '5',
    'provider': 'kbstar',
    'areaNo': '1',
    'addedRowCount': '0',
    'type': 'summary',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', params=params, cookies=cookies, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:26:05.212Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"20b55bc4327f4fba8235672d9c7f8a1e","init":false,"started":"2025-04-14T00:24:58.870Z","timestamp":"2025-04-14T00:26:05.232Z","status":"exited","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://new.land.naver.com',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

params = {
    'sentry_key': 'fa86ed004bb0411ea9e3de5a8ff08224',
    'sentry_version': '7',
}

data = '{"sent_at":"2025-04-14T00:26:05.212Z","sdk":{"name":"sentry.javascript.browser","version":"6.19.7"}}\n{"type":"session"}\n{"sid":"74743521ef24467786fd47dccb5c4ea5","init":true,"started":"2025-04-14T00:26:05.232Z","timestamp":"2025-04-14T00:26:05.232Z","status":"ok","errors":0,"attrs":{"release":"space-web@2025.04.10","environment":"real","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry-fin.naver.com/api/97/envelope/', params=params, headers=headers, data=data)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '',
}

response = requests.get('https://new.land.naver.com/api/articles/2519528238', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/api/pre-sale/1121510500', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/api/property/complex/13457/tour', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'pyeongTypeNumber': '2',
}

response = requests.get(
    'https://new.land.naver.com/api/property/complex/97/vr/representative',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'adtl.apt.info',
    'rnd': 'l74459o366ool',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'adtl.building',
    'rnd': 'l74459o366oo6',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '97',
    'tradeType': 'A1',
    'year': '5',
    'areaNo': '2',
    'type': 'chart',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', params=params, cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'dongNo': '732978',
    'complexNo': '97',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/97/buildings/pyeongtype',
    params=params,
    cookies=cookies,
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'dongNo': '732978',
    'complexNo': '97',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/97/buildings/landprice',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://landthumb-phinf.pstatic.net/20120124_185/land_system_1327401112175NkrEF_JPEG/112_97_2_115_GA1_1283409975730.jpg',
    headers=headers,
)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459o366ool',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459o366oo6',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'p': 'adtl.apt.info',
    'rnd': 'l74459o366e35',
}

response = requests.get('https://new.land.naver.com/ndscheck.html', params=params, cookies=cookies, headers=headers)


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '97',
    'tradeType': 'A1',
    'year': '5',
    'areaNo': '2',
    'type': 'table',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', params=params, cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459o366ool',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'if-modified-since': 'Thu, 10 Apr 2025 05:08:00 GMT',
    'if-none-match': 'W/"633-1961e190b80"',
    'priority': 'u=1',
    'referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459o366e35',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

response = requests.get('https://new.land.naver.com/common/script/nlog.js', cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459o366oo6',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459o366ool',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.building&rnd=l74459o366oo6',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459o366e35',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/scripts/ntm_f7d39342464d.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '97',
    'tradeType': 'A1',
    'areaNo': '2',
    'type': 'table',
}

response = requests.get(
    'https://new.land.naver.com/api/complexes/97/prices/real',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://new.land.naver.com/ndscheck.html?p=adtl.apt.info&rnd=l74459o366e35',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
}

response = requests.get('https://ntm.pstatic.net/ex/nlog.js', headers=headers)


cookies = {
    'NNB': '7NU35FMWMTPGA',
    '__utmc': '163452323',
    'BMR': 's=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F',
    'NAC': 'Z9cXBMgKtQ1A',
    'NID_AUT': 'bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS',
    'NID_JKL': '63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=',
    'page_uid': 'i/YVTlqo1SCssvpnnu4ssssstbl-385514',
    'NACT': '1',
    'NID_SES': 'AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==',
    'SRT30': '1744589438',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '46DuggXsasaYbVoTU2hP04.1744589442362',
    'REALESTATE': 'Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
    'SRT5': '1744590209',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDQ1ODk4MTMsImV4cCI6MTc0NDYwMDYxM30.I15LRLPBja5e1pMYX1hwdF32ZqHUS6vhYWmsy3qJ7qc',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NNB=7NU35FMWMTPGA; __utmc=163452323; BMR=s=1675196890185&r=https%3A%2F%2Fm.blog.naver.com%2Ftaxtour4848%2F222280683971%3Fview%3Dimg_9&r2=https%3A%2F%2Ft.co%2F; NAC=Z9cXBMgKtQ1A; NID_AUT=bA3JvGx/OCwT19cDZP2u80pnR19fkv8dAgD7P+xQFmsL40V9WaeDoLYeAsnUpuJS; NID_JKL=63b0RQTdTe9IDMC6mslVi4uB7UHSRqS6kbm/SyZriIo=; page_uid=i/YVTlqo1SCssvpnnu4ssssstbl-385514; NACT=1; NID_SES=AAABryaReySuYvvKJt0jXqiER23mMFyfYZ8MWI78gpi7R8yKyE4pFTDtrXdb4/40SdzIsLMcrdVFs7tYfA/X9hcUKgyZmQ37/GpXrNIThyBdF5WXQiH90pwXAzrxZYS1Fq8LSbYPvGsl8zk+yKVTglRZ3BBdQbOxB1Tm9JehWLwSHyA0MAKtVhyYWeyS0NOLPA1SAPjGfbUFlB8fjjKfmGmHIGLndD3fdNgXCkDuPyQ0TNTdDxRl1rxGrv7TNFW7801Dm6iFRP3eFXHS4DfZPTZXBXsLRFoxi4XG6NHorjQPBvz/T/Ffnu8UmP0YBr62OzpoGjHN8O5nHbXNsWbD34U3cXO+HfDcu5aMpDIMUcCHbj3/YybkgBJs8oB7FKNX/eKlJfU5l2kJ7/sRYfLe/eeEQxOt/mEzp8RMXofMCQ0F95AGZGFUz2acantpjGhsJo7r5P/bFYxf63Js6OmGXMsQt9ga5cFxW6SoxB9VklW50D4+gIOz7om/cN6O1dPHQxJ2ZxCcdiPf9d9WR9RxOVoQ6zYbGvIf1OJGJJQxZFOD2/JnpcwvL+s58gsPTMfPzswjWA==; SRT30=1744589438; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; landHomeFlashUseYn=Y; _fwb=46DuggXsasaYbVoTU2hP04.1744589442362; REALESTATE=Mon%20Apr%2014%202025%2009%3A16%3A53%20GMT%2B0900%20(Korean%20Standard%20Time); mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel=expired; SRT5=1744590209',
}

params = {
    'complexNo': '97',
    'tradeType': 'A1',
    'year': '5',
    'areaNo': '2',
    'type': 'summary',
}

response = requests.get('https://new.land.naver.com/api/complexes/97/prices', params=params, cookies=cookies, headers=headers)
print(response.text)
# Save response to JSON file
import json
try:
    with open('response_data.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(response.text), f, ensure_ascii=False, indent=4)
    print('Response data saved to response_data.json')
except json.JSONDecodeError:
    print('Could not parse response as JSON')
    with open('response_data.txt', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print('Response data saved as plain text to response_data.txt')
