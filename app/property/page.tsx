import MainLayout from '../components/layout/MainLayout';

export default function Property() {
  return (
    <MainLayout>
      <div className="py-10">
        <header>
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900">부동산 검색</h1>
          </div>
        </header>
        <main>
          <div className="mx-auto max-w-7xl sm:px-6 lg:px-8">
            <div className="px-4 py-8 sm:px-0">
              {/* Search Form */}
              <div className="bg-white shadow overflow-hidden sm:rounded-lg mb-8">
                <div className="px-4 py-5 sm:p-6">
                  <div className="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                    <div className="sm:col-span-2">
                      <label htmlFor="region" className="block text-sm font-medium text-gray-700">
                        지역
                      </label>
                      <div className="mt-1">
                        <select
                          id="region"
                          name="region"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                        >
                          <option>전체</option>
                          <option>서울특별시</option>
                          <option>경기도</option>
                          <option>인천광역시</option>
                          <option>부산광역시</option>
                        </select>
                      </div>
                    </div>

                    <div className="sm:col-span-2">
                      <label htmlFor="property-type" className="block text-sm font-medium text-gray-700">
                        매물 유형
                      </label>
                      <div className="mt-1">
                        <select
                          id="property-type"
                          name="property-type"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                        >
                          <option>전체</option>
                          <option>아파트</option>
                          <option>오피스텔</option>
                          <option>단독주택</option>
                          <option>상가</option>
                        </select>
                      </div>
                    </div>

                    <div className="sm:col-span-2">
                      <label htmlFor="price-range" className="block text-sm font-medium text-gray-700">
                        가격대
                      </label>
                      <div className="mt-1">
                        <select
                          id="price-range"
                          name="price-range"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                        >
                          <option>전체</option>
                          <option>1억 이하</option>
                          <option>1억-5억</option>
                          <option>5억-10억</option>
                          <option>10억 이상</option>
                        </select>
                      </div>
                    </div>

                    <div className="sm:col-span-4">
                      <label htmlFor="keywords" className="block text-sm font-medium text-gray-700">
                        키워드
                      </label>
                      <div className="mt-1">
                        <input
                          type="text"
                          name="keywords"
                          id="keywords"
                          placeholder="역세권, 학군, 신축 등 키워드 입력"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                        />
                      </div>
                    </div>

                    <div className="sm:col-span-2">
                      <label htmlFor="ai-score" className="block text-sm font-medium text-gray-700">
                        AI 추천 점수
                      </label>
                      <div className="mt-1">
                        <select
                          id="ai-score"
                          name="ai-score"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                        >
                          <option>전체</option>
                          <option>90점 이상</option>
                          <option>80점 이상</option>
                          <option>70점 이상</option>
                        </select>
                      </div>
                    </div>
                  </div>
                  <div className="mt-6">
                    <button
                      type="button"
                      className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                    >
                      검색하기
                    </button>
                  </div>
                </div>
              </div>

              {/* Property Results */}
              <div className="bg-white shadow overflow-hidden sm:rounded-lg">
                <div className="px-4 py-5 sm:px-6 flex justify-between items-center">
                  <div>
                    <h3 className="text-lg leading-6 font-medium text-gray-900">AI 분석 부동산 매물</h3>
                    <p className="mt-1 max-w-2xl text-sm text-gray-500">총 153개의 매물이 검색되었습니다.</p>
                  </div>
                  <div>
                    <select className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md">
                      <option>AI 추천순</option>
                      <option>가격 높은순</option>
                      <option>가격 낮은순</option>
                      <option>수익률 높은순</option>
                    </select>
                  </div>
                </div>
                <div className="border-t border-gray-200">
                  <ul className="divide-y divide-gray-200">
                    {properties.map((property) => (
                      <li key={property.id} className="px-4 py-4 sm:px-6 hover:bg-gray-50">
                        <div className="flex items-center justify-between">
                          <div className="flex items-center">
                            <div className="flex-shrink-0 h-20 w-20 bg-gray-200 rounded"></div>
                            <div className="ml-4">
                              <div className="text-sm font-medium text-indigo-600">{property.name}</div>
                              <div className="text-sm text-gray-900 mt-1">{property.price}</div>
                              <div className="text-xs text-gray-500 mt-1">{property.address}</div>
                              <div className="flex mt-2">
                                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 mr-2">
                                  AI 점수: {property.aiScore}
                                </span>
                                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                                  예상 수익률: {property.expectedReturn}
                                </span>
                              </div>
                            </div>
                          </div>
                          <div>
                            <button
                              type="button"
                              className="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                            >
                              상세 보기
                            </button>
                          </div>
                        </div>
                      </li>
                    ))}
                  </ul>
                </div>
                <div className="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
                  <div className="flex-1 flex justify-between sm:hidden">
                    <a href="#" className="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                      이전
                    </a>
                    <a href="#" className="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                      다음
                    </a>
                  </div>
                  <div className="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
                    <div>
                      <p className="text-sm text-gray-700">
                        전체 <span className="font-medium">153</span> 건 중 <span className="font-medium">1</span> 에서 <span className="font-medium">10</span> 까지 표시
                      </p>
                    </div>
                    <div>
                      <nav className="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                        <a href="#" className="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                          <span className="sr-only">이전</span>
                          <svg className="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fillRule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clipRule="evenodd" />
                          </svg>
                        </a>
                        <a href="#" aria-current="page" className="z-10 bg-indigo-50 border-indigo-500 text-indigo-600 relative inline-flex items-center px-4 py-2 border text-sm font-medium">
                          1
                        </a>
                        <a href="#" className="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium">
                          2
                        </a>
                        <a href="#" className="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium">
                          3
                        </a>
                        <span className="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
                          ...
                        </span>
                        <a href="#" className="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium">
                          16
                        </a>
                        <a href="#" className="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                          <span className="sr-only">다음</span>
                          <svg className="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fillRule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clipRule="evenodd" />
                          </svg>
                        </a>
                      </nav>
                    </div>
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

const properties = [
  {
    id: 1,
    name: '용인시 수지구 상현동 아파트',
    type: '아파트',
    price: '5억 8,000만원',
    address: '경기도 용인시 수지구 상현동 123-45',
    aiScore: '95점',
    expectedReturn: '35%',
  },
  {
    id: 2,
    name: '서울시 강남구 논현동 오피스텔',
    type: '오피스텔',
    price: '4억 2,000만원',
    address: '서울시 강남구 논현동 234-56',
    aiScore: '92점',
    expectedReturn: '28%',
  },
  {
    id: 3,
    name: '부산시 해운대구 우동 아파트',
    type: '아파트',
    price: '6억 3,000만원',
    address: '부산시 해운대구 우동 345-67',
    aiScore: '90점',
    expectedReturn: '24%',
  },
  {
    id: 4,
    name: '인천시 송도동 오피스텔',
    type: '오피스텔',
    price: '3억 5,000만원',
    address: '인천시 연수구 송도동 456-78',
    aiScore: '87점',
    expectedReturn: '20%',
  },
  {
    id: 5,
    name: '서울시 송파구 문정동 상가',
    type: '상가',
    price: '7억 5,000만원',
    address: '서울시 송파구 문정동 567-89',
    aiScore: '85점',
    expectedReturn: '22%',
  },
]; 