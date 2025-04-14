import os
import json
import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'naver_real_estate_analyzer_secret_key'

# Ensure templates folder exists
os.makedirs('templates', exist_ok=True)

@app.route('/')
def index():
    data_exists = os.path.exists('response_data.json')
    return render_template('index.html', data_exists=data_exists)

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    try:
        # Get form data
        complex_id = request.form.get('complex_id', '97')
        trade_type = request.form.get('trade_type', 'A1')
        year = request.form.get('year', '5')
        area_no = request.form.get('area_no', '2')
        data_type = request.form.get('data_type', 'summary')
        
        # Headers from the original script
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
            'nhn.realestate.article.rlet_type_cd': 'A1',
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
            'referer': 'https://new.land.naver.com/complexes/13457?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true&articleNo=2519528238&realtorId=haw4002',
            'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
        }

        params = {
            'complexNo': complex_id,
            'tradeType': trade_type,
            'year': year,
            'areaNo': area_no,
            'type': data_type,
        }

        url = f'https://new.land.naver.com/api/complexes/{complex_id}/prices'
        response = requests.get(url, params=params, cookies=cookies, headers=headers)
        
        # Save to file
        json_data = response.json()
        with open('response_data.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        
        # Process data for the website
        flash('데이터를 성공적으로 가져왔습니다', 'success')
        return redirect(url_for('view_data'))
    
    except Exception as e:
        flash(f'데이터를 가져오는 중 오류가 발생했습니다: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/view_data')
def view_data():
    try:
        if os.path.exists('response_data.json'):
            with open('response_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Extract table data and analytics
            table_data = []
            prices = []
            dates = []
            
            # Try to find price data in different data structures
            if 'realPriceOnMonthList' in data:
                for month_data in data['realPriceOnMonthList']:
                    if 'itemList' in month_data:
                        month = month_data.get('month', '')
                        year = month_data.get('year', '')
                        
                        for item in month_data['itemList']:
                            item_data = {
                                'year': year,
                                'month': month,
                            }
                            
                            # Copy all data from item
                            for key, value in item.items():
                                item_data[key] = value
                            
                            table_data.append(item_data)
                            
                            # Extract price for analytics
                            if 'dealPrice' in item:
                                try:
                                    price_str = item['dealPrice']
                                    cleaned = ''.join(c for c in price_str if c.isdigit() or c == '.')
                                    price = float(cleaned) if cleaned else 0
                                    prices.append(price)
                                    dates.append((f"{year}.{month}", price))
                                except ValueError:
                                    pass
            
            elif 'average' in data:
                for avg_data in data['average']:
                    table_data.append(avg_data)
                    
                    if 'price' in avg_data:
                        try:
                            price = float(avg_data['price'])
                            prices.append(price)
                            dates.append((avg_data.get('date', ''), price))
                        except (ValueError, TypeError):
                            pass
            
            # Generate analytics
            analytics = {
                'total_count': len(prices),
                'avg_price': sum(prices) / len(prices) if prices else 0,
                'min_price': min(prices) if prices else 0,
                'max_price': max(prices) if prices else 0,
                'trend': 'N/A'
            }
            
            # Calculate trend
            if len(dates) >= 2:
                sorted_dates = sorted(dates, key=lambda x: x[0])
                first_price = sorted_dates[0][1]
                last_price = sorted_dates[-1][1]
                
                if last_price > first_price:
                    trend = "상승"
                    pct_change = (last_price - first_price) / first_price * 100
                elif last_price < first_price:
                    trend = "하락"
                    pct_change = (first_price - last_price) / first_price * 100
                else:
                    trend = "유지"
                    pct_change = 0
                
                analytics['trend'] = f"{trend} ({pct_change:.2f}%)"
            
            # Determine headers dynamically
            headers = []
            if table_data:
                headers = list(table_data[0].keys())
            
            return render_template('view_data.html', 
                                  data=table_data, 
                                  headers=headers, 
                                  analytics=analytics,
                                  raw_data=json.dumps(data, ensure_ascii=False, indent=2))
        else:
            flash('데이터 파일이 없습니다. 먼저 데이터를 가져오세요.', 'warning')
            return redirect(url_for('index'))
    
    except Exception as e:
        flash(f'데이터를 표시하는 중 오류가 발생했습니다: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
