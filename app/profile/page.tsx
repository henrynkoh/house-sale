import MainLayout from '../components/layout/MainLayout';

export default function Profile() {
  return (
    <MainLayout>
      <div className="py-10">
        <header>
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900">내 프로필</h1>
          </div>
        </header>
        <main>
          <div className="mx-auto max-w-7xl sm:px-6 lg:px-8">
            <div className="px-4 py-8 sm:px-0">
              <div className="bg-white shadow overflow-hidden sm:rounded-lg">
                <div className="px-4 py-5 sm:px-6">
                  <div className="flex items-center">
                    <div className="h-16 w-16 rounded-full bg-indigo-100 flex items-center justify-center">
                      <svg className="h-10 w-10 text-indigo-500" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M24 20.993V24H0v-2.996A14.977 14.977 0 0112.004 15c4.904 0 9.26 2.354 11.996 5.993zM16.002 8.999a4 4 0 11-8 0 4 4 0 018 0z" />
                      </svg>
                    </div>
                    <div className="ml-4">
                      <h3 className="text-lg leading-6 font-medium text-gray-900">김투자</h3>
                      <p className="text-sm text-gray-500">AI 부동산 투자자</p>
                    </div>
                  </div>
                </div>
                <div className="border-t border-gray-200">
                  <dl>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">이메일</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">investor@example.com</dd>
                    </div>
                    <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">전화번호</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">010-1234-5678</dd>
                    </div>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">투자 유형</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">장기 투자</dd>
                    </div>
                    <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">투자 자금 규모</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">5억 ~ 10억</dd>
                    </div>
                    <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                      <dt className="text-sm font-medium text-gray-500">투자 목표</dt>
                      <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">자산 증식, 월 500만원 임대 수익</dd>
                    </div>
                  </dl>
                </div>
              </div>
              
              <div className="mt-8 bg-white shadow overflow-hidden sm:rounded-lg">
                <div className="px-4 py-5 sm:px-6">
                  <h3 className="text-lg leading-6 font-medium text-gray-900">나의 부동산 포트폴리오</h3>
                  <p className="mt-1 max-w-2xl text-sm text-gray-500">현재 보유 중인 부동산 자산</p>
                </div>
                <div className="border-t border-gray-200">
                  <div className="overflow-hidden overflow-x-auto">
                    <table className="min-w-full divide-y divide-gray-200">
                      <thead className="bg-gray-50">
                        <tr>
                          <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            매물
                          </th>
                          <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            매수가
                          </th>
                          <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            현재가
                          </th>
                          <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            수익률
                          </th>
                          <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            AI 추천 전략
                          </th>
                        </tr>
                      </thead>
                      <tbody className="bg-white divide-y divide-gray-200">
                        {properties.map((property) => (
                          <tr key={property.id}>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                              {property.name}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                              {property.purchasePrice}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                              {property.currentPrice}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                              <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${property.returnClass}`}>
                                {property.returnRate}
                              </span>
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                              {property.aiStrategy}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
              
              <div className="mt-8 bg-white shadow overflow-hidden sm:rounded-lg">
                <div className="px-4 py-5 sm:px-6">
                  <h3 className="text-lg leading-6 font-medium text-gray-900">AI 투자 분석 히스토리</h3>
                  <p className="mt-1 max-w-2xl text-sm text-gray-500">지난 6개월간 진행한 AI 분석 내역</p>
                </div>
                <div className="border-t border-gray-200">
                  <ul className="divide-y divide-gray-200">
                    {analysisHistory.map((item) => (
                      <li key={item.id} className="px-4 py-4 sm:px-6">
                        <div className="flex items-center justify-between">
                          <p className="text-sm font-medium text-indigo-600 truncate">{item.title}</p>
                          <div className="ml-2 flex-shrink-0 flex">
                            <p className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                              {item.date}
                            </p>
                          </div>
                        </div>
                        <div className="mt-2 sm:flex sm:justify-between">
                          <div className="sm:flex">
                            <p className="flex items-center text-sm text-gray-500">
                              {item.description}
                            </p>
                          </div>
                        </div>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </MainLayout>
  );
}

const properties = [
  {
    id: 1,
    name: '강남구 논현동 오피스텔',
    purchasePrice: '3억 8,000만원',
    currentPrice: '4억 2,000만원',
    returnRate: '+10.5%',
    returnClass: 'bg-green-100 text-green-800',
    aiStrategy: '3년 후 매각 권장',
  },
  {
    id: 2,
    name: '송파구 문정동 아파트',
    purchasePrice: '6억 5,000만원',
    currentPrice: '7억 2,000만원',
    returnRate: '+10.8%',
    returnClass: 'bg-green-100 text-green-800',
    aiStrategy: '유지 (재개발 예정)',
  },
  {
    id: 3,
    name: '부산시 해운대구 상가',
    purchasePrice: '4억 2,000만원',
    currentPrice: '3억 9,000만원',
    returnRate: '-7.1%',
    returnClass: 'bg-red-100 text-red-800',
    aiStrategy: '1년 내 매각 권장',
  },
];

const analysisHistory = [
  {
    id: 1,
    title: '용인시 수지구 투자 분석',
    date: '2023-12-15',
    description: '3년 뒤 약 35% 가격 상승 예상, 투자 적합',
  },
  {
    id: 2,
    title: '서울시 강남구 오피스텔 시장 분석',
    date: '2023-11-23',
    description: '단기 임대 수익률 5.8%, 장기 가치 상승 기대',
  },
  {
    id: 3,
    title: '전국 부동산 시장 트렌드 분석',
    date: '2023-10-05',
    description: '지방 중소도시 하락세, 수도권 상승세 지속 전망',
  },
  {
    id: 4,
    title: '포트폴리오 다각화 전략 분석',
    date: '2023-09-18',
    description: '오피스텔 40%, 아파트 40%, 상가 20% 배분 추천',
  },
]; 