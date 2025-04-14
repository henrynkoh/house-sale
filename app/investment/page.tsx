import MainLayout from '../components/layout/MainLayout';

export default function Investment() {
  return (
    <MainLayout>
      <div className="py-10">
        <header>
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900">투자 전략</h1>
          </div>
        </header>
        <main>
          <div className="mx-auto max-w-7xl sm:px-6 lg:px-8">
            <div className="px-4 py-8 sm:px-0">
              <div className="bg-white shadow overflow-hidden sm:rounded-lg">
                <div className="px-4 py-5 sm:px-6">
                  <h3 className="text-lg leading-6 font-medium text-gray-900">30단계 실전 투자 실행 매뉴얼</h3>
                  <p className="mt-1 max-w-2xl text-sm text-gray-500">AI를 활용한 부동산 투자 실행 단계</p>
                </div>
                <div className="border-t border-gray-200">
                  <dl>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">1단계: 시스템 설계</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                        <ul className="list-disc pl-5 space-y-1">
                          <li>AWS EC2 t3.xlarge 인스턴스 생성</li>
                          <li>PostgreSQL 데이터베이스 구축</li>
                          <li>Python 3.8 환경 설정</li>
                          <li>TensorFlow 2.4 설치</li>
                        </ul>
                      </dd>
                    </div>
                    <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">2단계: 데이터 준비</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                        <ul className="list-disc pl-5 space-y-1">
                          <li>공공데이터포털 API 키 발급</li>
                          <li>부동산 실거래가 API 연동</li>
                          <li>지리정보 시스템(GIS) 데이터 수집</li>
                        </ul>
                        <div className="mt-2 bg-gray-100 p-3 rounded">
                          <code className="text-xs">
                            curl -X GET "https://api.realestate.co.kr/v1/prices?region=seoul&type=apt"
                          </code>
                        </div>
                      </dd>
                    </div>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">3단계: 모델 개발</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                        <ul className="list-disc pl-5 space-y-1">
                          <li>LSTM 신경망 구조 설계</li>
                          <li>Hyperparameter 튜닝(학습률 0.001, 배치 크기 64)</li>
                          <li>3년 치 역사적 데이터 학습</li>
                        </ul>
                      </dd>
                    </div>
                    <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">4단계: 실시간 분석</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                        <ul className="list-disc pl-5 space-y-1">
                          <li>Airflow를 이용한 일일 배치 작업 설정</li>
                          <li>Slack API 연동으로 알림 시스템 구축</li>
                          <li>매일 오전 7시 자동 리포트 생성</li>
                        </ul>
                      </dd>
                    </div>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">5단계: 현장 검증</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                        <ul className="list-disc pl-5 space-y-1">
                          <li>추천 지역 방문 계획 수립</li>
                          <li>현지 부동산 중개사와 협업 체계 구축</li>
                          <li>물건 실사 시 드론 촬영 활용</li>
                        </ul>
                      </dd>
                    </div>
                  </dl>
                </div>
              </div>
              
              <div className="mt-8 bg-white shadow overflow-hidden sm:rounded-lg">
                <div className="px-4 py-5 sm:px-6">
                  <h3 className="text-lg leading-6 font-medium text-gray-900">투자 포트폴리오 관리</h3>
                  <p className="mt-1 max-w-2xl text-sm text-gray-500">장기적인 자산 관리 방안</p>
                </div>
                <div className="border-t border-gray-200 px-4 py-5 sm:p-6">
                  <div className="prose max-w-none">
                    <h3>포트폴리오 관리</h3>
                    <ol>
                      <li>위험 분산을 위한 지역별 자산 배분</li>
                      <li>6개월 주기 재평가</li>
                      <li>매각 시기 결정을 위한 지표 설정</li>
                    </ol>
                    
                    <h3 className="mt-6">투자 실행 시 고려사항</h3>
                    <p>
                      계약서 검토용 AI 도구를 적용하여 위험 요소를 사전에 파악하고, 
                      최적의 자금 조달 계획을 수립하는 것이 중요합니다.
                    </p>
                    <div className="bg-gray-100 p-3 rounded mt-2">
                      <code className="text-xs">
                        from transformers import pipeline<br />
                        contract_analyzer = pipeline("text-classification", model="contract-review-v2")
                      </code>
                    </div>
                    
                    <blockquote className="mt-6">
                      초기 단계에서는 소규모 자본으로 테스트 진행 후 점진적으로 확장할 것을 권장합니다.
                    </blockquote>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </MainLayout>
  );
} 