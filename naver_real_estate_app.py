import sys
import json
import requests
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QPushButton, QLabel, QTableWidget, 
                               QTableWidgetItem, QComboBox, QLineEdit, QMessageBox,
                               QTabWidget, QGroupBox, QFormLayout, QSpinBox,
                               QSplitter, QTextEdit, QHeaderView, QProgressBar)
from PySide6.QtCore import Qt, Signal, QThread
from PySide6.QtGui import QFont, QColor

class DataFetcherThread(QThread):
    """Thread to fetch data from the Naver Real Estate API"""
    data_fetched = Signal(dict)
    error_occurred = Signal(str)
    progress_updated = Signal(int)

    def __init__(self, complex_id, trade_type="A1", year="5", area_no="2", data_type="summary"):
        super().__init__()
        self.complex_id = complex_id
        self.trade_type = trade_type
        self.year = year
        self.area_no = area_no
        self.data_type = data_type

    def run(self):
        try:
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
                'complexNo': self.complex_id,
                'tradeType': self.trade_type,
                'year': self.year,
                'areaNo': self.area_no,
                'type': self.data_type,
            }

            self.progress_updated.emit(25)
            url = f'https://new.land.naver.com/api/complexes/{self.complex_id}/prices'
            response = requests.get(url, params=params, cookies=cookies, headers=headers)
            self.progress_updated.emit(75)
            
            # Save to file
            json_data = response.json()
            with open('response_data.json', 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)
            
            self.progress_updated.emit(100)
            self.data_fetched.emit(json_data)
        
        except Exception as e:
            self.error_occurred.emit(str(e))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("네이버 부동산 데이터 분석기")
        self.setMinimumSize(1000, 700)
        
        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)
        
        # Create data fetcher tab
        self.create_data_fetcher_tab()
        
        # Create data viewer tab
        self.create_data_viewer_tab()
        
        # Analytics tab
        self.create_analytics_tab()
        
        self.setCentralWidget(main_widget)
        
        # Data storage
        self.current_data = None
        
        # Load data if exists
        self.try_load_existing_data()
        
    def try_load_existing_data(self):
        """Try to load existing data from file if it exists"""
        if os.path.exists('response_data.json'):
            try:
                with open('response_data.json', 'r', encoding='utf-8') as f:
                    self.current_data = json.load(f)
                    self.update_data_view()
                    self.update_analytics()
            except Exception as e:
                QMessageBox.warning(self, "데이터 로드 오류", f"기존 데이터를 로드하는 데 실패했습니다: {str(e)}")
    
    def create_data_fetcher_tab(self):
        """Create the data fetcher tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Form for data fetching parameters
        form_group = QGroupBox("API 요청 설정")
        form_layout = QFormLayout()
        
        # Complex ID
        self.complex_id_input = QLineEdit("97")  # Default from the script
        form_layout.addRow("복합 ID:", self.complex_id_input)
        
        # Trade Type
        self.trade_type_combo = QComboBox()
        self.trade_type_combo.addItems(["A1", "B1", "B2", "B3"])
        form_layout.addRow("거래 유형:", self.trade_type_combo)
        
        # Year
        self.year_input = QSpinBox()
        self.year_input.setRange(1, 20)
        self.year_input.setValue(5)  # Default from the script
        form_layout.addRow("연도:", self.year_input)
        
        # Area No
        self.area_no_input = QLineEdit("2")  # Default from the script
        form_layout.addRow("지역 번호:", self.area_no_input)
        
        # Type
        self.type_combo = QComboBox()
        self.type_combo.addItems(["summary", "table", "real"])
        form_layout.addRow("데이터 타입:", self.type_combo)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        # Fetch button
        fetch_button = QPushButton("데이터 가져오기")
        fetch_button.clicked.connect(self.fetch_data)
        layout.addWidget(fetch_button)
        
        # Response preview
        self.response_preview = QTextEdit()
        self.response_preview.setReadOnly(True)
        layout.addWidget(QLabel("응답 미리보기:"))
        layout.addWidget(self.response_preview)
        
        self.tab_widget.addTab(tab, "데이터 가져오기")
    
    def create_data_viewer_tab(self):
        """Create the data viewer tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Data table
        self.data_table = QTableWidget()
        self.data_table.setAlternatingRowColors(True)
        self.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(QLabel("거래 데이터:"))
        layout.addWidget(self.data_table)
        
        self.tab_widget.addTab(tab, "데이터 보기")
    
    def create_analytics_tab(self):
        """Create analytics tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Summary section
        summary_group = QGroupBox("요약 정보")
        summary_layout = QFormLayout()
        
        self.total_count_label = QLabel("0")
        summary_layout.addRow("총 거래 수:", self.total_count_label)
        
        self.avg_price_label = QLabel("0")
        summary_layout.addRow("평균 가격:", self.avg_price_label)
        
        self.min_price_label = QLabel("0")
        summary_layout.addRow("최저 가격:", self.min_price_label)
        
        self.max_price_label = QLabel("0")
        summary_layout.addRow("최고 가격:", self.max_price_label)
        
        self.price_trend_label = QLabel("데이터 없음")
        summary_layout.addRow("가격 추세:", self.price_trend_label)
        
        summary_group.setLayout(summary_layout)
        layout.addWidget(summary_group)
        
        # Additional stats could be added here
        
        self.tab_widget.addTab(tab, "분석")
    
    def fetch_data(self):
        """Fetch data from the API"""
        # Get parameters from inputs
        complex_id = self.complex_id_input.text()
        trade_type = self.trade_type_combo.currentText()
        year = str(self.year_input.value())
        area_no = self.area_no_input.text()
        data_type = self.type_combo.currentText()
        
        # Show progress
        self.progress_bar.setValue(10)
        
        # Create and start thread
        self.fetcher_thread = DataFetcherThread(
            complex_id=complex_id,
            trade_type=trade_type,
            year=year,
            area_no=area_no,
            data_type=data_type
        )
        self.fetcher_thread.data_fetched.connect(self.on_data_fetched)
        self.fetcher_thread.error_occurred.connect(self.on_fetch_error)
        self.fetcher_thread.progress_updated.connect(self.progress_bar.setValue)
        self.fetcher_thread.start()
    
    def on_data_fetched(self, data):
        """Handle fetched data"""
        self.current_data = data
        
        # Update response preview
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        self.response_preview.setText(json_str[:2000] + "..." if len(json_str) > 2000 else json_str)
        
        # Update data view and analytics
        self.update_data_view()
        self.update_analytics()
        
        # Switch to the data viewer tab
        self.tab_widget.setCurrentIndex(1)
        
        QMessageBox.information(self, "성공", "데이터를 성공적으로 가져왔습니다.")
    
    def on_fetch_error(self, error_message):
        """Handle fetch error"""
        QMessageBox.critical(self, "데이터 가져오기 오류", f"데이터를 가져오는 중 오류가 발생했습니다: {error_message}")
        self.progress_bar.setValue(0)
    
    def update_data_view(self):
        """Update the data view with current data"""
        if not self.current_data:
            return
        
        # Clear existing data
        self.data_table.clear()
        
        try:
            # Extract relevant data based on the structure of Naver Real Estate API response
            # This may need adjustment based on actual response structure
            if 'realPriceOnMonthList' in self.current_data:
                price_list = self.current_data['realPriceOnMonthList']
                if price_list and len(price_list) > 0:
                    # Get all data items
                    all_items = []
                    for month_data in price_list:
                        month = month_data.get('month', '')
                        year = month_data.get('year', '')
                        if 'itemList' in month_data:
                            for item in month_data['itemList']:
                                item['month'] = month
                                item['year'] = year
                                all_items.append(item)
                    
                    if all_items:
                        # Get headers from first item
                        headers = list(all_items[0].keys())
                        
                        # Set up table
                        self.data_table.setRowCount(len(all_items))
                        self.data_table.setColumnCount(len(headers))
                        self.data_table.setHorizontalHeaderLabels(headers)
                        
                        # Fill data
                        for row, item in enumerate(all_items):
                            for col, key in enumerate(headers):
                                value = item.get(key, '')
                                self.data_table.setItem(row, col, QTableWidgetItem(str(value)))
                        
                        # Adjust column widths
                        self.data_table.resizeColumnsToContents()
                        return
            
            # If we reach here, try alternative data format
            if 'average' in self.current_data:
                # Handle summary data format
                averages = self.current_data['average']
                self.data_table.setRowCount(len(averages))
                self.data_table.setColumnCount(5)  # Adjust based on your data
                self.data_table.setHorizontalHeaderLabels(
                    ["Date", "Average Price", "High", "Low", "Deal Count"]
                )
                
                for i, avg in enumerate(averages):
                    self.data_table.setItem(i, 0, QTableWidgetItem(f"{avg.get('date', '')}"))
                    self.data_table.setItem(i, 1, QTableWidgetItem(f"{avg.get('price', '')}"))
                    self.data_table.setItem(i, 2, QTableWidgetItem(f"{avg.get('highPrice', '')}"))
                    self.data_table.setItem(i, 3, QTableWidgetItem(f"{avg.get('lowPrice', '')}"))
                    self.data_table.setItem(i, 4, QTableWidgetItem(f"{avg.get('dealCount', '')}"))
            else:
                # Generic fallback display for unknown structure
                # Just show top-level keys and values
                rows = list(self.current_data.items())
                self.data_table.setRowCount(len(rows))
                self.data_table.setColumnCount(2)
                self.data_table.setHorizontalHeaderLabels(["Key", "Value"])
                
                for i, (key, value) in enumerate(rows):
                    self.data_table.setItem(i, 0, QTableWidgetItem(key))
                    # For complex values, show type instead of full value
                    if isinstance(value, (dict, list)):
                        val_str = f"{type(value).__name__} with {len(value)} items"
                    else:
                        val_str = str(value)
                    self.data_table.setItem(i, 1, QTableWidgetItem(val_str))
        
        except Exception as e:
            QMessageBox.warning(self, "데이터 표시 오류", f"데이터를 표시하는 중 오류가 발생했습니다: {str(e)}")
    
    def update_analytics(self):
        """Update analytics view with current data"""
        if not self.current_data:
            return
        
        try:
            # Extract prices for analysis
            prices = []
            dates = []
            
            # Try to find price data in different data structures
            if 'realPriceOnMonthList' in self.current_data:
                for month_data in self.current_data['realPriceOnMonthList']:
                    if 'itemList' in month_data:
                        for item in month_data['itemList']:
                            if 'dealPrice' in item:
                                # Convert to numeric value - handle price strings like "1억 2,000"
                                price_str = item['dealPrice']
                                
                                # Simple conversion - assumes price is just a number
                                try:
                                    # Remove non-numeric characters except '.'
                                    cleaned = ''.join(c for c in price_str if c.isdigit() or c == '.')
                                    price = float(cleaned) if cleaned else 0
                                    prices.append(price)
                                    
                                    # Store date for trend analysis
                                    date_str = f"{month_data.get('year', '')}.{month_data.get('month', '')}"
                                    dates.append((date_str, price))
                                except ValueError:
                                    pass
            
            elif 'average' in self.current_data:
                for avg_data in self.current_data['average']:
                    if 'price' in avg_data:
                        try:
                            price = float(avg_data['price'])
                            prices.append(price)
                            dates.append((avg_data.get('date', ''), price))
                        except (ValueError, TypeError):
                            pass
            
            # Update summary stats
            if prices:
                self.total_count_label.setText(str(len(prices)))
                self.avg_price_label.setText(f"{sum(prices)/len(prices):.2f}")
                self.min_price_label.setText(f"{min(prices):.2f}")
                self.max_price_label.setText(f"{max(prices):.2f}")
                
                # Simple trend analysis
                if len(dates) >= 2:
                    # Sort by date (assuming date format is sortable)
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
                    
                    self.price_trend_label.setText(f"{trend} ({pct_change:.2f}%)")
                else:
                    self.price_trend_label.setText("추세 분석에 데이터가 부족합니다")
            else:
                self.total_count_label.setText("0")
                self.avg_price_label.setText("데이터 없음")
                self.min_price_label.setText("데이터 없음")
                self.max_price_label.setText("데이터 없음")
                self.price_trend_label.setText("데이터 없음")
        
        except Exception as e:
            QMessageBox.warning(self, "분석 오류", f"데이터 분석 중 오류가 발생했습니다: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
