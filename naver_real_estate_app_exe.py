import os
import sys
import json
import requests
import webbrowser
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, make_response
import threading
import socket
import time
from werkzeug.serving import make_server
import pandas as pd
import io
from datetime import datetime

# Find an available port
def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

# Get the base directory for resources
if getattr(sys, 'frozen', False):
    # Running as compiled executable
    base_dir = sys._MEIPASS
else:
    # Running as script
    base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))
app.secret_key = 'naver_real_estate_analyzer_secret_key'

# Ensure data directory exists
data_dir = os.path.join(os.path.expanduser("~"), "naver_real_estate_data")
os.makedirs(data_dir, exist_ok=True)

@app.route('/')
def index():
    data_path = os.path.join(data_dir, 'response_data.json')
    data_exists = os.path.exists(data_path)
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
        
        # Updated headers with current timestamp
        current_timestamp = int(time.time())
        
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
            'REALESTATE': f'Mon Apr 14 2025 09:16:53 GMT+0900 (Korean Standard Time)',
            'mp_9c85fda7212d269ea46c3f6a57ba69ca_mixpanel': 'expired',
        }

        # Create a simulated token - these are examples and would need to be refreshed in a real app
        exp_time = current_timestamp + 10800  # Token valid for 3 hours
        auth_token = f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOnt7Y3VycmVudF90aW1lc3RhbXB9fSwiZXhwIjp7e2V4cF90aW1lfX0=.xyz123"
        auth_token = auth_token.replace("{{current_timestamp}}", str(current_timestamp)).replace("{{exp_time}}", str(exp_time))

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
            'authorization': f'Bearer {auth_token}',
            'priority': 'u=1, i',
            'referer': f'https://new.land.naver.com/complexes/{complex_id}?ms=37.53751,127.072592,17&a=APT:ABYG:JGC:PRE&b={trade_type}&e=RETAIL',
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
        
        # For demo purposes, create sample data if API call fails
        try:
            response = requests.get(url, params=params, cookies=cookies, headers=headers, timeout=10)
            response.raise_for_status()  # Raise exception for non-200 status codes
            json_data = response.json()
        except Exception as e:
            # If API call fails, create a sample response
            flash(f'네이버 API에서 실제 데이터를 가져올 수 없습니다: {str(e)}. 샘플 데이터를 사용합니다.', 'warning')
            json_data = create_sample_data(complex_id, trade_type, year)

        # Save to file
        data_path = os.path.join(data_dir, 'response_data.json')
        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        
        # Process data for the website
        flash('데이터를 성공적으로 가져왔습니다', 'success')
        return redirect(url_for('view_data'))
    
    except Exception as e:
        flash(f'데이터를 가져오는 중 오류가 발생했습니다: {str(e)}', 'error')
        return redirect(url_for('index'))

def create_sample_data(complex_id, trade_type, year):
    """Create sample data for demonstration purposes"""
    # Sample data structure similar to Naver Real Estate API
    year_int = int(year)
    current_year = 2025  # Simulated current year
    
    sample_data = {
        "complexNo": complex_id,
        "realPriceOnMonthList": []
    }
    
    # Create sample data for each month
    for y in range(current_year - year_int + 1, current_year + 1):
        for m in range(1, 13):
            # Skip future months for current year
            if y == current_year and m > 4:  # Assuming current month is April
                continue
                
            month_data = {
                "year": str(y),
                "month": f"{m:02d}",
                "itemList": []
            }
            
            # Add 1-5 transactions per month
            import random
            num_items = random.randint(1, 5)
            
            for i in range(num_items):
                # Generate random prices with an upward trend
                base_price = 80000 + (y - (current_year - year_int)) * 5000
                variation = random.randint(-2000, 2000)
                price = base_price + variation
                
                # Format price with Korean formatting
                price_str = f"{price:,}"
                
                item = {
                    "dealPrice": price_str,
                    "area": random.choice(["84.51", "109.23", "59.87", "122.14"]),
                    "floor": str(random.randint(1, 25)),
                    "dealType": "매매" if trade_type == "A1" else "전세" if trade_type == "B1" else "월세"
                }
                
                month_data["itemList"].append(item)
                
            sample_data["realPriceOnMonthList"].append(month_data)
    
    return sample_data

@app.route('/view_data')
def view_data():
    try:
        data_path = os.path.join(data_dir, 'response_data.json')
        if os.path.exists(data_path):
            with open(data_path, 'r', encoding='utf-8') as f:
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
            
            # If no data was found, create sample data
            if not table_data:
                flash('데이터 구조를 해석할 수 없습니다. 샘플 데이터를 표시합니다.', 'warning')
                # Create simple sample data
                table_data = [
                    {'year': '2025', 'month': '04', 'dealPrice': '85,000', 'area': '84.51', 'floor': '12', 'dealType': '매매'},
                    {'year': '2025', 'month': '03', 'dealPrice': '84,500', 'area': '84.51', 'floor': '8', 'dealType': '매매'},
                    {'year': '2025', 'month': '02', 'dealPrice': '83,800', 'area': '84.51', 'floor': '15', 'dealType': '매매'},
                    {'year': '2024', 'month': '12', 'dealPrice': '82,500', 'area': '84.51', 'floor': '10', 'dealType': '매매'},
                    {'year': '2024', 'month': '09', 'dealPrice': '81,200', 'area': '84.51', 'floor': '7', 'dealType': '매매'},
                    {'year': '2024', 'month': '06', 'dealPrice': '80,000', 'area': '84.51', 'floor': '5', 'dealType': '매매'},
                ]
                
                # Populate prices and dates for analytics
                for item in table_data:
                    try:
                        price_str = item['dealPrice']
                        cleaned = ''.join(c for c in price_str if c.isdigit() or c == '.')
                        price = float(cleaned) if cleaned else 0
                        prices.append(price)
                        dates.append((f"{item['year']}.{item['month']}", price))
                    except (ValueError, KeyError):
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

@app.route('/download-data/<format>')
def download_data(format):
    """
    데이터를 다운로드 하는 엔드포인트
    :param format: 다운로드 포맷 (csv, excel)
    :return: 파일 다운로드 응답
    """
    if 'data' not in session:
        flash('다운로드할 데이터가 없습니다.', 'danger')
        return redirect(url_for('index'))
    
    try:
        data = session['data']
        if not data:
            flash('다운로드할 데이터가 없습니다.', 'danger')
            return redirect(url_for('view_data'))
        
        # 데이터프레임 생성
        df = pd.DataFrame(data)
        
        # 현재 시간을 파일명에 추가
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if format == 'csv':
            # CSV 파일로 변환
            csv_data = df.to_csv(index=False, encoding='utf-8-sig')
            output = make_response(csv_data)
            output.headers["Content-Disposition"] = f"attachment; filename=naver_real_estate_data_{timestamp}.csv"
            output.headers["Content-type"] = "text/csv"
            return output
            
        elif format == 'excel':
            # 엑셀 파일로 변환
            excel_buffer = io.BytesIO()
            df.to_excel(excel_buffer, index=False, engine='openpyxl')
            excel_buffer.seek(0)
            
            response = make_response(excel_buffer.getvalue())
            response.headers["Content-Disposition"] = f"attachment; filename=naver_real_estate_data_{timestamp}.xlsx"
            response.headers["Content-type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            return response
            
        elif format == 'json':
            # JSON 파일로 변환
            json_data = df.to_json(orient='records', force_ascii=False)
            response = make_response(json_data)
            response.headers["Content-Disposition"] = f"attachment; filename=naver_real_estate_data_{timestamp}.json"
            response.headers["Content-type"] = "application/json"
            return response
            
        else:
            flash('지원하지 않는 포맷입니다.', 'danger')
            return redirect(url_for('view_data'))
            
    except Exception as e:
        flash(f'다운로드 중 오류가 발생했습니다: {str(e)}', 'danger')
        return redirect(url_for('view_data'))

class ServerThread(threading.Thread):
    def __init__(self, app, port):
        threading.Thread.__init__(self)
        self.server = make_server('127.0.0.1', port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

def run_app():
    # Get a free port
    port = find_free_port()
    
    # Create ServerThread
    server = ServerThread(app, port)
    server.daemon = True
    server.start()
    
    # Open web browser
    url = f"http://127.0.0.1:{port}"
    webbrowser.open(url)
    
    return server, port

if __name__ == '__main__':
    # Install pandas for Excel/CSV export
    try:
        import pandas
    except ImportError:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "openpyxl"])
    
    # Set up server
    server, port = run_app()
    
    # Display info in console
    print(f"네이버 부동산 데이터 분석기가 실행 중입니다.")
    print(f"웹 브라우저가 자동으로 열립니다.")
    print(f"URL: http://127.0.0.1:{port}")
    print("애플리케이션을 종료하려면 이 창을 닫으세요.")
    
    # Keep the app running
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("애플리케이션을 종료합니다...")
        server.shutdown() 