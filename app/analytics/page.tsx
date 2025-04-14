import MainLayout from '../components/layout/MainLayout';

export default function Analytics() {
  return (
    <MainLayout>
      <div className="py-10">
        <header>
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900">투자 분석</h1>
          </div>
        </header>
        <main>
          <div className="mx-auto max-w-7xl sm:px-6 lg:px-8">
            <div className="px-4 py-8 sm:px-0">
              <div className="bg-white shadow overflow-hidden sm:rounded-lg">
                <div className="px-4 py-5 sm:px-6">
                  <h3 className="text-lg leading-6 font-medium text-gray-900">AI 부동산 투자 분석 시스템</h3>
                  <p className="mt-1 max-w-2xl text-sm text-gray-500">딥러닝 알고리즘을 통한 투자 분석</p>
                </div>
                <div className="border-t border-gray-200 px-4 py-5 sm:p-6">
                  <div className="prose max-w-none">
                    <h2>AI 부동산 투자의 핵심 메커니즘</h2>
                    <h3>1. 데이터 수집 단계</h3>
                    <ul>
                      <li>부동산 등기정보(3.8억 건)</li>
                      <li>전세/월세 거래 이력(1.2억 건)</li>
                      <li>지역별 인프라 데이터(학교, 병원, 교통)</li>
                      <li>경제 지표(금리, 물가, 고용률)</li>
                    </ul>

                    <h3>2. 알고리즘 작동 원리</h3>
                    <pre className="bg-gray-100 p-4 rounded overflow-auto">
                      <code>
{`# 머신러닝 모델 학습 예시
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=500)
model.fit(X_train, y_train)
predictions = model.predict(X_test)`}
                      </code>
                    </pre>

                    <h3>3. 투자 결정 프로세스</h3>
                    <ol>
                      <li>지역별 <strong>공급-수요 균형 분석</strong></li>
                      <li>가격 변동성 패턴 식별</li>
                      <li>위험 요소(자연재해, 법규 변경) 평가</li>
                      <li>최적 매수 시점 예측</li>
                    </ol>
                    
                    <h2 className="mt-8">AI 프롬프트 활용 가이드</h2>
                    <div className="bg-gray-100 p-4 rounded mb-4">
                      <h4 className="mb-2">시장 분석</h4>
                      <p className="text-gray-700 font-mono">"2025년 2분기 서울 강남구 아파트 가격 변동 요인 5가지 분석 후 표로 작성"</p>
                    </div>
                    
                    <div className="bg-gray-100 p-4 rounded mb-4">
                      <h4 className="mb-2">계약서 검토</h4>
                      <p className="text-gray-700 font-mono">"다음 부동산 매매 계약서에서 위험 요소 3개 찾아 설명: [계약서 텍스트 삽입]"</p>
                    </div>
                    
                    <div className="bg-gray-100 p-4 rounded mb-4">
                      <h4 className="mb-2">투자 시뮬레이션</h4>
                      <p className="text-gray-700 font-mono">"5억 원 예산으로 3년 후 20% 수익률 달성 가능한 지역 추천 리스트 생성"</p>
                    </div>

                    <blockquote className="mt-6">
                      "AI는 도구일 뿐, 최종 결정은 인간의 판단이 필요합니다. 기술을 활용하되 투자의 본질을 잊지 마십시오." - 100억 자산가 CEO
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